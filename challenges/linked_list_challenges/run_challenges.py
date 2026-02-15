#!/usr/bin/env python3
"""Run linked-list challenge files level-by-level or all at once."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


LEVEL_DIR_PATTERN = re.compile(r"^level_(\d+)$")


def discover_level_dirs(base_dir: Path) -> list[tuple[int, Path]]:
    levels: list[tuple[int, Path]] = []
    for entry in base_dir.iterdir():
        if not entry.is_dir():
            continue
        match = LEVEL_DIR_PATTERN.match(entry.name)
        if not match:
            continue
        levels.append((int(match.group(1)), entry))
    return sorted(levels, key=lambda pair: pair[0])


def discover_challenge_files(level_dirs: list[tuple[int, Path]]) -> list[tuple[int, Path]]:
    challenge_files: list[tuple[int, Path]] = []
    for level, level_dir in level_dirs:
        for file_path in sorted(level_dir.glob("*.py")):
            challenge_files.append((level, file_path))
    return challenge_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run linked-list challenge files. "
            "By default, runs every challenge across all levels."
        )
    )
    parser.add_argument(
        "--level",
        type=int,
        action="append",
        help="Run only a specific level (repeatable), e.g. --level 1 --level 3.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List selected challenge files without running them.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    base_dir = Path(__file__).resolve().parent
    discovered = discover_level_dirs(base_dir)

    if not discovered:
        print("No level directories found (expected folders like level_1, level_2, ...).")
        return 1

    available_levels = {level for level, _ in discovered}
    selected_levels = set(args.level) if args.level else available_levels

    invalid = sorted(level for level in selected_levels if level not in available_levels)
    if invalid:
        print(
            f"Invalid level(s): {invalid}. "
            f"Available levels: {sorted(available_levels)}."
        )
        return 2

    selected_dirs = [pair for pair in discovered if pair[0] in selected_levels]
    challenge_files = discover_challenge_files(selected_dirs)

    if not challenge_files:
        print("No challenge Python files found for the selected level(s).")
        return 1

    if args.list:
        for level, file_path in challenge_files:
            print(f"level_{level}: {file_path.name}")
        return 0

    print(f"Running {len(challenge_files)} challenge file(s)...\n")

    passed = 0
    failed = 0
    failed_files: list[tuple[int, Path, int]] = []

    for level, file_path in challenge_files:
        print(f"=== level_{level} / {file_path.name} ===")
        result = subprocess.run(
            [sys.executable, str(file_path)],
            capture_output=True,
            text=True,
            cwd=base_dir,
        )

        if result.stdout:
            print(result.stdout.rstrip())
        if result.stderr:
            print(result.stderr.rstrip())

        if result.returncode == 0:
            passed += 1
            print(f"[FILE PASS] {file_path.name}\n")
        else:
            failed += 1
            failed_files.append((level, file_path, result.returncode))
            print(f"[FILE FAIL] {file_path.name} (exit code {result.returncode})\n")

    print("Summary")
    print(f"- Passed files: {passed}")
    print(f"- Failed files: {failed}")
    print(f"- Total files: {len(challenge_files)}")

    if failed_files:
        print("\nFailed file list:")
        for level, file_path, exit_code in failed_files:
            print(f"- level_{level} / {file_path.name} (exit code {exit_code})")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
