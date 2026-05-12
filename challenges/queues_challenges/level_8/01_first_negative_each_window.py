# Level 8a - First negative in each window
# Return the first negative value in every window of size k.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 8a — First negative in each window
#
# ```python
# def first_negative_each_window(values: list[int], k: int) -> list[int]:
#     ...
# ```
#
# For each contiguous window of size `k` in `values`, return the first negative value in that window — that is, the negative value with the smallest index inside the window. If the window contains no negative value, output `0` for that window.
#
# ```
# first_negative_each_window([12, -1, -7, 8, -15, 30, 16, 28], 3)
# # [-1, -1, -7, -15, -15, 0]
# ```

def first_negative_each_window(values, k):
    raise NotImplementedError("Implement first_negative_each_window(values, k).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_sample():
    values = [12, -1, -7, 8, -15, 30, 16, 28]
    _assert_equal(first_negative_each_window(values, 3), [-1, -1, -7, -15, -15, 0],
                  "sample windows should match expected first negatives.")


def test_no_negatives_and_k_one():
    _assert_equal(first_negative_each_window([1, 2, 3], 2), [0, 0],
                  "windows with no negatives should output 0.")
    _assert_equal(first_negative_each_window([-1, 2, -3], 1), [-1, 0, -3],
                  "k=1 should inspect each value directly.")


def test_invalid_k_raises():
    _assert_raises(ValueError, lambda: first_negative_each_window([1, 2], 0),
                   "k=0 should raise ValueError.")
    _assert_raises(ValueError, lambda: first_negative_each_window([1, 2], 3),
                   "k larger than values length should raise ValueError.")


if __name__ == "__main__":
    TEST_CASES = [
        ("sample", test_sample),
        ("no negatives and k one", test_no_negatives_and_k_one),
        ("invalid k raises", test_invalid_k_raises),
    ]
    _run_all_tests(TEST_CASES)
