# Level 1.4 - most_frequent_element
# Return the most frequently occurring element, with earliest-first tie-breaking.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 4. `most_frequent_element`
#
# ```python
# def most_frequent_element(nums: list[int]) -> int:
# ```
#
# Return the element of `nums` that appears most often. If there is a tie, return the one whose first occurrence is earliest in `nums`. The list is non-empty.
#
# Examples:
# - `most_frequent_element([1, 2, 2, 3, 3, 3])` → `3`
# - `most_frequent_element([4, 4, 1, 1])` → `4`
# - `most_frequent_element([7])` → `7`

def most_frequent_element(nums):
    raise NotImplementedError('Implement most_frequent_element(nums).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_clear_winner():
    _assert_equal(most_frequent_element([1, 2, 2, 3, 3, 3]), 3,
                  "3 appears most often (3 times).")


def test_02_pedagogy_tie_breaks_by_first_occurrence():
    _assert_equal(most_frequent_element([4, 4, 1, 1]), 4,
                  "4 and 1 tie at 2 each; 4 appears first.")


def test_03_boundaries_single_element():
    _assert_equal(most_frequent_element([7]), 7,
                  "Single element list should return that element.")


def test_04_boundaries_all_same():
    _assert_equal(most_frequent_element([5, 5, 5, 5]), 5,
                  "All same elements should return that element.")


def test_05_interactions_three_way_tie():
    _assert_equal(most_frequent_element([3, 2, 1, 3, 2, 1]), 3,
                  "Three-way tie; 3 appears first at index 0.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: clear winner", test_01_pedagogy_clear_winner),
        ("pedagogy: tie-break by first occurrence", test_02_pedagogy_tie_breaks_by_first_occurrence),
        ("boundaries: single element", test_03_boundaries_single_element),
        ("boundaries: all same", test_04_boundaries_all_same),
        ("interactions: three-way tie", test_05_interactions_three_way_tie),
    ]
    _run_all_tests(TEST_CASES)
