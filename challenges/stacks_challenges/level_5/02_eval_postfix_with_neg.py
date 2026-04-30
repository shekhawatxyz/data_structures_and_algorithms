# Level 5b - Evaluate Postfix with Unary neg
# Write eval_postfix_with_neg(tokens) extending postfix evaluation
# with unary operator "neg".

# Complete Exact Problem Statement (from stack-challenges.md):
# **5b.** Extend your evaluator to support a unary negation token, say `"neg"`, which pops the top value and pushes its negation. For example: `["5", "neg", "3", "+"]` → `-2`. This forces you to handle operators with different arities.

def eval_postfix_with_neg(tokens):
    raise NotImplementedError('Implement eval_postfix_with_neg(tokens).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ("single negation", ["5", "neg"], -5),
    ("example with neg and plus", ["5", "neg", "3", "+"], -2),
    ("double negation", ["4", "neg", "neg"], 4),
    ("neg after binary op", ["2", "3", "+", "neg"], -5),
    ("neg with subtraction", ["10", "3", "-", "neg"], -7),
]


BOUNDARY_CASES = [
    ("neg on empty stack", ["neg"], _CASE_EXPECTS_RAISE),
    ("leftover operand invalid", ["1", "neg", "2"], _CASE_EXPECTS_RAISE),
    ("neg applied to zero", ["0", "neg"], 0),
    ("neg then division truncation", ["8", "neg", "3", "/"], -2),
    ("missing operand for binary op", ["1", "+"], _CASE_EXPECTS_RAISE),
]


INTERACTION_CASES = [
    ("mix neg with multiplication", ["2", "3", "+", "neg", "4", "*"], -20),
    ("both operands negated", ["5", "neg", "3", "neg", "+"], -8),
    ("neg interleaved with binary ops", ["6", "2", "/", "neg", "3", "*"], -9),
    ("nested neg pattern", ["9", "neg", "neg", "neg"], -9),
    ("complex chain with neg", ["7", "2", "-", "3", "neg", "*"], -15),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): eval_postfix_with_neg(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = eval_postfix_with_neg(copy.deepcopy(input_value))
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
