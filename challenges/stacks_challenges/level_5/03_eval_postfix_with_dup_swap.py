# Level 5c - Evaluate Postfix with dup and swap
# Write eval_postfix_with_stack_ops(tokens) supporting +,-,*,/,dup,swap.
# dup duplicates top item; swap swaps top two items.

def eval_postfix_with_stack_ops(tokens):
    raise NotImplementedError('Implement eval_postfix_with_stack_ops(tokens).')

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
    ('dup then add', ['2', 'dup', '+'], 4),
    ('swap then subtract', ['10', '3', 'swap', '-'], -7),
    ('given expression', ['3', 'dup', '*', '4', 'swap', '-'], -5),
    ('dup with multiplication', ['5', 'dup', '*'], 25),
    ('swap without arithmetic yet invalid end', ['1', '2', 'swap'], _CASE_EXPECTS_RAISE),
]


BOUNDARY_CASES = [
    ('dup on empty stack', ['dup'], _CASE_EXPECTS_RAISE),
    ('swap needs two items', ['1', 'swap'], _CASE_EXPECTS_RAISE),
    ('binary operator missing args', ['+'], _CASE_EXPECTS_RAISE),
    ('division by zero through stack ops', ['0', 'dup', '/'], _CASE_EXPECTS_RAISE),
    ('leftover stack invalid', ['1', '2'], _CASE_EXPECTS_RAISE),
]


INTERACTION_CASES = [
    ('dup swap plus composition', ['1', '2', 'swap', 'dup', '+', '+'], 4),
    ('dup dup multiply swap add', ['5', 'dup', 'dup', '*', 'swap', '+'], 30),
    ('dup then square then divide after swap', ['4', 'dup', '*', '2', 'swap', '/'], 0),
    ('swap with neg-like arithmetic effect', ['8', '3', 'swap', '-', '2', '*'], -10),
    ('long mixed stack-manip expression', ['2', 'dup', '3', 'swap', '*', '+'], 8),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): eval_postfix_with_stack_ops(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = eval_postfix_with_stack_ops(copy.deepcopy(input_value))
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
