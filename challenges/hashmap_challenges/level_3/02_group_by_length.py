# Level 3.2 - group_by_length
# Group words by their length.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 9. `group_by_length`
#
# ```python
# def group_by_length(words: list[str]) -> dict[int, list[str]]:
# ```
#
# Group words by their length. Return a dictionary mapping each length to the list of words of that length, preserving the order in which they appeared in the input.
#
# Examples:
# - `group_by_length(["hi", "world", "go", "is", "code"])` → `{2: ["hi", "go", "is"], 5: ["world"], 4: ["code"]}`
# - `group_by_length([])` → `{}`

def group_by_length(words):
    raise NotImplementedError('Implement group_by_length(words).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_mixed_lengths():
    result = group_by_length(["hi", "world", "go", "is", "code"])
    _assert_equal(result, {2: ["hi", "go", "is"], 5: ["world"], 4: ["code"]},
                  "Words should be grouped by length, preserving input order.")


def test_02_boundaries_empty_list():
    result = group_by_length([])
    _assert_equal(result, {}, "Empty list should return empty dict.")


def test_03_boundaries_all_same_length():
    result = group_by_length(["cat", "dog", "bat"])
    _assert_equal(result, {3: ["cat", "dog", "bat"]},
                  "All length-3 words go into one group.")


def test_04_interactions_includes_empty_string():
    result = group_by_length(["", "a", "bb", ""])
    _assert_equal(result, {0: ["", ""], 1: ["a"], 2: ["bb"]},
                  "Empty strings have length 0 and should be grouped together.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: mixed lengths", test_01_pedagogy_mixed_lengths),
        ("boundaries: empty list", test_02_boundaries_empty_list),
        ("boundaries: all same length", test_03_boundaries_all_same_length),
        ("interactions: includes empty string", test_04_interactions_includes_empty_string),
    ]
    _run_all_tests(TEST_CASES)
