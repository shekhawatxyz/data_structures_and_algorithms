# Level 3a - Balanced Parentheses (Only () )
# Write is_balanced_parentheses(text) for strings containing only ( and ).


def is_balanced_parentheses(text):
    counter = []
    for t in text:
        if t == "(":
            counter.append(t)
        elif t == ")":
            if len(counter) == 0:
                return False
            else:
                counter.pop()
    if len(counter) != 0:
        return False
    return True


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ("empty string", "", True),
    ("single pair", "()", True),
    ("nested pair", "(())", True),
    ("adjacent pairs", "()()", True),
    ("nested and adjacent", "(()())", True),
]


BOUNDARY_CASES = [
    ("single opener", "(", False),
    ("single closer", ")", False),
    ("missing closer", "(()", False),
    ("missing opener", "())", False),
    ("crossing invalid pattern", "())(()", False),
]


INTERACTION_CASES = [
    ("deep valid nesting", "((())())()", True),
    ("valid mixed adjacency", "()(())(()())", True),
    ("starts with closer", ")()(", False),
    ("complex valid pattern", "((()()))(()())", True),
    ("very nested valid pattern", "(()()())(()(()))", True),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): is_balanced_parentheses(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = is_balanced_parentheses(copy.deepcopy(input_value))
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
