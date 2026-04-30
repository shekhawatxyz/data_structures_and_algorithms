# Level 4.2 - longest_substring_without_repeating
# Find the length of the longest substring with no repeated characters.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 12. `longest_substring_without_repeating`
#
# ```python
# def longest_substring_without_repeating(s: str) -> int:
# ```
#
# Return the length of the longest substring of `s` that contains no repeated characters.
#
# Examples:
# - `longest_substring_without_repeating("abcabcbb")` → `3`
# - `longest_substring_without_repeating("bbbbb")` → `1`
# - `longest_substring_without_repeating("pwwkew")` → `3`
# - `longest_substring_without_repeating("")` → `0`

def longest_substring_without_repeating(s):
    raise NotImplementedError('Implement longest_substring_without_repeating(s).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_basic():
    _assert_equal(longest_substring_without_repeating("abcabcbb"), 3,
                  "'abc' is the longest substring without repeats, length 3.")


def test_02_pedagogy_all_same():
    _assert_equal(longest_substring_without_repeating("bbbbb"), 1,
                  "All same chars; longest unique substring is length 1.")


def test_03_pedagogy_middle_window():
    _assert_equal(longest_substring_without_repeating("pwwkew"), 3,
                  "'wke' is the longest substring without repeats, length 3.")


def test_04_boundaries_empty():
    _assert_equal(longest_substring_without_repeating(""), 0,
                  "Empty string has no substring; return 0.")


def test_05_boundaries_all_unique():
    _assert_equal(longest_substring_without_repeating("abcdef"), 6,
                  "All unique chars; whole string is the answer.")


def test_06_interactions_single_char():
    _assert_equal(longest_substring_without_repeating("a"), 1,
                  "Single character string has length 1.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("pedagogy: all same", test_02_pedagogy_all_same),
        ("pedagogy: middle window", test_03_pedagogy_middle_window),
        ("boundaries: empty", test_04_boundaries_empty),
        ("boundaries: all unique", test_05_boundaries_all_unique),
        ("interactions: single char", test_06_interactions_single_char),
    ]
    _run_all_tests(TEST_CASES)
