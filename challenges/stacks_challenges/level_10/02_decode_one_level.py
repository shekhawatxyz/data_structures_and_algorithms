# Level 10b - Decode Bracket Multipliers (One Level)
# Write decode_one_level(text) for non-nested patterns like 3[ab]2[c].
# No nested brackets in this challenge.

def decode_one_level(text):
    raise NotImplementedError('Implement decode_one_level(text).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ('single group decode', '2[a]', 'aa'),
    ('given-style decode', '3[ab]2[c]', 'abababcc'),
    ('literal prefix/suffix', 'z2[ab]y', 'zababy'),
    ('multi-digit count', '10[a]', 'aaaaaaaaaa'),
    ('zero count allowed', '0[a]', ''),
]


BOUNDARY_CASES = [
    ('empty string input', '', ''),
    ('no brackets plain text', 'plain', 'plain'),
    ('missing closing bracket', '3[ab', _CASE_EXPECTS_RAISE),
    ('missing opening bracket', '3ab]', _CASE_EXPECTS_RAISE),
    ('invalid missing count', '[ab]', _CASE_EXPECTS_RAISE),
]


INTERACTION_CASES = [
    ('multiple groups and literals', '2[ab]3[cd]ef', 'ababcdcdcdef'),
    ('alternating groups with literals', 'x3[yz]2[p]q', 'xyzyzyzppq'),
    ('large count plus extra group', '10[a]b2[c]', 'aaaaaaaaaabcc'),
    ('single-count groups', '1[z]1[y]', 'zy'),
    ('empty group inside expression', '2[]a', 'a'),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): decode_one_level(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = decode_one_level(copy.deepcopy(input_value))
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
