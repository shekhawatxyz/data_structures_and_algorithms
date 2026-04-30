#!/usr/bin/env python3
"""Sync exact markdown challenge statements into challenge files."""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path

LEVEL_DIR_RE = re.compile(r"^level_(\d+)$")
FILE_RE = re.compile(r"^(\d+)_.*\.py$")
LEVEL_HEADER_RE = re.compile(r"^## Level\s+(\d+)\b")
CHALLENGE_LINE_RE = re.compile(r"^\*\*([^\s*]*\d[^\s*]*)\*\*\s+.*$")
CHALLENGE_HEADING_RE = re.compile(r"^###\s+([^\s]*\d[^\s]*)\s+.+$")
FLAT_CHALLENGE_HEADER_RE = re.compile(r"^##\s+\d+\.\s+.+$")
MARKER_RE = re.compile(r"^# Complete Exact Problem Statement \(from .+\):$")


def discover_challenge_dirs(base_dir: Path) -> list[Path]:
    result = []

    for entry in sorted(base_dir.iterdir()):
        if not entry.is_dir():
            continue

        markdown_files = sorted(entry.glob("*challenges.md"))
        if len(markdown_files) != 1:
            continue

        if not any(
            child.is_dir() and LEVEL_DIR_RE.match(child.name) for child in entry.iterdir()
        ):
            continue

        result.append(entry)

    return result


def resolve_target_dirs(base_dir: Path, targets: list[str]) -> list[Path]:
    if not targets:
        return discover_challenge_dirs(base_dir)

    resolved = []
    for target in targets:
        path = (base_dir / target).resolve() if not Path(target).is_absolute() else Path(target)
        if not path.is_dir():
            raise FileNotFoundError(f"Challenge directory not found: {target}")
        resolved.append(path)

    return resolved


def parse_markdown_blocks(markdown_path: Path) -> dict[int, list[list[str]]]:
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    blocks_by_level: dict[int, list[list[str]]] = {}
    current_level: int | None = None
    i = 0

    while i < len(lines):
        level_match = LEVEL_HEADER_RE.match(lines[i])
        if level_match:
            current_level = int(level_match.group(1))
            blocks_by_level.setdefault(current_level, [])
            i += 1
            continue

        if current_level is None:
            i += 1
            continue

        if CHALLENGE_LINE_RE.match(lines[i]) or CHALLENGE_HEADING_RE.match(lines[i]):
            block = [lines[i]]
            i += 1

            while i < len(lines):
                line = lines[i]
                if (
                    LEVEL_HEADER_RE.match(line)
                    or CHALLENGE_LINE_RE.match(line)
                    or CHALLENGE_HEADING_RE.match(line)
                    or line == "---"
                ):
                    break
                block.append(line)
                i += 1

            while block and block[-1] == "":
                block.pop()

            blocks_by_level[current_level].append(block)
            continue

        i += 1

    return blocks_by_level


def parse_flat_markdown_blocks(markdown_path: Path) -> list[list[str]]:
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    blocks: list[list[str]] = []
    i = 0

    while i < len(lines):
        if not FLAT_CHALLENGE_HEADER_RE.match(lines[i]):
            i += 1
            continue

        block = [lines[i]]
        i += 1
        while i < len(lines):
            line = lines[i]
            if FLAT_CHALLENGE_HEADER_RE.match(line) or line == "---":
                break
            block.append(line)
            i += 1

        while block and block[-1] == "":
            block.pop()
        blocks.append(block)

    return blocks


def comment_block(markdown_lines: list[str], markdown_name: str) -> list[str]:
    result = [f"# Complete Exact Problem Statement (from {markdown_name}):"]
    for line in markdown_lines:
        if line:
            result.append(f"# {line}")
        else:
            result.append("#")
    return result


def validate_python_text(file_path: Path, text: str) -> None:
    try:
        ast.parse(text)
    except SyntaxError as exc:
        raise ValueError(f"{file_path} is not valid Python: {exc.msg}.") from exc


def ensure_tests_exist(file_path: Path, lines: list[str]) -> None:
    if not any(line.startswith("def test_") for line in lines):
        raise ValueError(f"{file_path} is missing test functions.")


def count_prompt_markers(lines: list[str]) -> int:
    return sum(1 for line in lines if MARKER_RE.match(line))


def challenge_files(challenge_dir: Path) -> list[tuple[int, Path]]:
    result: list[tuple[int, Path]] = []

    for level_dir in sorted(challenge_dir.iterdir()):
        if not level_dir.is_dir():
            continue

        level_match = LEVEL_DIR_RE.match(level_dir.name)
        if not level_match:
            continue

        level = int(level_match.group(1))
        for file_path in sorted(level_dir.glob("*.py")):
            if FILE_RE.match(file_path.name):
                result.append((level, file_path))

    return result


def build_rewritten_text(file_path: Path, block_lines: list[str], markdown_name: str) -> str:
    original = file_path.read_text(encoding="utf-8")
    validate_python_text(file_path, original)
    lines = original.splitlines()
    ensure_tests_exist(file_path, lines)

    shebang = []
    start_index = 0
    if lines and lines[0].startswith("#!"):
        shebang = [lines[0]]
        start_index = 1

    summary_end = start_index
    while summary_end < len(lines) and lines[summary_end].startswith("#"):
        summary_end += 1

    if summary_end == start_index:
        raise ValueError(f"{file_path} does not start with summary comments.")

    cursor = summary_end
    while cursor < len(lines) and lines[cursor] == "":
        cursor += 1

    if cursor < len(lines) and MARKER_RE.match(lines[cursor]):
        cursor += 1
        while cursor < len(lines) and (lines[cursor].startswith("#") or lines[cursor] == ""):
            cursor += 1

    rest = lines[cursor:]
    while rest and rest[0] == "":
        rest = rest[1:]

    new_lines = (
        shebang
        + lines[start_index:summary_end]
        + [""]
        + comment_block(block_lines, markdown_name)
        + [""]
        + rest
    )
    return "\n".join(new_lines) + "\n"


