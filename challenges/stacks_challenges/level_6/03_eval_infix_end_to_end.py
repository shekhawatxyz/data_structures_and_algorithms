# Level 6c - Evaluate Infix End-to-End
# Write evaluate_infix(expression) that converts infix to postfix
# and evaluates it using integer division truncating toward zero.

# Complete Exact Problem Statement (from stack-challenges.md):
# **6c.** Chain your 6b converter with your 5a evaluator to evaluate infix expressions end-to-end. Test on: `"3 + 4 * 2 / ( 1 - 5 )"` → should give `1` (with integer division).


def eval_postfix_with_neg(tokens):
    nums = []
    binary_operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b),
    }
    unary_operators = {"neg": lambda a: -a}
    for t in tokens:
        if t in unary_operators:
            if not nums:
                raise Exception
            nv = unary_operators[t](int(nums[-1]))
            nums.pop()
            nums.append(nv)
        elif t in binary_operators:
            n = binary_operators[t](int(nums[-2]), int(nums[-1]))
            nums.pop()
            nums.pop()
            nums.append(n)
        else:
            nums.append(t)
    if len(nums) > 1:
        raise Exception
    return int(nums[0])


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
            output.append(int(e))
    if "(" in st:
        raise Exception
    while st:
        output.append(st.pop())
    return output


def evaluate_infix(expression):
    e = expression.split()
    return eval_postfix_with_neg(infix_to_postfix(e))


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ("single number", "42", 42),
    ("simple addition", "1 + 2", 3),
    ("simple multiplication", "3 * 4", 12),
    ("given expression", "3 + 4 * 2 / ( 1 - 5 )", 1),
    ("nested parentheses", "( 2 + 3 ) * ( 4 + 1 )", 25),
]


BOUNDARY_CASES = [
    ("division truncates toward zero", "7 / 3 + 2", 4),
    ("negative division truncates toward zero", "-7 / 3 + 1", -1),
    ("incomplete expression", "3 +", _CASE_EXPECTS_RAISE),
    ("unbalanced parentheses", "( 1 + 2", _CASE_EXPECTS_RAISE),
    ("empty expression", "", _CASE_EXPECTS_RAISE),
]


INTERACTION_CASES = [
    ("multiple nested groups", "( ( 1 + 2 ) * ( 3 + 4 ) )", 21),
    ("mixed precedence without outer parentheses", "2 + 3 * 4 - 5", 9),
    ("left associativity division chain", "20 / 3 / 2", 3),
    ("complex nested arithmetic", "2 * ( 3 + ( 4 * ( 5 - 1 ) ) )", 38),
    ("balanced expression with many ops", "( 8 - 3 ) * ( 2 + 6 / 3 )", 20),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): evaluate_infix(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = evaluate_infix(copy.deepcopy(input_value))
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
