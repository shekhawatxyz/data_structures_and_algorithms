# Level 6a - Fully Parenthesized Infix to Postfix
# Write fully_parenthesized_infix_to_postfix(expression).
# Input expression is space-separated and fully parenthesized.
# Return postfix tokens as a list of strings.

# Complete Exact Problem Statement (from stack-challenges.md):
# **6a.** Start simple: write a function that converts a *fully parenthesised* infix expression to postfix. By "fully parenthesised" I mean every operation is wrapped: `"( ( 3 + 4 ) * 2 )"`. This is easier because the parentheses already tell you the structure — you don't need precedence rules yet. Tokens are space-separated. Use a stack.


def fully_parenthesized_infix_to_postfix(expression):
    operators = ["+", "-", "/", "*"]
    expression_list = expression.split()
    st = []
    output = []
    count = 0
    num_count = 0
    for i, e in enumerate(expression_list):
        if e == "(":
            count += 1
        elif e == ")":
            if count < 0:
                raise Exception
            if len(st) == 0:
                raise Exception
            o = st.pop()
            if num_count < 2:
                raise Exception
            output.append(o)
            count -= 1
            num_count -= 1
        elif e in operators:
            if expression_list[i - 1] == "(":
                raise Exception
            st.append(e)
        else:
            output.append(e)
            num_count += 1
    if count != 0:
        raise Exception
    return output


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ("single number", "42", ["42"]),
    ("single parenthesized sum", "( 1 + 2 )", ["1", "2", "+"]),
    ("nested multiplication example", "( ( 3 + 4 ) * 2 )", ["3", "4", "+", "2", "*"]),
    (
        "two nested groups",
        "( ( 10 - 2 ) / ( 1 + 1 ) )",
        ["10", "2", "-", "1", "1", "+", "/"],
    ),
    (
        "left-deep addition chain",
        "( ( ( 1 + 2 ) + 3 ) + 4 )",
        ["1", "2", "+", "3", "+", "4", "+"],
    ),
]


BOUNDARY_CASES = [
    ("missing closing parenthesis", "( 3 + 4", _CASE_EXPECTS_RAISE),
    ("extra closing parenthesis", "3 + 4 )", _CASE_EXPECTS_RAISE),
    ("empty parentheses invalid", "( )", _CASE_EXPECTS_RAISE),
    ("operator missing right operand", "( ( 1 + 2 ) * )", _CASE_EXPECTS_RAISE),
    ("operator missing left operand", "( * 1 2 )", _CASE_EXPECTS_RAISE),
]


INTERACTION_CASES = [
    (
        "deeply nested mixed operators",
        "( ( ( 2 * 3 ) + ( 4 / 2 ) ) - 5 )",
        ["2", "3", "*", "4", "2", "/", "+", "5", "-"],
    ),
    (
        "nested subtraction and multiplication",
        "( ( 8 - ( 3 + 1 ) ) * ( 2 + 2 ) )",
        ["8", "3", "1", "+", "-", "2", "2", "+", "*"],
    ),
    (
        "multi-level right nesting",
        "( 1 + ( 2 * ( 3 + 4 ) ) )",
        ["1", "2", "3", "4", "+", "*", "+"],
    ),
    (
        "combined divisions",
        "( ( 20 / 5 ) / ( 2 + 2 ) )",
        ["20", "5", "/", "2", "2", "+", "/"],
    ),
    (
        "chain with all operators",
        "( ( ( 9 - 3 ) * 2 ) + ( 8 / 4 ) )",
        ["9", "3", "-", "2", "*", "8", "4", "/", "+"],
    ),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(
                    input_value
                ): fully_parenthesized_infix_to_postfix(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = fully_parenthesized_infix_to_postfix(copy.deepcopy(input_value))
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
