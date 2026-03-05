# Level 1c - Stack __str__ + Interleaved Script
# Add __str__ to print stack from top to bottom.
# Then implement an interleaved script: push 1, push 2, pop, push 3, pop, pop,
# printing the stack after each operation.

# Complete Exact Problem Statement (from stack-challenges.md):
# **1c.** Add a `__str__` method to your `Stack` class that prints the stack contents from top to bottom (so you can see what's in it at any point). Then write a script that interleaves pushes and pops — e.g., push 1, push 2, pop, push 3, pop, pop — printing the stack after each operation. Predict the full output before running.
#

import io
from contextlib import redirect_stdout


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def __str__(self):
        if len(self._items) == 0:
            return "[]"
        st = ""
        for s in reversed(self._items):
            st = f"{st} {s}"
        return st


def interleaved_stack_demo():
    s = Stack()
    s.push(1)
    print(s)
    s.push(2)
    print(s)
    s.pop()
    print(s)
    s.push(3)
    print(s)
    s.pop()
    print(s)
    s.pop()
    print(s)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


def _assert_equal(actual, expected, context):
    if actual != expected:
        raise AssertionError(f"{context} Expected {expected!r}, got {actual!r}.")


def _assert_true(condition, context):
    if not condition:
        raise AssertionError(context)


def _assert_raises(callable_obj, context):
    try:
        callable_obj()
    except Exception:
        return
    raise AssertionError(f"{context} Expected an exception, but none was raised.")


def _run_test(name, test_fn):
    try:
        test_fn()
    except NotImplementedError as exc:
        print(f"[FAIL] {name}: Function is not implemented yet ({exc}).")
        return False
    except AssertionError as exc:
        print(f"[FAIL] {name}: {exc}")
        return False
    except Exception as exc:
        print(f"[FAIL] {name}: Unexpected {type(exc).__name__}: {exc}")
        return False

    print(f"[PASS] {name}")
    return True


def _run_all_tests(test_cases):
    passed = 0
    total = len(test_cases)

    for name, fn in test_cases:
        if _run_test(name, fn):
            passed += 1

    print(f"\nPassed {passed}/{total} tests.")
    if passed != total:
        raise SystemExit(1)


import re


def _extract_numbers_from_snapshot(snapshot_text):
    bracket_chunks = re.findall(r"\[(.*?)\]", snapshot_text)
    if bracket_chunks:
        segment = bracket_chunks[-1]
    else:
        segment = snapshot_text.split(":")[-1]

    return [int(token) for token in re.findall(r"-?\d+", segment)]


def _capture_demo_snapshots():
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        returned = interleaved_stack_demo()

    if isinstance(returned, (list, tuple)):
        snapshots = [str(item) for item in returned]
    else:
        snapshots = [
            line.strip() for line in buffer.getvalue().splitlines() if line.strip()
        ]

    return snapshots


def test_01_pedagogy_str_represents_top_before_lower_values():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    rendered = str(stack)

    _assert_true(
        "1" in rendered and "2" in rendered,
        "__str__ should include both stacked values.",
    )
    _assert_true(
        rendered.find("2") < rendered.find("1"),
        "__str__ should show top value (2) before lower value (1).",
    )


def test_02_pedagogy_empty_stack_string_is_not_misleading():
    stack = Stack()
    rendered = str(stack).strip().lower()
    _assert_true(
        rendered != "",
        "__str__ for an empty stack should still communicate emptiness explicitly.",
    )


def test_03_boundaries_demo_produces_exactly_six_snapshots():
    snapshots = _capture_demo_snapshots()
    _assert_equal(
        len(snapshots),
        6,
        "Interleaved demo should expose exactly 6 snapshots for 6 operations.",
    )


def test_04_boundaries_demo_final_snapshot_is_empty():
    snapshots = _capture_demo_snapshots()
    last_numbers = _extract_numbers_from_snapshot(snapshots[-1])
    _assert_equal(
        last_numbers,
        [],
        (
            "Final snapshot should represent an empty stack after push/push/pop/push/pop/pop. "
            f"Last snapshot was: {snapshots[-1]!r}"
        ),
    )


def test_05_interactions_snapshot_progression_matches_expected_shape():
    snapshots = _capture_demo_snapshots()
    signatures = [_extract_numbers_from_snapshot(s) for s in snapshots]
    expected = [[1], [2, 1], [1], [3, 1], [1], []]
    _assert_equal(
        signatures,
        expected,
        (
            "Snapshot progression should reflect operations: push 1, push 2, pop, push 3, pop, pop. "
            "Expected top-to-bottom signatures [[1],[2,1],[1],[3,1],[1],[]]."
        ),
    )


def test_06_interactions_repeat_runs_have_stable_outputs():
    first = _capture_demo_snapshots()
    second = _capture_demo_snapshots()
    _assert_equal(
        second,
        first,
        "Interleaved demo output should be stable across repeated executions.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        (
            "pedagogy: __str__ top ordering",
            test_01_pedagogy_str_represents_top_before_lower_values,
        ),
        (
            "pedagogy: empty __str__ clarity",
            test_02_pedagogy_empty_stack_string_is_not_misleading,
        ),
        (
            "boundaries: snapshot count",
            test_03_boundaries_demo_produces_exactly_six_snapshots,
        ),
        (
            "boundaries: final empty snapshot",
            test_04_boundaries_demo_final_snapshot_is_empty,
        ),
        (
            "interactions: snapshot progression",
            test_05_interactions_snapshot_progression_matches_expected_shape,
        ),
        (
            "interactions: repeated-run stability",
            test_06_interactions_repeat_runs_have_stable_outputs,
        ),
    ]
    _run_all_tests(TEST_CASES)
