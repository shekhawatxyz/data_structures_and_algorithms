# Level 9b - Nearest Smaller Indices Left and Right
# Write nearest_smaller_indices(heights) returning (left, right).
# left[i] = index of nearest smaller bar to left else -1.
# right[i] = index of nearest smaller bar to right else len(heights).

def nearest_smaller_indices(heights):
    raise NotImplementedError('Implement nearest_smaller_indices(heights).')

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
    ('empty input', [], ([], [])),
    ('single bar', [5], ([-1], [1])),
    ('given example', [2, 1, 5, 6, 2, 3], ([-1, -1, 1, 2, 1, 4], [1, 6, 4, 4, 6, 6])),
    ('strictly increasing', [1, 2, 3, 4], ([-1, 0, 1, 2], [4, 4, 4, 4])),
    ('strictly decreasing', [4, 3, 2, 1], ([-1, -1, -1, -1], [1, 2, 3, 4])),
]


BOUNDARY_CASES = [
    ('all equal heights', [2, 2, 2], ([-1, -1, -1], [3, 3, 3])),
    ('includes zero', [0, 2, 0], ([-1, 0, -1], [3, 2, 3])),
    ('two bars increasing', [1, 3], ([-1, 0], [2, 2])),
    ('two bars decreasing', [3, 1], ([-1, -1], [1, 2])),
    ('symmetric pattern', [3, 1, 3], ([-1, -1, 1], [1, 3, 3])),
]


INTERACTION_CASES = [
    ('mixed valley pattern', [4, 2, 0, 3, 2, 5], ([-1, -1, -1, 2, 2, 4], [1, 2, 6, 4, 6, 6])),
    ('peak middle symmetry', [5, 4, 3, 4, 5], ([-1, -1, -1, 2, 3], [1, 2, 5, 5, 5])),
    ('plateau with dips', [2, 1, 2, 1, 2], ([-1, -1, 1, -1, 3], [1, 5, 3, 5, 5])),
    ('late minimum', [3, 3, 3, 1], ([-1, -1, -1, -1], [3, 3, 3, 4])),
    ('complex mixed heights', [1, 3, 2, 4, 2], ([-1, 0, 0, 2, 0], [5, 2, 5, 4, 5])),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): nearest_smaller_indices(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = nearest_smaller_indices(copy.deepcopy(input_value))
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
