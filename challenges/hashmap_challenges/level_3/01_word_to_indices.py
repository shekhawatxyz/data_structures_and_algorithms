# Level 3.1 - word_to_indices
# Map each word to the list of indices where it appears.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 8. `word_to_indices`
#
# ```python
# def word_to_indices(words: list[str]) -> dict[str, list[int]]:
# ```
#
# Given a list of words, return a dictionary mapping each distinct word to the list of indices (in ascending order) at which it appears.
#
# Examples:
# - `word_to_indices(["cat", "dog", "cat", "bird", "dog", "cat"])` → `{"cat": [0, 2, 5], "dog": [1, 4], "bird": [3]}`
# - `word_to_indices([])` → `{}`
# - `word_to_indices(["x"])` → `{"x": [0]}`

def word_to_indices(words):
    raise NotImplementedError('Implement word_to_indices(words).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_repeated_words():
    result = word_to_indices(["cat", "dog", "cat", "bird", "dog", "cat"])
    _assert_equal(result, {"cat": [0, 2, 5], "dog": [1, 4], "bird": [3]},
                  "Each word should map to its list of indices.")


def test_02_pedagogy_single_word():
    result = word_to_indices(["x"])
    _assert_equal(result, {"x": [0]},
                  "Single word should map to index [0].")


def test_03_boundaries_empty_list():
    result = word_to_indices([])
    _assert_equal(result, {}, "Empty list should return empty dict.")


def test_04_boundaries_all_unique():
    result = word_to_indices(["a", "b", "c"])
    _assert_equal(result, {"a": [0], "b": [1], "c": [2]},
                  "All unique words each get a single-element index list.")


def test_05_interactions_all_same():
    result = word_to_indices(["hi", "hi", "hi"])
    _assert_equal(result, {"hi": [0, 1, 2]},
                  "All same words should produce one key with all indices.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: repeated words", test_01_pedagogy_repeated_words),
        ("pedagogy: single word", test_02_pedagogy_single_word),
        ("boundaries: empty list", test_03_boundaries_empty_list),
        ("boundaries: all unique", test_04_boundaries_all_unique),
        ("interactions: all same", test_05_interactions_all_same),
    ]
    _run_all_tests(TEST_CASES)
