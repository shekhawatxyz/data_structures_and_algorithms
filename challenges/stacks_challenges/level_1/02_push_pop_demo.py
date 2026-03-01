# Level 1b - Push/Pop Demo Script
# Write a function that creates a stack, pushes 1 through 5,
# then pops and prints all values in order of popping.

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

    def is_empty(self):
        return len(self._items) == 0


def push_pop_demo():
    sample = Stack()
    for _ in range(1, 6):
        sample.push(_)
    while not sample.is_empty():
        print(sample.pop())


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


def _extract_observed_sequence():
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        returned = push_pop_demo()

    printed_lines = [
        line.strip() for line in buffer.getvalue().splitlines() if line.strip()
    ]
    if printed_lines:
        observed = []
        for index, line in enumerate(printed_lines, start=1):
            numbers = re.findall(r"-?\d+", line)
            _assert_true(
                bool(numbers),
                (
                    f"Printed line {index} ({line!r}) did not contain a numeric popped value. "
                    "Expected each printed line to communicate one popped integer."
                ),
            )
            observed.append(int(numbers[-1]))
        return observed

    _assert_true(
        returned is not None,
        "push_pop_demo() should either print popped values or return them.",
    )

    if isinstance(returned, (list, tuple)):
        return list(returned)

    if hasattr(returned, "__iter__") and not isinstance(returned, (str, bytes)):
        return list(returned)

    return [returned]


def test_01_pedagogy_core_behavior_is_lifo_5_to_1():
    observed = _extract_observed_sequence()
    _assert_equal(
        observed,
        [5, 4, 3, 2, 1],
        "Demo should communicate popped values in strict LIFO order after pushing 1..5.",
    )


def test_02_boundaries_exactly_five_values_no_off_by_one():
    observed = _extract_observed_sequence()
    _assert_equal(
        len(observed), 5, "Demo should produce exactly 5 popped values (not 4 or 6)."
    )
    _assert_equal(
        sorted(observed),
        [1, 2, 3, 4, 5],
        "Demo should produce values 1..5 exactly once each.",
    )


def test_03_boundaries_output_values_are_integers():
    observed = _extract_observed_sequence()
    for index, value in enumerate(observed, start=1):
        _assert_true(
            isinstance(value, int),
            f"Observed output value #{index} should be int, got {type(value).__name__}: {value!r}.",
        )


def test_04_interactions_repeat_runs_are_independent_and_consistent():
    first = _extract_observed_sequence()
    second = _extract_observed_sequence()
    _assert_equal(
        second,
        first,
        "Running demo multiple times should not leak stack state across runs; outputs should match.",
    )


def test_05_interactions_sequence_is_strictly_descending_by_one():
    observed = _extract_observed_sequence()
    for i in range(1, len(observed)):
        _assert_equal(
            observed[i - 1] - observed[i],
            1,
            (
                f"Consecutive outputs should differ by exactly 1 in descending order; "
                f"got {observed[i - 1]} then {observed[i]}."
            ),
        )


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: core LIFO behavior", test_01_pedagogy_core_behavior_is_lifo_5_to_1),
        (
            "boundaries: exact count and no off-by-one",
            test_02_boundaries_exactly_five_values_no_off_by_one,
        ),
        (
            "boundaries: output value types",
            test_03_boundaries_output_values_are_integers,
        ),
        (
            "interactions: repeated-run independence",
            test_04_interactions_repeat_runs_are_independent_and_consistent,
        ),
        (
            "interactions: descending step consistency",
            test_05_interactions_sequence_is_strictly_descending_by_one,
        ),
    ]
    _run_all_tests(TEST_CASES)
