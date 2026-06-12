#!/usr/bin/env python3
"""Regression checks for progress-marker validation rules."""

from __future__ import annotations

import validate_progress_markers as validator


def assert_matches(pattern, text: str) -> None:
    if not pattern.match(text):
        raise AssertionError(f"Expected pattern to match: {text!r}")


def assert_problem_count(text: str, expected: str) -> None:
    match = validator.PROBLEM_COUNT_RE.match(text)
    if not match:
        raise AssertionError(f"Expected problem count to match: {text!r}")
    actual = match.group("count")
    if actual != expected:
        raise AssertionError(f"Expected count {expected!r}, got {actual!r}.")


def main() -> int:
    assert_problem_count("_Problems: 38._", "38")
    assert_problem_count("_Problems: 13/38._", "38")

    assert_matches(
        validator.STATUS_RE,
        "- [x] **4.1** — Status: shaky",
    )
    assert_matches(
        validator.STATUS_RE,
        "- [x] **4.2** — Status: hard",
    )
    assert_matches(
        validator.STATUS_RE,
        "- [ ] **1a — Problem name** — Status: deep practice",
    )
    assert_matches(
        validator.STATUS_RE,
        "- [ ] **1b — Problem without status**",
    )

    assert_matches(validator.LEVEL_RE, "## Level 1 — Basics")
    assert_matches(validator.LEVEL_RE, "## [x] Level 1 — Old format")
    assert_matches(validator.LEVEL_RE, "## [ ] Level 2 — Old format")

    print("Progress marker validator regression checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
