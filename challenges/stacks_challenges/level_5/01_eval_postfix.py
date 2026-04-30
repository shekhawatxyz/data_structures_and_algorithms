# Level 5a - Evaluate Postfix Expression
# Write eval_postfix(tokens) supporting +, -, *, / with integer division
# truncating toward zero.

# Complete Exact Problem Statement (from stack-challenges.md):
# **5a.** Write a function that evaluates a postfix (reverse Polish notation) expression. Input is a list of tokens like `["3", "4", "+", "2", "*"]` → `14`. Support `+`, `-`, `*`, `/` (integer division, truncating toward zero).

def eval_postfix(tokens):
    raise NotImplementedError('Implement eval_postfix(tokens).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ("single operand", ["2"], 2),
    ("simple addition", ["3", "4", "+"], 7),
    ("simple subtraction order", ["10", "3", "-"], 7),
    ("simple multiplication", ["6", "7", "*"], 42),
    ("given expression", ["3", "4", "+", "2", "*"], 14),
]


BOUNDARY_CASES = [
    ("integer division truncates positive", ["7", "3", "/"], 2),
    ("integer division truncates toward zero negative", ["-7", "3", "/"], -2),
    ("missing operands", ["+"], _CASE_EXPECTS_RAISE),
    ("leftover operands", ["1", "2"], _CASE_EXPECTS_RAISE),
    ("division by zero should raise", ["4", "0", "/"], _CASE_EXPECTS_RAISE),
]


INTERACTION_CASES = [
    (
        "classic long postfix expression",
        ["5", "1", "2", "+", "4", "*", "+", "3", "-"],
        14,
    ),
    ("mixed operations chain", ["4", "13", "5", "/", "+"], 6),
    ("nested-like stack interaction", ["2", "3", "11", "+", "5", "-", "*"], 18),
    ("negative intermediate result", ["2", "3", "-", "4", "*"], -4),
    ("multiple divisions and adds", ["20", "3", "/", "2", "/", "1", "+"], 4),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): eval_postfix(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = eval_postfix(copy.deepcopy(input_value))
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
