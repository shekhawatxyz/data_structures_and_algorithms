# Level 6d - Shunting-Yard with Right-Associative ^
# Write infix_to_postfix_with_exponent(tokens) supporting +,-,*,/,^ and parentheses.
# ^ must be right-associative.

def infix_to_postfix_with_exponent(tokens):
    raise NotImplementedError('Implement infix_to_postfix_with_exponent(tokens).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ('simple exponent', ['2', '^', '3'], ['2', '3', '^']),
    ('right associativity core case', ['2', '^', '3', '^', '2'], ['2', '3', '2', '^', '^']),
    ('parenthesized exponent grouping', ['(', '2', '^', '3', ')', '^', '2'], ['2', '3', '^', '2', '^']),
    ('exponent with multiplication', ['2', '*', '3', '^', '2'], ['2', '3', '2', '^', '*']),
    ('addition around exponents', ['1', '+', '2', '^', '3'], ['1', '2', '3', '^', '+']),
]


BOUNDARY_CASES = [
    ('missing right operand', ['2', '^'], _CASE_EXPECTS_RAISE),
    ('leading operator', ['^', '2', '3'], _CASE_EXPECTS_RAISE),
    ('mismatched parentheses', ['(', '2', '^', '3'], _CASE_EXPECTS_RAISE),
    ('extra closing parenthesis', ['2', '^', '3', ')'], _CASE_EXPECTS_RAISE),
    ('empty tokens', [], _CASE_EXPECTS_RAISE),
]


INTERACTION_CASES = [
    ('mixed operators and exponent chain', ['3', '+', '2', '^', '3', '*', '2'], ['3', '2', '3', '^', '2', '*', '+']),
    ('nested exponent group with subtraction', ['(', '2', '^', '3', '^', '2', ')', '-', '1'], ['2', '3', '2', '^', '^', '1', '-']),
    ('multiple exponent groups', ['2', '^', '2', '+', '3', '^', '2'], ['2', '2', '^', '3', '2', '^', '+']),
    ('exponent then division', ['2', '^', '4', '/', '4'], ['2', '4', '^', '4', '/']),
    ('parenthesized base and exponent', ['(', '1', '+', '1', ')', '^', '(', '2', '+', '1', ')'], ['1', '1', '+', '2', '1', '+', '^']),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): infix_to_postfix_with_exponent(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = infix_to_postfix_with_exponent(copy.deepcopy(input_value))
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
