# Level 9d - Maximal Rectangle of 1s in Binary Matrix
# Write maximal_rectangle_binary_matrix(matrix) using row-wise histogram
# reduction plus largest-rectangle-in-histogram logic.

def maximal_rectangle_binary_matrix(matrix):
    raise NotImplementedError('Implement maximal_rectangle_binary_matrix(matrix).')

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
    ('empty matrix', [], 0),
    ('matrix with empty row', [[]], 0),
    ('single cell one', [[1]], 1),
    ('single cell zero', [[0]], 0),
    ('classic benchmark matrix', [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]], 6),
]


BOUNDARY_CASES = [
    ('all zeros matrix', [[0, 0], [0, 0]], 0),
    ('all ones matrix 2x2', [[1, 1], [1, 1]], 4),
    ('single row matrix', [[1, 0, 1, 1]], 2),
    ('single column matrix', [[1], [1], [0], [1]], 2),
    ('narrow matrix with one rectangle', [[0, 1, 1, 0]], 2),
]


INTERACTION_CASES = [
    ('wide rectangle across middle rows', [[1, 1, 1, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 6),
    ('staircase ones pattern', [[1, 0, 0], [1, 1, 0], [1, 1, 1]], 4),
    ('disjoint blocks pick max', [[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1]], 4),
    ('tall thin rectangle dominates', [[1, 0], [1, 0], [1, 0], [1, 1]], 4),
    ('complex mixed matrix', [[0, 1, 1], [1, 1, 1], [1, 1, 0]], 4),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): maximal_rectangle_binary_matrix(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = maximal_rectangle_binary_matrix(copy.deepcopy(input_value))
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
