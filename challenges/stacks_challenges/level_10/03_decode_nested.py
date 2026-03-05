# Level 10c - Decode Nested Bracket Multipliers
# Write decode_nested(text) handling fully nested patterns like 3[a2[c]].
# Use stack to save and restore both partial string and repeat count.

# Complete Exact Problem Statement (from stack-challenges.md):
# **10c.** Now handle full nesting: `"3[a2[c]]"` → `"accaccacc"` and `"2[abc]3[cd]ef"` → `"abcabccdcdcdef"`. The stack must save and restore the *entire state* of your in-progress computation (the string built so far *and* the repeat count) when entering/exiting a nesting level. You are essentially using the stack to simulate a call stack.

def decode_nested(text):
    raise NotImplementedError('Implement decode_nested(text).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ('simple non-nested group', '3[a]', 'aaa'),
    ('given nested example', '3[a2[c]]', 'accaccacc'),
    ('given mixed example', '2[abc]3[cd]ef', 'abcabccdcdcdef'),
    ('nested repetition chain', '2[ab3[c]]', 'abcccabccc'),
    ('multi-digit count', '12[z]', 'zzzzzzzzzzzz'),
]


BOUNDARY_CASES = [
    ('empty string', '', ''),
    ('plain text no groups', 'plain', 'plain'),
    ('missing closing bracket', '3[a2[c]', _CASE_EXPECTS_RAISE),
    ('missing opening bracket', '3a]', _CASE_EXPECTS_RAISE),
    ('invalid count placement', '[abc]', _CASE_EXPECTS_RAISE),
]


INTERACTION_CASES = [
    ('multi-level nested case', '2[a2[b3[c]]]', 'abcccbcccabcccbccc'),
    ('adjacent nested groups', '2[x3[y]]1[z]', 'xyyyxyyyz'),
    ('nested with literals around', 'p2[a2[b]]q', 'pabbabbq'),
    ('combination of simple and nested', '3[a]2[bc3[d]]', 'aaabcdddbcddd'),
    ('invalid extra closing bracket', '2[a]]', _CASE_EXPECTS_RAISE),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): decode_nested(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = decode_nested(copy.deepcopy(input_value))
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
