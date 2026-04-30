# Level 4.4 - longest_subarray_with_sum_k
# Find the length of the longest contiguous subarray summing to k.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 14. `longest_subarray_with_sum_k`
#
# ```python
# def longest_subarray_with_sum_k(nums: list[int], k: int) -> int:
# ```
#
# Return the length of the longest contiguous, non-empty subarray of `nums` summing to exactly `k`. If no such subarray exists, return `0`. Elements may be negative.
#
# Examples:
# - `longest_subarray_with_sum_k([1, -1, 5, -2, 3], 3)` → `4`
# - `longest_subarray_with_sum_k([-2, -1, 2, 1], 1)` → `2`
# - `longest_subarray_with_sum_k([1, 2, 3], 7)` → `0`

def longest_subarray_with_sum_k(nums, k):
    raise NotImplementedError('Implement longest_subarray_with_sum_k(nums, k).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    _assert_equal(longest_subarray_with_sum_k([1, -1, 5, -2, 3], 3), 4,
                  "[1,-1,5,-2] sums to 3 with length 4.")


def test_02_pedagogy_shorter():
    _assert_equal(longest_subarray_with_sum_k([-2, -1, 2, 1], 1), 2,
                  "[2,-1] or [-1,2] both sum to 1 with length 2.")


def test_03_boundaries_no_match():
    _assert_equal(longest_subarray_with_sum_k([1, 2, 3], 7), 0,
                  "No subarray sums to 7; return 0.")


def test_04_boundaries_single_element():
    _assert_equal(longest_subarray_with_sum_k([5], 5), 1,
                  "Single element matching k; length is 1.")


def test_05_interactions_entire_array():
    _assert_equal(longest_subarray_with_sum_k([1, 2, 3], 6), 3,
                  "Entire array sums to k; length is 3.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("pedagogy: shorter", test_02_pedagogy_shorter),
        ("boundaries: no match", test_03_boundaries_no_match),
        ("boundaries: single element", test_04_boundaries_single_element),
        ("interactions: entire array", test_05_interactions_entire_array),
    ]
    _run_all_tests(TEST_CASES)
