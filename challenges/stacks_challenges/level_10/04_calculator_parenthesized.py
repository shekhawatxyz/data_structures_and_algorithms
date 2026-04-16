# Level 10d - Nested Parenthesized Calculator (+ and *)
# Write evaluate_nested_expression(text) for expressions with +, *, and parentheses.
# Use a stack-based state save/restore strategy across nesting levels.

# Complete Exact Problem Statement (from stack-challenges.md):
# **10d.** Write a simple calculator that handles nested parenthesised expressions with `+` and `*` (no precedence needed since parentheses are explicit), e.g., `"2*(3+(4*(2+1)))"` → `30`. Use a stack to save the current accumulated value and pending operator when you enter a `(`, and restore and combine when you hit `)`. This is the same state-save/restore pattern as 10c, but applied to arithmetic instead of string building.


def combine(pending_op, b, result):
    if pending_op == "+":
        result = result + b
    else:
        result = result * b
    return result


def evaluate_nested_expression(text):
    if not text:
        raise ValueError
    s = []
    result = 0
    b = ""
    pending_op = "+"
    prev = None
    for t in text:
        if t == "(":
            if prev == "closed":
                raise ValueError
            s.append((result, pending_op))
            b = ""
            pending_op = "+"
            result = 0
            prev = "open"
        elif t == ")":
            if not s:
                raise ValueError
            if prev in ("sign", "open", None):
                raise ValueError
            if b:
                result = combine(pending_op, int(b), result)
            b = ""
            prev_result, sign = s.pop()
            result = combine(sign, prev_result, result)
            prev = "closed"
        elif t.isdigit():
            b = b + t
            prev = "number"
        elif t in ["+", "*"]:
            if prev == "sign":
                raise ValueError
            if b:
                result = combine(pending_op, int(b), result)
            pending_op = t
            b = ""
            prev = "sign"
    if s:
        raise ValueError
    if b:
        result = combine(pending_op, int(b), result)
        b = ""
    return result


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ("simple addition", "1+2", 3),
    ("simple multiplication", "3*4", 12),
    ("single parenthesized sum", "(1+2)", 3),
    ("given expression", "2*(3+(4*(2+1)))", 30),
    ("fully parenthesized product", "(2+3)*(4+1)", 25),
]


BOUNDARY_CASES = [
    ("double nested expression", "((1+2)*(3+4))", 21),
    ("missing closing parenthesis", "(1+2", _CASE_EXPECTS_RAISE),
    ("missing opening parenthesis", "1+2)", _CASE_EXPECTS_RAISE),
    ("empty expression", "", _CASE_EXPECTS_RAISE),
    ("invalid operator sequence", "2**3", _CASE_EXPECTS_RAISE),
]


INTERACTION_CASES = [
    ("nested multiplication inside addition", "2*(3+(4*(5+1)))", 54),
    ("multiple grouped products and sums", "(2*(3+4))*((1+1)+1)", 42),
    ("nested sum/product mix", "((2+2)*(2+2))+(3*3)", 25),
    ("state restore heavy nesting", "((1+1)+((1+1)*(1+1)))", 6),
    ("longer grouped expression", "(3*(2+1))+((4+1)*(2+2))", 29),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): evaluate_nested_expression(
                    value
                ),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = evaluate_nested_expression(copy.deepcopy(input_value))
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
