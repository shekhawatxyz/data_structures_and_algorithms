# Level 9b - Max sum subarray of length at most k
# Return the best non-empty contiguous sum with length at most k.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 9b — Max sum subarray of length at most k
#
# ```python
# def max_subarray_at_most_k(values: list[int], k: int) -> int:
#     ...
# ```
#
# Return the maximum sum over all non-empty contiguous subarrays of `values` whose length is at most `k`. Values may be negative. Total runtime should be O(n).
#
# ```
# max_subarray_at_most_k([1, -2, 3, -1, 2], 2)   # 3      (the subarray [3])
# max_subarray_at_most_k([1, -2, 3, -1, 2], 3)   # 4      ([3, -1, 2])
# max_subarray_at_most_k([-3, -1, -4, -1], 2)    # -1     ([-1])
# ```

def max_subarray_at_most_k(values, k):
    raise NotImplementedError("Implement max_subarray_at_most_k(values, k).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _assert_raises(expected_exception, callable_obj, context):
    try:
        callable_obj()
    except expected_exception:
        return
    except Exception as exc:
        raise AssertionError(
            f"{context} Expected {expected_exception.__name__}, "
            f"got {type(exc).__name__}: {exc}."
        ) from exc
    raise AssertionError(
        f"{context} Expected {expected_exception.__name__}, but none was raised."
    )


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
    for name, fn in test_cases:
        if _run_test(name, fn):
            passed += 1
    print(f"\nPassed {passed}/{len(test_cases)} tests.")
    if passed != len(test_cases):
        raise SystemExit(1)


def test_samples():
    values = [1, -2, 3, -1, 2]
    _assert_equal(max_subarray_at_most_k(values, 2), 3,
                  "best length-at-most-2 subarray should sum to 3.")
    _assert_equal(max_subarray_at_most_k(values, 3), 4,
                  "best length-at-most-3 subarray should sum to 4.")
    _assert_equal(max_subarray_at_most_k([-3, -1, -4, -1], 2), -1,
                  "all-negative input should still choose a non-empty subarray.")


def test_k_larger_than_length():
    _assert_equal(max_subarray_at_most_k([2, -1, 4], 10), 5,
                  "k larger than len(values) should allow the whole array.")


def test_invalid_input_raises():
    _assert_raises(ValueError, lambda: max_subarray_at_most_k([], 1),
                   "empty values should raise ValueError because subarray must be non-empty.")
    _assert_raises(ValueError, lambda: max_subarray_at_most_k([1], 0),
                   "non-positive k should raise ValueError.")


if __name__ == "__main__":
    TEST_CASES = [
        ("samples", test_samples),
        ("k larger than length", test_k_larger_than_length),
        ("invalid input raises", test_invalid_input_raises),
    ]
    _run_all_tests(TEST_CASES)
