# Level 9c - Shortest subarray with sum at least K
# Return the shortest contiguous length whose sum is at least k.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 9c — Shortest subarray with sum at least K
#
# ```python
# def shortest_subarray(values: list[int], k: int) -> int:
#     ...
# ```
#
# Return the length of the shortest contiguous subarray of `values` whose sum is at least `k`. If no such subarray exists, return `-1`. Values may be negative. Total runtime should be O(n).
#
# ```
# shortest_subarray([1], 1)                       # 1
# shortest_subarray([1, 2], 4)                    # -1
# shortest_subarray([2, -1, 2], 3)                # 3
# shortest_subarray([84, -37, 32, 40, 95], 167)   # 3
# ```

def shortest_subarray(values, k):
    raise NotImplementedError("Implement shortest_subarray(values, k).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    _assert_equal(shortest_subarray([1], 1), 1, "single item can satisfy k.")
    _assert_equal(shortest_subarray([1, 2], 4), -1, "return -1 when no subarray works.")
    _assert_equal(shortest_subarray([2, -1, 2], 3), 3,
                  "negative values can force a longer answer.")
    _assert_equal(shortest_subarray([84, -37, 32, 40, 95], 167), 3,
                  "sample with mixed signs should return 3.")


def test_short_window_after_negative_prefix():
    _assert_equal(shortest_subarray([17, 85, 93, -45, -21], 150), 2,
                  "algorithm should find the shortest valid later window.")


def test_empty_returns_minus_one():
    _assert_equal(shortest_subarray([], 1), -1,
                  "empty input has no valid non-empty subarray.")


if __name__ == "__main__":
    TEST_CASES = [
        ("samples", test_samples),
        ("short window after negative prefix", test_short_window_after_negative_prefix),
        ("empty returns minus one", test_empty_returns_minus_one),
    ]
    _run_all_tests(TEST_CASES)
