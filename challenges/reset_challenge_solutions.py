#!/usr/bin/env python3
"""Reset challenge solutions to unsolved placeholders while preserving tests."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

FILE_RE = re.compile(r"^(\d+)_.*\.py$")
PROMPT_MARKER_RE = re.compile(r"^# Complete Exact Problem Statement \(from .+\):$")
FILLER_LINE_RE = re.compile(r"^#$")


def find_solution_start(lines: list[str]) -> int:
    index = 0
    if lines and lines[0].startswith("#!"):
        index = 1

    while index < len(lines) and lines[index].startswith("#"):
        index += 1

    while index < len(lines) and lines[index] == "":
        index += 1

    if index < len(lines) and PROMPT_MARKER_RE.match(lines[index]):
        index += 1
        while index < len(lines) and (lines[index].startswith("#") or lines[index] == ""):
            index += 1

    while index < len(lines) and lines[index] == "":
        index += 1

    return index


def find_solution_end(lines: list[str], start_index: int) -> int:
    for index in range(start_index, len(lines) - 4):
        if all(FILLER_LINE_RE.match(lines[offset]) for offset in range(index, index + 5)):
            return index
    raise ValueError("Could not find filler separator block of '#' lines.")


def count_prompt_markers(lines: list[str]) -> int:
    return sum(1 for line in lines if PROMPT_MARKER_RE.match(line))


def ensure_tests_exist(file_path: Path, lines: list[str]) -> None:
    if not any(line.startswith("def test_") for line in lines):
        raise ValueError(f"{file_path} is missing test functions.")


def validate_python_text(file_path: Path, text: str) -> None:
    try:
        ast.parse(text)
    except SyntaxError as exc:
        raise ValueError(f"{file_path} is not valid Python: {exc.msg}.") from exc


def hash_lines(lines: list[str]) -> str:
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def is_docstring_expr(node: ast.stmt) -> bool:
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )


def is_data_container_init(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    for stmt in node.body:
        if is_docstring_expr(stmt):
            continue
        if isinstance(stmt, ast.Assign):
            targets = stmt.targets
        elif isinstance(stmt, ast.AnnAssign):
            targets = [stmt.target]
        else:
            return False

        for target in targets:
            if not (
                isinstance(target, ast.Attribute)
                and isinstance(target.value, ast.Name)
                and target.value.id == "self"
            ):
                return False

    return True


def is_data_container_class(node: ast.ClassDef) -> bool:
    body = [stmt for stmt in node.body if not is_docstring_expr(stmt)]
    if len(body) != 1:
        return False

    method = body[0]
    if not isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return False

    return method.name == "__init__" and is_data_container_init(method)


def get_node_bounds(node: ast.stmt) -> tuple[int, int]:
    if node.end_lineno is None:
        raise ValueError("AST node is missing end_lineno.")
    return node.lineno, node.end_lineno


def get_node_source(lines: list[str], node: ast.stmt) -> list[str]:
    start_lineno, end_lineno = get_node_bounds(node)
    return lines[start_lineno - 1:end_lineno]


def extract_header(lines: list[str]) -> list[str]:
    header = []
    for line in lines:
        header.append(line)
        if line.rstrip().endswith(":"):
            return header
    raise ValueError("Could not find definition header terminator ':'.")


def format_placeholder_name(
    node: ast.FunctionDef | ast.AsyncFunctionDef, class_name: str | None = None
) -> str:
    arg_names = []

    posonly = getattr(node.args, "posonlyargs", [])
    for arg in posonly:
        arg_names.append(arg.arg)
    for arg in node.args.args:
        arg_names.append(arg.arg)
    if node.args.vararg is not None:
        arg_names.append(f"*{node.args.vararg.arg}")
    elif node.args.kwonlyargs:
        arg_names.append("*")
    for arg in node.args.kwonlyargs:
        arg_names.append(arg.arg)
    if node.args.kwarg is not None:
        arg_names.append(f"**{node.args.kwarg.arg}")

    if class_name is not None and arg_names and arg_names[0] == "self":
        arg_names = arg_names[1:]

    joined = ", ".join(arg_names)
    if class_name is None:
        return f"{node.name}({joined})"
    return f"{class_name}.{node.name}({joined})"


def render_function_stub(
    lines: list[str],
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    class_name: str | None = None,
) -> list[str]:
    source_lines = get_node_source(lines, node)
    header = extract_header(source_lines)
    indent = " " * (node.col_offset + 4)
    placeholder_name = format_placeholder_name(node, class_name=class_name)
    body_line = f"{indent}raise NotImplementedError('Implement {placeholder_name}.')"
    return header + [body_line]


def render_class_stub(lines: list[str], node: ast.ClassDef) -> list[str]:
    source_lines = get_node_source(lines, node)
    header = extract_header(source_lines)
    rendered = list(header)

    methods = [
        stmt
        for stmt in node.body
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    if not methods:
        rendered.append(" " * (node.col_offset + 4) + "pass")
        return rendered

    for index, method in enumerate(methods):
        if index > 0:
            rendered.append("")
        rendered.extend(render_function_stub(lines, method, class_name=node.name))

    return rendered


def inspect_solution_layout(file_path: Path) -> tuple[str, list[str], int, int]:
    original = file_path.read_text(encoding="utf-8")
    validate_python_text(file_path, original)
    lines = original.splitlines()
    prompt_marker_count = count_prompt_markers(lines)
    if prompt_marker_count != 1:
        raise ValueError(f"{file_path} must contain exactly one prompt block marker.")
    ensure_tests_exist(file_path, lines)
    solution_start = find_solution_start(lines)
    solution_end = find_solution_end(lines, solution_start)
    ensure_tests_exist(file_path, lines[solution_end:])
    return original, lines, solution_start, solution_end


def build_reset_text(file_path: Path) -> str:
    original, lines, solution_start, solution_end = inspect_solution_layout(file_path)

    tree = ast.parse(original)
    replacement_blocks: list[str] = []

    for node in tree.body:
        start_lineno, end_lineno = get_node_bounds(node)
        if start_lineno - 1 < solution_start or end_lineno - 1 >= solution_end:
            continue

        if isinstance(node, (ast.Import, ast.ImportFrom)):
            block_lines = get_node_source(lines, node)
        elif isinstance(node, ast.ClassDef):
            if is_data_container_class(node):
                block_lines = get_node_source(lines, node)
            else:
                block_lines = render_class_stub(lines, node)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            block_lines = render_function_stub(lines, node)
        else:
            continue

        replacement_blocks.append("\n".join(block_lines))

    replacement = "\n\n".join(replacement_blocks)
    prefix = lines[:solution_start]
    suffix = lines[solution_end:]

    new_lines = list(prefix)
    if replacement:
        new_lines.append(replacement)
    new_lines.extend(suffix)
    new_text = "\n".join(new_lines) + "\n"
    validate_python_text(file_path, new_text)
    new_lines_split = new_text.splitlines()
    if count_prompt_markers(new_lines_split) != 1:
        raise ValueError(f"{file_path} lost its prompt block during reset.")
    ensure_tests_exist(file_path, new_lines_split)
    return new_text


def extract_solution_lines(file_path: Path) -> list[str]:
    _, lines, solution_start, solution_end = inspect_solution_layout(file_path)
    return lines[solution_start:solution_end]


def challenge_files(challenge_dir: Path) -> list[Path]:
    result: list[Path] = []
    for path in sorted(challenge_dir.glob("level_*/*.py")):
        if FILE_RE.match(path.name):
            result.append(path)
    return result


def plan_reset_challenge_dir(challenge_dir: Path) -> list[tuple[Path, str]]:
    files = challenge_files(challenge_dir)
    if not files:
        raise ValueError(f"{challenge_dir} has no challenge files under level_* directories.")

    plan: list[tuple[Path, str]] = []
    for file_path in files:
        original = file_path.read_text(encoding="utf-8")
        new_text = build_reset_text(file_path)
        if new_text != original:
            plan.append((file_path, new_text))
    return plan


def reset_challenge_dir(challenge_dir: Path, check_only: bool) -> list[Path]:
    plan = plan_reset_challenge_dir(challenge_dir)
    if not check_only:
        for file_path, new_text in plan:
            file_path.write_text(new_text, encoding="utf-8")
    return [file_path for file_path, _ in plan]


def build_backup_entry(file_path: Path) -> dict[str, object]:
    _, lines, solution_start, solution_end = inspect_solution_layout(file_path)
    return {
        "solution_lines": lines[solution_start:solution_end],
        "prefix_sha256": hash_lines(lines[:solution_start]),
        "suffix_sha256": hash_lines(lines[solution_end:]),
    }


def write_backup(challenge_dir: Path, backup_path: Path) -> None:
    payload = {
        "format_version": 2,
        "challenge_dir_name": challenge_dir.name,
        "files": {
            str(path.relative_to(challenge_dir)): build_backup_entry(path)
            for path in challenge_files(challenge_dir)
        },
    }
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    backup_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Reset challenge solutions while preserving prompts and tests."
    )
    parser.add_argument(
        "targets",
        nargs="*",
        help=(
            "Optional challenge directories under challenges/, such as "
            "stacks_challenges or linked_list_challenges. "
            "If omitted, all eligible challenge directories are processed."
        ),
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report files that would be reset without writing them.",
    )
    parser.add_argument(
        "--backup-to",
        help=(
            "Optional JSON file path to save current solution regions before reset. "
            "Supported only when resetting exactly one target directory."
        ),
    )
    args = parser.parse_args()

    try:
        from sync_full_problem_statements import (
            discover_challenge_dirs,
            resolve_target_dirs,
        )

        base_dir = Path(__file__).resolve().parent
        target_dirs = (
            resolve_target_dirs(base_dir, args.targets)
            if args.targets
            else discover_challenge_dirs(base_dir)
        )

        planned_by_dir: dict[Path, list[tuple[Path, str]]] = {}
        for challenge_dir in target_dirs:
            planned_by_dir[challenge_dir] = plan_reset_challenge_dir(challenge_dir)

        if args.backup_to:
            if args.check:
                raise SystemExit("--backup-to cannot be used with --check.")
            if len(target_dirs) != 1:
                raise SystemExit("--backup-to requires exactly one target directory.")
            write_backup(target_dirs[0], Path(args.backup_to))

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
            print("Files that would be reset:")
            for challenge_dir, paths in changed_by_dir.items():
                if not paths:
                    continue
                print(f"{challenge_dir.name}:")
                for path in paths:
                    print(f"- {path.relative_to(challenge_dir)}")
            return 1
        print("All challenge files are already in unsolved state.")
        return 0

    print(f"Reset {total_changed} file(s).")
    for challenge_dir, paths in changed_by_dir.items():
        if not paths:
            continue
        print(f"{challenge_dir.name}:")
        for path in paths:
            print(f"- {path.relative_to(challenge_dir)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
