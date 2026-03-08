# Level 6b - Shunting-Yard Infix to Postfix
# Write infix_to_postfix(tokens) for +,-,*,/ and parentheses.
# Tokens are given as a list of strings.

# Complete Exact Problem Statement (from stack-challenges.md):
# **6b.** Now implement the full shunting-yard algorithm: convert an infix expression (with the standard operators `+`, `-`, `*`, `/` and parentheses, but *not* necessarily fully parenthesised) to postfix. You will need a precedence table and a rule for left-associativity. Tokens are given as a list of strings.


def infix_to_postfix(tokens):
    st = []
    output = []
    prec = {"*": 2, "/": 2, "+": 1, "-": 1}
    if len(tokens) == 0:
        raise Exception
    for i, e in enumerate(tokens):
        if e == "(":
            st.append("(")
        elif e == ")":
            while st and st[-1] != "(":
                output.append(st.pop())
            st.pop()
        elif e in prec:
            if i == 0:
                raise Exception
            elif i == len(tokens) - 1:
                raise Exception
            if tokens[i - 1] in prec:
                raise Exception
            while st:
                if st[-1] == "(":
                    break
                if prec[st[-1]] >= prec[e]:
                    s = st.pop()
                    output.append(s)
                else:
                    break
            st.append(e)
        else:
            output.append(e)
    if "(" in st:
        raise Exception
    while st:
        output.append(st.pop())
    return output


# expression_list = tokens.split()


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ("single number token", ["42"], ["42"]),
    ("simple addition", ["3", "+", "4"], ["3", "4", "+"]),
    (
        "precedence with multiplication",
        ["3", "+", "4", "*", "2"],
        ["3", "4", "2", "*", "+"],
    ),
    (
        "parenthesized subgroup",
        ["(", "3", "+", "4", ")", "*", "2"],
        ["3", "4", "+", "2", "*"],
    ),
    (
        "left associativity subtraction",
        ["10", "-", "3", "-", "2"],
        ["10", "3", "-", "2", "-"],
    ),
]


BOUNDARY_CASES = [
    ("missing closing parenthesis", ["(", "1", "+", "2"], _CASE_EXPECTS_RAISE),
    ("extra closing parenthesis", ["1", "+", "2", ")"], _CASE_EXPECTS_RAISE),
    ("operator starts expression", ["+", "1"], _CASE_EXPECTS_RAISE),
    ("operator ends expression", ["1", "+"], _CASE_EXPECTS_RAISE),
    ("empty token list", [], _CASE_EXPECTS_RAISE),
]


INTERACTION_CASES = [
    (
        "classic shunting-yard expression",
        ["3", "+", "4", "*", "2", "/", "(", "1", "-", "5", ")"],
        ["3", "4", "2", "*", "1", "5", "-", "/", "+"],
    ),
    (
        "nested groups with multiple operators",
        ["(", "2", "+", "3", ")", "*", "(", "4", "+", "5", ")"],
        ["2", "3", "+", "4", "5", "+", "*"],
    ),
    (
        "division and multiplication chain",
        ["8", "/", "2", "*", "3", "+", "1"],
        ["8", "2", "/", "3", "*", "1", "+"],
    ),
    (
        "multiple nested parentheses",
        ["(", "1", "+", "(", "2", "*", "3", ")", ")", "-", "4"],
        ["1", "2", "3", "*", "+", "4", "-"],
    ),
    (
        "adjacent parenthesized groups",
        ["(", "1", "+", "2", ")", "*", "(", "3", "-", "4", ")", "/", "5"],
        ["1", "2", "+", "3", "4", "-", "*", "5", "/"],
    ),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): infix_to_postfix(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = infix_to_postfix(copy.deepcopy(input_value))
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
