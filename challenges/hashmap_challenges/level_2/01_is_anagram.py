# Level 2.1 - is_anagram
# Check if two strings are anagrams of each other.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 5. `is_anagram`
#
# ```python
# def is_anagram(s: str, t: str) -> bool:
# ```
#
# Return `True` if `t` contains exactly the same characters as `s` with the same frequencies, regardless of order.
#
# Examples:
# - `is_anagram("listen", "silent")` → `True`
# - `is_anagram("hello", "world")` → `False`
# - `is_anagram("a", "ab")` → `False`
# - `is_anagram("", "")` → `True`

def is_anagram(s, t):
    raise NotImplementedError('Implement is_anagram(s, t).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_valid_anagram():
    _assert_equal(is_anagram("listen", "silent"), True,
                  "'listen' and 'silent' are anagrams.")


def test_02_pedagogy_not_anagram():
    _assert_equal(is_anagram("hello", "world"), False,
                  "'hello' and 'world' are not anagrams.")


def test_03_boundaries_different_lengths():
    _assert_equal(is_anagram("a", "ab"), False,
                  "Different length strings cannot be anagrams.")


def test_04_boundaries_both_empty():
    _assert_equal(is_anagram("", ""), True,
                  "Two empty strings are anagrams of each other.")


def test_05_interactions_same_chars_different_freq():
    _assert_equal(is_anagram("aab", "abb"), False,
                  "Same characters but different frequencies are not anagrams.")


def test_06_interactions_single_char():
    _assert_equal(is_anagram("a", "a"), True,
                  "Single identical characters are anagrams.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: valid anagram", test_01_pedagogy_valid_anagram),
        ("pedagogy: not anagram", test_02_pedagogy_not_anagram),
        ("boundaries: different lengths", test_03_boundaries_different_lengths),
        ("boundaries: both empty", test_04_boundaries_both_empty),
        ("interactions: same chars different freq", test_05_interactions_same_chars_different_freq),
        ("interactions: single char", test_06_interactions_single_char),
    ]
    _run_all_tests(TEST_CASES)
