#!/usr/bin/env python3
"""Validate challenge progress markers in markdown files."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ALLOWED_TAGS = {"", "[fluent]", "[shaky]", "[deep]"}

PROBLEM_COUNT_RE = re.compile(r"^_Problems: (?P<done>\d+)/(?P<count>\d+)\._$")
STATUS_RE = re.compile(
    r"^- \[(?P<checked>[ xX])\] \*\*(?P<title>.+)\*\* — Status:(?P<tag>.*)$"
)
LEVEL_RE = re.compile(r"^## \[(?P<checked>[ xX])\] (?P<title>Level\b.*)$")
OLD_LEVEL_RE = re.compile(r"^## Level\b")
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

    count_lines: list[tuple[int, int, int]] = []
    for line_number, line in enumerate(lines, start=1):
        match = PROBLEM_COUNT_RE.match(line)
        if match:
            count_lines.append(
                (
                    line_number,
                    int(match.group("done")),
                    int(match.group("count")),
                )
            )

    expected_count = count_challenge_files(doc_path.parent)
    if len(count_lines) != 1:
        errors.append(
            f"{rel_path}: expected exactly one '_Problems: done/total._' line; "
            f"found {len(count_lines)}."
        )
    elif count_lines[0][2] != expected_count:
        errors.append(
            f"{rel_path}:{count_lines[0][0]}: problem count is {count_lines[0][2]}, "
            f"but {expected_count} challenge file(s) exist."
        )

    status_count = 0
    checked_count = 0
    level_sections: list[tuple[int, bool, list[bool]]] = []
    current_level: tuple[int, bool, list[bool]] | None = None

    for line_number, line in enumerate(lines, start=1):
        level_match = LEVEL_RE.match(line)
        if level_match:
            current_level = (
                line_number,
                level_match.group("checked").lower() == "x",
                [],
            )
            level_sections.append(current_level)
            continue
        if OLD_LEVEL_RE.match(line):
            errors.append(f"{rel_path}:{line_number}: malformed level marker: {line!r}.")
            continue

        match = STATUS_RE.match(line)
        if not match:
            if "Status:" in line:
                errors.append(f"{rel_path}:{line_number}: malformed status marker: {line!r}.")
            continue

        status_count += 1
        is_checked = match.group("checked").lower() == "x"
        if is_checked:
            checked_count += 1
        if current_level is not None:
            current_level[2].append(is_checked)

        tag = match.group("tag").strip()
        if tag not in ALLOWED_TAGS:
            allowed = ", ".join(sorted(tag for tag in ALLOWED_TAGS if tag))
            errors.append(
                f"{rel_path}:{line_number}: invalid status tag {tag!r}; "
                f"use blank, or one of {allowed}."
            )

    if status_count != expected_count:
        errors.append(
            f"{rel_path}: found {status_count} status marker(s), "
            f"but {expected_count} challenge file(s) exist."
        )
    if count_lines and count_lines[0][1] != checked_count:
        errors.append(
            f"{rel_path}:{count_lines[0][0]}: completed problem count is {count_lines[0][1]}, "
            f"but {checked_count} status marker(s) are checked."
        )

    for line_number, level_checked, section_statuses in level_sections:
        if not section_statuses:
            continue
        expected_level_checked = all(section_statuses)
        if level_checked != expected_level_checked:
            expected_marker = "x" if expected_level_checked else " "
            errors.append(
                f"{rel_path}:{line_number}: level marker should be [{expected_marker}] "
                "based on status markers in that level."
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
