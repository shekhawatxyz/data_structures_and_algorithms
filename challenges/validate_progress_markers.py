#!/usr/bin/env python3
"""Validate challenge progress markers in markdown files."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROBLEM_COUNT_RE = re.compile(r"^_Problems: (?:(?:\d+)/)?(?P<count>\d+)\._$")
STATUS_RE = re.compile(
    r"^- \[(?P<checked>[ xX])\] \*\*(?P<title>.+)\*\*(?: — Status:(?P<status>.*))?$"
)
LEVEL_RE = re.compile(r"^## (?:\[[ xX]\] )?Level\b")
LEVEL_DIR_RE = re.compile(r"^level_\d+$")


def discover_challenge_docs() -> list[Path]:
    docs: list[Path] = []
    for challenge_dir in sorted(ROOT.glob("*_challenges")):
        if not challenge_dir.is_dir():
            continue
        docs.extend(sorted(challenge_dir.glob("*.md")))
    return docs


def count_challenge_files(challenge_dir: Path) -> int:
    total = 0
    for level_dir in challenge_dir.iterdir():
        if not level_dir.is_dir() or not LEVEL_DIR_RE.match(level_dir.name):
            continue
        total += len(list(level_dir.glob("*.py")))
    return total


def validate_doc(doc_path: Path) -> list[str]:
    lines = doc_path.read_text(encoding="utf-8").splitlines()
    rel_path = doc_path.relative_to(ROOT.parent)
    errors: list[str] = []

    count_lines: list[tuple[int, int]] = []
    for line_number, line in enumerate(lines, start=1):
        match = PROBLEM_COUNT_RE.match(line)
        if match:
            count_lines.append(
                (
                    line_number,
                    int(match.group("count")),
                )
            )

    expected_count = count_challenge_files(doc_path.parent)
    if len(count_lines) != 1:
        errors.append(
            f"{rel_path}: expected exactly one '_Problems: total._' line; "
            f"found {len(count_lines)}."
        )
    elif count_lines[0][1] != expected_count:
        errors.append(
            f"{rel_path}:{count_lines[0][0]}: problem count is {count_lines[0][1]}, "
            f"but {expected_count} challenge file(s) exist."
        )

    status_count = 0

    for line_number, line in enumerate(lines, start=1):
        if LEVEL_RE.match(line):
            continue

        match = STATUS_RE.match(line)
        if not match:
            if "Status:" in line:
                errors.append(f"{rel_path}:{line_number}: malformed status marker: {line!r}.")
            continue

        status_count += 1

    if status_count != expected_count:
        errors.append(
            f"{rel_path}: found {status_count} problem marker(s), "
            f"but {expected_count} challenge file(s) exist."
        )

    return errors


def main() -> int:
    docs = discover_challenge_docs()
    errors: list[str] = []
    for doc_path in docs:
        errors.extend(validate_doc(doc_path))

    if errors:
        print("Progress marker validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Progress marker validation passed for {len(docs)} markdown file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
