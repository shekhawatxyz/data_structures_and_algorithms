# Level 1.3 - first_unique_char
# Return the index of the first character that appears exactly once.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 3. `first_unique_char`
#
# ```python
# def first_unique_char(s: str) -> int:
# ```
#
# Return the index of the first character in `s` that appears exactly once. If no such character exists, return `-1`.
#
# Examples:
# - `first_unique_char("leetcode")` → `0`
# - `first_unique_char("loveleetcode")` → `2`
# - `first_unique_char("aabb")` → `-1`
# - `first_unique_char("")` → `-1`

def first_unique_char(s):
    raise NotImplementedError('Implement first_unique_char(s).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_first_char_is_unique():
    _assert_equal(first_unique_char("leetcode"), 0,
                  "In 'leetcode', 'l' at index 0 is the first unique char.")


def test_02_pedagogy_unique_in_middle():
    _assert_equal(first_unique_char("loveleetcode"), 2,
                  "In 'loveleetcode', 'v' at index 2 is the first unique char.")


def test_03_boundaries_no_unique_char():
    _assert_equal(first_unique_char("aabb"), -1,
                  "In 'aabb', no character is unique; should return -1.")


def test_04_boundaries_empty_string():
    _assert_equal(first_unique_char(""), -1,
                  "Empty string has no characters; should return -1.")


def test_05_boundaries_single_char():
    _assert_equal(first_unique_char("z"), 0,
                  "Single character is always unique at index 0.")


def test_06_interactions_all_unique():
    _assert_equal(first_unique_char("abcdef"), 0,
                  "When all chars are unique, the first one at index 0 should be returned.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: first char is unique", test_01_pedagogy_first_char_is_unique),
        ("pedagogy: unique in middle", test_02_pedagogy_unique_in_middle),
        ("boundaries: no unique char", test_03_boundaries_no_unique_char),
        ("boundaries: empty string", test_04_boundaries_empty_string),
        ("boundaries: single char", test_05_boundaries_single_char),
        ("interactions: all unique", test_06_interactions_all_unique),
    ]
    _run_all_tests(TEST_CASES)
