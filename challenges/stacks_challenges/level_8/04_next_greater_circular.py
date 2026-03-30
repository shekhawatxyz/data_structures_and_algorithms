# Level 8d - Next Greater Element in Circular Array
# Write next_greater_elements_circular(values).
# Treat array as circular when searching to the right.

# Complete Exact Problem Statement (from stack-challenges.md):
# **8d.** Given a circular array (the element after the last is the first), find the next greater element for each position. Example: `[1, 2, 1]` → `[2, -1, 2]` (the `1` at index 2 wraps around to find `2` at index 0). (Hint: a standard trick for circular arrays — iterate through the array twice.)
#


def next_greater_elements_circular(values):
    stack = []
    modified_values = values + values
    result = [-1 for _ in values]
    for i in range(len(modified_values)):
        # if i == len(values):
        #     break
        while stack and modified_values[i] > modified_values[stack[-1]]:
            idx = stack.pop()
            if idx < len(values):
                result[idx] = modified_values[i]
        else:
            stack.append(i)
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
    ("single element", [1], [-1]),
    ("given example", [1, 2, 1], [2, -1, 2]),
    ("strictly increasing", [1, 2, 3], [2, 3, -1]),
    ("strictly decreasing", [3, 2, 1], [-1, 3, 3]),
]


BOUNDARY_CASES = [
    ("all equal values", [5, 5, 5], [-1, -1, -1]),
    ("two elements increasing", [1, 9], [9, -1]),
    ("two elements decreasing wrap", [9, 1], [-1, 9]),
    ("duplicates with one greater", [2, 2, 3], [3, 3, -1]),
    ("wraparound required at end", [3, 1, 2], [-1, 2, 3]),
]


INTERACTION_CASES = [
    ("alternating highs and lows", [2, 5, 1, 4], [5, -1, 4, 5]),
    ("multiple wraparound hits", [4, 1, 2, 3], [-1, 2, 3, 4]),
    ("plateau with single max", [1, 1, 2, 1], [2, 2, -1, 2]),
    ("complex mixed pattern", [6, 3, 8, 2, 7], [8, 8, -1, 7, 8]),
    ("descending then spike", [5, 4, 3, 6], [6, 6, 6, -1]),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): next_greater_elements_circular(
                    value
                ),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = next_greater_elements_circular(copy.deepcopy(input_value))
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
