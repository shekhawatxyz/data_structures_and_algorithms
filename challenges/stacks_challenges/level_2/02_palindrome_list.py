# Level 2b - Palindrome Check for Integer List Using Stack
# Write is_palindrome_list_stack(values) using a stack-based reverse compare.
# Do not directly reverse the list with slicing.

# Complete Exact Problem Statement (from stack-challenges.md):
# **2b.** Write a function that takes a list of integers and checks whether it is a palindrome, using only a stack. Do *not* reverse the list directly — use the stack to produce the reversed sequence and compare element by element.

def is_palindrome_list_stack(values):
    ls = []
    for v in values:
        ls.append(v)
    for _ in range(len(values)):
        if ls.pop() != values[_]:
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
    ("empty list", [], True),
    ("single element", [7], True),
    ("two equal elements", [1, 1], True),
    ("odd palindrome", [1, 2, 1], True),
    ("even palindrome", [1, 2, 2, 1], True),
]


BOUNDARY_CASES = [
    ("two unequal elements", [1, 2], False),
    ("simple non-palindrome", [1, 2, 3], False),
    ("negative values palindrome", [-1, 0, -1], True),
    ("all same values", [0, 0, 0, 0], True),
    ("near-palindrome off-by-one", [1, 2, 3, 2, 1, 0], False),
]


INTERACTION_CASES = [
    ("long odd palindrome", [1, 2, 3, 4, 3, 2, 1], True),
    ("long even palindrome", [1, 2, 3, 3, 2, 1], True),
    ("structured non-palindrome", [1, 2, 3, 4, 2, 1], False),
    (
        "large mirrored sequence",
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            19,
            18,
            17,
            16,
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
            0,
        ],
        True,
    ),
    (
        "large almost-mirrored sequence",
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        False,
    ),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): is_palindrome_list_stack(
                    value
                ),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = is_palindrome_list_stack(copy.deepcopy(input_value))
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