def validate_rewritten_text(file_path: Path, text: str) -> None:
    lines = text.splitlines()
    if count_prompt_markers(lines) != 1:
        raise ValueError(f"{file_path} must contain exactly one prompt block marker after sync.")
    ensure_tests_exist(file_path, lines)
    validate_python_text(file_path, text)


def plan_sync_challenge_dir(challenge_dir: Path) -> list[tuple[Path, str]]:
    markdown_files = sorted(challenge_dir.glob("*challenges.md"))
    if len(markdown_files) != 1:
        raise ValueError(
            f"{challenge_dir} must contain exactly one *challenges.md file."
        )

    markdown_path = markdown_files[0]
    blocks_by_level = parse_markdown_blocks(markdown_path)
    flat_blocks = parse_flat_markdown_blocks(markdown_path)
    files_by_level: dict[int, list[Path]] = {}
    for level, file_path in challenge_files(challenge_dir):
        files_by_level.setdefault(level, []).append(file_path)

    if not files_by_level:
        raise ValueError(f"{challenge_dir} has no challenge files under level_* directories.")

    markdown_levels = {level for level, blocks in blocks_by_level.items() if blocks}
    file_levels = set(files_by_level)

    if not markdown_levels and flat_blocks:
        cursor = 0
        for level, files in sorted(files_by_level.items()):
            next_cursor = cursor + len(files)
            blocks_by_level[level] = flat_blocks[cursor:next_cursor]
            cursor = next_cursor
        if cursor != len(flat_blocks):
            raise ValueError(
                f"{challenge_dir.name} has {sum(len(files) for files in files_by_level.values())} "
                f"files but {len(flat_blocks)} flat markdown challenge blocks."
            )
        markdown_levels = set(files_by_level)

    extra_file_levels = sorted(file_levels - markdown_levels)
    if extra_file_levels:
        raise ValueError(
            f"{challenge_dir.name} has file levels missing from markdown: {extra_file_levels}."
        )

    extra_markdown_levels = sorted(markdown_levels - file_levels)
    if extra_markdown_levels:
        raise ValueError(
            f"{challenge_dir.name} has markdown levels missing files: {extra_markdown_levels}."
        )

    plan: list[tuple[Path, str]] = []
    for level, files in sorted(files_by_level.items()):
        blocks = blocks_by_level.get(level)
        if blocks is None:
            raise KeyError(f"{markdown_path.name} has no block list for level {level}.")
        if len(blocks) != len(files):
            raise ValueError(
                f"{challenge_dir.name} level {level} has {len(files)} files but "
                f"{len(blocks)} markdown challenge blocks."
            )

        for file_path, block_lines in zip(files, blocks, strict=True):
            new_text = build_rewritten_text(file_path, block_lines, markdown_path.name)
            validate_rewritten_text(file_path, new_text)
            if new_text != file_path.read_text(encoding="utf-8"):
                plan.append((file_path, new_text))

    return plan


def sync_challenge_dir(challenge_dir: Path, check_only: bool) -> list[Path]:
    plan = plan_sync_challenge_dir(challenge_dir)
    if not check_only:
        for file_path, new_text in plan:
            file_path.write_text(new_text, encoding="utf-8")
    return [file_path for file_path, _ in plan]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync full markdown problem statements into challenge files."
    )
    parser.add_argument(
        "targets",
        nargs="*",
        help=(
            "Optional challenge directories under challenges/, such as "
            "linked_list_challenges or doubly_linked_list_challenges. "
            "If omitted, all eligible challenge directories are processed."
        ),
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report files that would change without writing them.",
    )
    args = parser.parse_args()

    try:
        base_dir = Path(__file__).resolve().parent
        target_dirs = resolve_target_dirs(base_dir, args.targets)

        if not target_dirs:
            print("No eligible challenge directories found.")
            return 1

        planned_by_dir: dict[Path, list[tuple[Path, str]]] = {}
        for challenge_dir in target_dirs:
            planned_by_dir[challenge_dir] = plan_sync_challenge_dir(challenge_dir)

        if not args.check:
            for plan in planned_by_dir.values():
                for file_path, new_text in plan:
                    file_path.write_text(new_text, encoding="utf-8")

        changed_by_dir: dict[Path, list[Path]] = {
            challenge_dir: [file_path for file_path, _ in plan]
            for challenge_dir, plan in planned_by_dir.items()
        }
    except (FileNotFoundError, KeyError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    total_changed = sum(len(paths) for paths in changed_by_dir.values())
    if args.check:
        if total_changed:
            print("Files out of sync:")
            for challenge_dir, paths in changed_by_dir.items():
                if not paths:
                    continue
                print(f"{challenge_dir.name}:")
                for path in paths:
                    print(f"- {path.relative_to(challenge_dir)}")
            return 1

        print("All challenge files are in sync.")
        return 0

    print(f"Updated {total_changed} file(s).")
    for challenge_dir, paths in changed_by_dir.items():
        if not paths:
            continue
        print(f"{challenge_dir.name}:")
        for path in paths:
            print(f"- {path.relative_to(challenge_dir)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
