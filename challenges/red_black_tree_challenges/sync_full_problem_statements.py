#!/usr/bin/env python3
"""Compatibility wrapper for the repo-level sync script."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    repo_script = Path(__file__).resolve().parents[1] / "sync_full_problem_statements.py"
    cmd = [sys.executable, str(repo_script), "red_black_tree_challenges", *sys.argv[1:]]
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
