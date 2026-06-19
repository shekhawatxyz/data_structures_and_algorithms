# Level 2a - Reverse String Using Stack
# Write reverse_string_stack(text) that uses a stack to reverse the string.

# Complete Exact Problem Statement (from stack-challenges.md):
# **2a.** Write a function that takes a string and returns it reversed, using only a stack. (Push every character, then pop them all.)


def reverse_string_stack(text):
    stack1 = list(text)
    stack2 = [stack1.pop() for _ in range(len(stack1))]
    return "".join(stack2)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ("empty string", "", ""),
    ("single character", "a", "a"),
    ("two-character swap", "ab", "ba"),
    ("simple word", "stack", "kcats"),
    ("embedded space", "ab cd", "dc ba"),
]


BOUNDARY_CASES = [
    ("only spaces", "   ", "   "),
    ("punctuation preserved", "a!b?", "?b!a"),
    ("numeric characters", "12345", "54321"),
    ("mixed alphanumeric", "a1b2", "2b1a"),
    (
        "long repeated sequence",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ),
]


INTERACTION_CASES = [
    ("palindrome remains same", "racecar", "racecar"),
    ("mixed casing", "AaBbCc", "cCbBaA"),
    ("symbols and spaces", " hi-there! ", " !ereht-ih "),
    ("repeated pattern", "abcabc", "cbacba"),
    ("alternating chars", "xyxyxy", "yxyxyx"),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): reverse_string_stack(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = reverse_string_stack(copy.deepcopy(input_value))
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
