# Level 3b - Remove Adjacent Duplicates Using Stack
# Write remove_adjacent_duplicates(text) using stack logic:
# if incoming char equals top, pop; else push.

# Complete Exact Problem Statement (from stack-challenges.md):
# **3b.** Write a function that takes a string (of any characters, not just parentheses) and removes all adjacent duplicates, using a stack. For example: `"abbaca"` → `"ca"`. (Process each character: if it matches the top of the stack, pop; otherwise push. Whatever remains in the stack is the result.)

def remove_adjacent_duplicates(text):
    s = []
    if len(text) == 0:
        return ''

    for i, c in enumerate(text):
        if len(s) > 0:
            if c == s[-1]:
                s.pop()
                continue
            s.append(c)
            continue
        s.append(c)

    b = ''
    for a in s:
        b = f'{b}{a}'
    return b

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ('empty string', '', ''),
    ('single char', 'a', 'a'),
    ('one duplicate pair', 'aa', ''),
    ('no duplicates', 'ab', 'ab'),
    ('example case', 'abbaca', 'ca'),
]


BOUNDARY_CASES = [
    ('all duplicates', 'aaaa', ''),
    ('pair cancellation chain', 'abba', ''),
    ('no adjacent duplicates', 'abab', 'abab'),
    ('mixed cancellation', 'aabcca', 'ba'),
    ('full collapse palindrome-like', 'abcddcba', ''),
]


INTERACTION_CASES = [
    ('known test pattern', 'azxxzy', 'ay'),
    ('odd duplicate block', 'abbba', 'aba'),
    ('staggered cascade', 'aabccba', 'a'),
    ('multi-stage cascade', 'abcddcbae', 'e'),
    ('symmetric full collapse', 'cabbaac', 'cac'),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): remove_adjacent_duplicates(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = remove_adjacent_duplicates(copy.deepcopy(input_value))
        _assert_equal(
            actual,
            expected,
            (
                f"{group_name} case {case_index} ({case_label}) produced an unexpected result "
                f"for input {input_value!r}."
            ),
        )


def test_01_pedagogical_progression():
    _run_case_group('Pedagogy', PEDAGOGY_CASES)


def test_02_boundaries_and_off_by_ones():
    _run_case_group('Boundaries', BOUNDARY_CASES)


def test_03_complex_input_interactions():
    _run_case_group('Interactions', INTERACTION_CASES)


if __name__ == '__main__':
    TEST_CASES = [
        ('pedagogical progression', test_01_pedagogical_progression),
        ('boundary and off-by-one coverage', test_02_boundaries_and_off_by_ones),
        ('complex interaction coverage', test_03_complex_input_interactions),
    ]
    _run_all_tests(TEST_CASES)
