#!/usr/bin/env python3
"""Restore challenge solution regions from a backup JSON file."""

from __future__ import annotations

import argparse
from functools import lru_cache
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))


@lru_cache(maxsize=1)
def load_reset_helpers():
    from reset_challenge_solutions import (
        count_prompt_markers,
        ensure_tests_exist,
        find_solution_end,
        find_solution_start,
        hash_lines,
        validate_python_text,
    )

    return (
        count_prompt_markers,
        ensure_tests_exist,
        find_solution_end,
        find_solution_start,
        hash_lines,
        validate_python_text,
    )


def normalize_solution_payload(solution_payload: object) -> tuple[list[str], str | None, str | None]:
    if isinstance(solution_payload, dict):
        lines = solution_payload["solution_lines"]
        if not isinstance(lines, list):
            raise ValueError("Backup solution_lines must be a list of strings.")
        if not all(isinstance(line, str) for line in lines):
            raise ValueError("Backup solution_lines entries must all be strings.")
        return (
            lines,
            solution_payload.get("prefix_sha256"),
            solution_payload.get("suffix_sha256"),
        )

    if isinstance(solution_payload, list):
        if not all(isinstance(line, str) for line in solution_payload):
            raise ValueError("Backup solution_lines entries must all be strings.")
        return solution_payload, None, None

    if isinstance(solution_payload, str):
        return solution_payload.splitlines(), None, None

    raise ValueError("Unsupported backup entry format.")


def build_restored_text(file_path: Path, solution_payload: object) -> str:
    (
        count_prompt_markers,
        ensure_tests_exist,
        find_solution_end,
        find_solution_start,
        hash_lines,
        validate_python_text,
    ) = load_reset_helpers()

    original = file_path.read_text(encoding="utf-8")
    validate_python_text(file_path, original)
    lines = original.splitlines()
    if count_prompt_markers(lines) != 1:
        raise ValueError(f"{file_path} must contain exactly one prompt block marker.")
    solution_start = find_solution_start(lines)
    solution_end = find_solution_end(lines, solution_start)
    ensure_tests_exist(file_path, lines[solution_end:])

    replacement_lines, prefix_sha256, suffix_sha256 = normalize_solution_payload(
        solution_payload
    )
    if prefix_sha256 is not None and hash_lines(lines[:solution_start]) != prefix_sha256:
        raise ValueError(f"{file_path} prefix does not match the backup frame.")
    if suffix_sha256 is not None and hash_lines(lines[solution_end:]) != suffix_sha256:
        raise ValueError(f"{file_path} suffix does not match the backup frame.")

    prefix = lines[:solution_start]
    suffix = lines[solution_end:]
    new_lines = prefix + replacement_lines + suffix
    new_text = "\n".join(new_lines) + "\n"
    validate_python_text(file_path, new_text)
    new_lines_split = new_text.splitlines()
    if count_prompt_markers(new_lines_split) != 1:
        raise ValueError(f"{file_path} lost its prompt block during restore.")
    ensure_tests_exist(file_path, new_lines_split)
    return new_text


def plan_restore(target_dir: Path, payload: dict[str, object]) -> list[tuple[Path, str]]:
    files_payload = payload.get("files")
    if not isinstance(files_payload, dict) or not files_payload:
        raise ValueError("Backup payload must contain a non-empty 'files' mapping.")

    plan: list[tuple[Path, str]] = []
    for relative_path, solution_payload in files_payload.items():
        if not isinstance(relative_path, str):
            raise ValueError("Backup file paths must be strings.")
        relative = Path(relative_path)
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"Unsafe backup path: {relative_path}")
        file_path = target_dir / relative
        if not file_path.is_file():
            raise FileNotFoundError(f"Target file not found for restore: {file_path}")
        new_text = build_restored_text(file_path, solution_payload)
        original = file_path.read_text(encoding="utf-8")
        if new_text != original:
            plan.append((file_path, new_text))

    return plan


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Restore challenge solution regions from a backup JSON file."
    )
    parser.add_argument("backup_file", help="Path to a backup JSON file.")
    parser.add_argument(
        "target_dir",
        help="Challenge directory to restore into, e.g. linked_list_challenges.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the restore and report files that would change without writing.",
    )
    args = parser.parse_args()

    try:
        backup_path = Path(args.backup_file)
        target_dir = (
            Path(args.target_dir)
            if Path(args.target_dir).is_absolute()
            else Path.cwd() / args.target_dir
        )
        if not target_dir.is_dir():
            raise ValueError(f"Target directory not found: {target_dir}")

        payload = json.loads(backup_path.read_text(encoding="utf-8"))
        expected_dir_name = payload.get("challenge_dir_name")
        if isinstance(expected_dir_name, str) and target_dir.name != expected_dir_name:
            raise ValueError(
                f"Backup targets {expected_dir_name}, but restore target is {target_dir.name}."
            )
        plan = plan_restore(target_dir, payload)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.check:
        if plan:
            print("Files that would be restored:")
            for file_path, _ in plan:
                print(f"- {file_path.relative_to(target_dir)}")
            return 1
        print("Target directory already matches the backup.")
        return 0

    for file_path, new_text in plan:
        file_path.write_text(new_text, encoding="utf-8")

    print(f"Restored {len(plan)} file(s).")
    for path, _ in plan:
        print(f"- {path.relative_to(target_dir)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
