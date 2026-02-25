# Level 9c - Largest Histogram Rectangle (O(n) Stack)
# Write largest_rectangle_stack(heights) using one monotonic stack pass
# and area computation when popping.

def largest_rectangle_stack(heights):
    raise NotImplementedError('Implement largest_rectangle_stack(heights).')

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
    ('empty histogram', [], 0),
    ('single bar', [5], 5),
    ('two bars', [2, 4], 4),
    ('uniform bars', [2, 2, 2], 6),
    ('given example', [2, 1, 5, 6, 2, 3], 10),
]


BOUNDARY_CASES = [
    ('includes zero-height bar', [0, 1, 0], 1),
    ('all zeros', [0, 0, 0], 0),
    ('strictly increasing', [1, 2, 3, 4], 6),
    ('strictly decreasing', [4, 3, 2, 1], 6),
    ('single zero bar', [0], 0),
]


INTERACTION_CASES = [
    ('classic second benchmark', [6, 2, 5, 4, 5, 1, 6], 12),
    ('valley in middle', [5, 4, 1, 2], 8),
    ('plateau then dip', [3, 3, 3, 1, 3], 9),
    ('multiple local maxima', [2, 4, 2, 1], 6),
    ('wide low bar dominates', [1, 1, 1, 1, 5], 5),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): largest_rectangle_stack(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = largest_rectangle_stack(copy.deepcopy(input_value))
        _assert_equal(
            actual,
            expected,
            (
                f"{group_name} case {case_index} ({case_label}) produced an unexpected result "
                f"for input {input_value!r}."
            ),
        )


def test_01_pedagogical_progression():
    _run_case_group('Pedagogy', PEDAGOGY_CASES)


def test_02_boundaries_and_off_by_ones():
    _run_case_group('Boundaries', BOUNDARY_CASES)


def test_03_complex_input_interactions():
    _run_case_group('Interactions', INTERACTION_CASES)


if __name__ == '__main__':
    TEST_CASES = [
        ('pedagogical progression', test_01_pedagogical_progression),
        ('boundary and off-by-one coverage', test_02_boundaries_and_off_by_ones),
        ('complex interaction coverage', test_03_complex_input_interactions),
    ]
    _run_all_tests(TEST_CASES)
