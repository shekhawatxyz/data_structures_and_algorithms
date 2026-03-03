# Level 4a - Balanced Brackets Across Types
# Write is_valid_brackets(text) for (), [], {} with strict type matching.

# Complete Exact Problem Statement (from stack-challenges.md):
# **4a.** Extend your balanced-parentheses checker from 3a to handle three types: `()`, `[]`, and `{}`. Each closer must match the most recently unmatched opener of the *correct* type. For example: `"([{}])"` is valid; `"([)]"` is not.


def is_valid_brackets(text):
    brackets = []
    closers = {")": "(", "]": "[", "}": "{"}
    for t in text:
        if t == "(" or t == "{" or t == "[":
            brackets.append(t)
        else:
            if t in closers.keys():
                if len(brackets) == 0:
                    return False
                elif brackets[-1] == closers[t]:
                    brackets.pop()
                else:
                    return False
            # if t == ")":
            #     if len(brackets) == 0:
            #         return False
            #     elif brackets[-1] == "(":
            #         brackets.pop()
            #     else:
            #         return False
            # elif t == "]":
            #     if len(brackets) == 0:
            #         return False
            #     elif brackets[-1] == "[":
            #         brackets.pop()
            #     else:
            #         return False
            # elif t == "}":
            #     if len(brackets) == 0:
            #         return False
            #     elif brackets[-1] == "{":
            #         brackets.pop()
            #     else:
            #         return False
            # if t == ")":
    if len(brackets) == 0:
        return True
    else:
        return False


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ("single pair type", "()", True),
    ("independent pair types", "()[]{}", True),
    ("nested mixed pairs", "([{}])", True),
    ("nested repeated structure", "{[()()[]]}", True),
]


BOUNDARY_CASES = [
    ("single opener", "(", False),
    ("single closer", "]", False),
    ("type mismatch", "(]", False),
    ("crossed nesting", "([)]", False),
    ("unfinished nesting", "[({})", False),
]


INTERACTION_CASES = [
    ("deep valid expression", "(({{[[]]}}))", True),
    ("valid mixed repetition", "([{}{}[]])", True),
    ("invalid reversed order", "}{", False),
    ("valid multi-block", "[[[[]]]](){}", True),
    ("invalid mixed mismatch late", "{[(])}", False),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): is_valid_brackets(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = is_valid_brackets(copy.deepcopy(input_value))
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
