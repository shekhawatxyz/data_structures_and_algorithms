# Level 4b - First Offending Bracket Index
# Write first_offending_bracket_index(text).
# Return -1 if valid.
# If invalid, return first unmatched closer index, or earliest unmatched opener index.

# Complete Exact Problem Statement (from stack-challenges.md):
# **4b.** Write a function that takes a string of brackets like the above, and if it is *invalid*, returns the index of the *first* offending character (either the first unmatched closer or, if all closers matched but openers remain, the index of the earliest unmatched opener). If valid, return `-1`.

def first_offending_bracket_index(text):
    raise NotImplementedError('Implement first_offending_bracket_index(text).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ("valid nested string", "([{}])", -1),
    ("leading unmatched closer", "]{}", 0),
    ("crossed mismatch", "([)]", 2),
    ("earliest unmatched opener", "(()", 0),
    ("valid mixed blocks", "()[]{}", -1),
]


BOUNDARY_CASES = [
    ("empty string", "", -1),
    ("single opener", "(", 0),
    ("single closer", ")", 0),
    ("trailing opener after valid pair", "[](", 2),
    ("extra closer at end", "([{}]))", 6),
]


INTERACTION_CASES = [
    ("long valid sequence", "((()))[]{}", -1),
    ("valid then unmatched opener", "([{}])(", 6),
    ("late mismatch closer", "([{})", 4),
    ("many opens then extra closer", "[[[]]]]", 6),
    ("complex mismatch", "{[(])}", 3),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): first_offending_bracket_index(
                    value
                ),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = first_offending_bracket_index(copy.deepcopy(input_value))
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
