# Level 8b - Next Greater Element to the Right
# Write next_greater_elements(values) in O(n).
# Return first strictly greater value to the right for each position, else -1.

# Complete Exact Problem Statement (from stack-challenges.md):
# **8b.** Given an array of integers, for each element, find the *next greater element* — i.e., the first element to its right that is strictly larger. If none exists, output `-1`. Example: `[4, 2, 6, 1, 3]` → `[6, 6, -1, 3, -1]`. Do this in O(n).


def next_greater_elements(values):
    stack = []
    result = [-1 for _ in values]
    i = 0
    while i < len(values):
        while stack and values[i] > values[stack[-1]]:
            idx = stack.pop()
            result[idx] = values[i]
        stack.append(i)
        i += 1
    return result


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


import copy

_CASE_EXPECTS_RAISE = object()


PEDAGOGY_CASES = [
    ("empty input", [], []),
    ("single element", [5], [-1]),
    ("given example", [4, 2, 6, 1, 3], [6, 6, -1, 3, -1]),
    ("strictly increasing", [1, 2, 3, 4], [2, 3, 4, -1]),
    ("strictly decreasing", [5, 4, 3, 2], [-1, -1, -1, -1]),
]


BOUNDARY_CASES = [
    ("all equal values", [2, 2, 2], [-1, -1, -1]),
    ("two elements increasing", [1, 9], [9, -1]),
    ("two elements decreasing", [9, 1], [-1, -1]),
    ("includes negatives", [-3, -2, -1], [-2, -1, -1]),
    ("duplicate then greater", [2, 2, 3], [3, 3, -1]),
]


INTERACTION_CASES = [
    ("alternating peaks", [3, 1, 4, 2, 5], [4, 4, 5, 5, -1]),
    ("late greater value", [8, 1, 2, 3, 9], [9, 2, 3, 9, -1]),
    ("multiple equal maxima", [1, 3, 3, 2], [3, -1, -1, -1]),
    ("zig-zag pattern", [2, 5, 1, 6, 0, 7], [5, 6, 6, 7, 7, -1]),
    ("complex with plateaus", [4, 4, 2, 4, 5], [5, 5, 4, 5, -1]),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): next_greater_elements(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = next_greater_elements(copy.deepcopy(input_value))
        _assert_equal(
            actual,
            expected,
            (
                f"{group_name} case {case_index} ({case_label}) produced an unexpected result "
                f"for input {input_value!r}."
            ),
        )


def test_01_pedagogical_progression():
    _run_case_group("Pedagogy", PEDAGOGY_CASES)


def test_02_boundaries_and_off_by_ones():
    _run_case_group("Boundaries", BOUNDARY_CASES)


def test_03_complex_input_interactions():
    _run_case_group("Interactions", INTERACTION_CASES)


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogical progression", test_01_pedagogical_progression),
        ("boundary and off-by-one coverage", test_02_boundaries_and_off_by_ones),
        ("complex interaction coverage", test_03_complex_input_interactions),
    ]
    _run_all_tests(TEST_CASES)
