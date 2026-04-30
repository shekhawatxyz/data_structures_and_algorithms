# Level 3.3 - group_anagrams
# Group words that are anagrams of each other.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 10. `group_anagrams`
#
# ```python
# def group_anagrams(words: list[str]) -> list[list[str]]:
# ```
#
# Group words that are anagrams of each other. Return a list of groups. Within each group, words appear in the order they appeared in the input. The order of the groups themselves doesn't matter.
#
# Examples:
# - `group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])` → `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]` (groups in any order)
# - `group_anagrams([""])` → `[[""]]`
# - `group_anagrams(["a"])` → `[["a"]]`

def group_anagrams(words):
    raise NotImplementedError('Implement group_anagrams(words).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _sorted_groups(groups):
    return sorted([sorted(g) for g in groups])


def test_01_pedagogy_basic_grouping():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    _assert_equal(_sorted_groups(result),
                  _sorted_groups([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
                  "Should group anagrams together.")


def test_02_pedagogy_single_word():
    result = group_anagrams(["a"])
    _assert_equal(result, [["a"]],
                  "Single word should return one group with that word.")


def test_03_boundaries_empty_string():
    result = group_anagrams([""])
    _assert_equal(result, [[""]],
                  "Single empty string should return one group.")


def test_04_boundaries_no_anagrams():
    result = group_anagrams(["abc", "def", "ghi"])
    _assert_equal(_sorted_groups(result),
                  _sorted_groups([["abc"], ["def"], ["ghi"]]),
                  "No anagrams means each word is its own group.")


def test_05_interactions_all_anagrams():
    result = group_anagrams(["abc", "bca", "cab"])
    _assert_equal(len(result), 1,
                  "All anagrams of each other should produce one group.")
    _assert_equal(result[0], ["abc", "bca", "cab"],
                  "Group should preserve input order.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic grouping", test_01_pedagogy_basic_grouping),
        ("pedagogy: single word", test_02_pedagogy_single_word),
        ("boundaries: empty string", test_03_boundaries_empty_string),
        ("boundaries: no anagrams", test_04_boundaries_no_anagrams),
        ("interactions: all anagrams", test_05_interactions_all_anagrams),
    ]
    _run_all_tests(TEST_CASES)
