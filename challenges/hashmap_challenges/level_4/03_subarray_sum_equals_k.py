# Level 4.3 - subarray_sum_equals_k
# Count contiguous subarrays summing to exactly k.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 13. `subarray_sum_equals_k`
#
# ```python
# def subarray_sum_equals_k(nums: list[int], k: int) -> int:
# ```
#
# Return the number of contiguous, non-empty subarrays of `nums` whose elements sum to exactly `k`. Elements may be negative.
#
# Examples:
# - `subarray_sum_equals_k([1, 1, 1], 2)` → `2`
# - `subarray_sum_equals_k([1, 2, 3], 3)` → `2`
# - `subarray_sum_equals_k([1, -1, 1, -1], 0)` → `4`

def subarray_sum_equals_k(nums, k):
    raise NotImplementedError('Implement subarray_sum_equals_k(nums, k).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    _assert_equal(subarray_sum_equals_k([1, 1, 1], 2), 2,
                  "[1,1] at indices 0-1 and 1-2 both sum to 2.")


def test_02_pedagogy_longer():
    _assert_equal(subarray_sum_equals_k([1, 2, 3], 3), 2,
                  "[1,2] and [3] both sum to 3.")


def test_03_boundaries_negatives():
    _assert_equal(subarray_sum_equals_k([1, -1, 1, -1], 0), 4,
                  "Subarrays [1,-1], [-1,1], [1,-1], and [1,-1,1,-1] sum to 0.")


def test_04_boundaries_single_element_match():
    _assert_equal(subarray_sum_equals_k([5], 5), 1,
                  "Single element matching k gives count 1.")


def test_05_boundaries_no_match():
    _assert_equal(subarray_sum_equals_k([1, 2, 3], 7), 0,
                  "No subarray sums to 7; should return 0.")


def test_06_interactions_all_zeros():
    _assert_equal(subarray_sum_equals_k([0, 0, 0], 0), 6,
                  "Every non-empty subarray of all zeros sums to 0: 6 total.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("pedagogy: longer", test_02_pedagogy_longer),
        ("boundaries: negatives", test_03_boundaries_negatives),
        ("boundaries: single element match", test_04_boundaries_single_element_match),
        ("boundaries: no match", test_05_boundaries_no_match),
        ("interactions: all zeros", test_06_interactions_all_zeros),
    ]
    _run_all_tests(TEST_CASES)
