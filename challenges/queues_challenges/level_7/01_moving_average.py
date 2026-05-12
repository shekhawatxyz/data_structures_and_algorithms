# Level 7a - Moving average
# Maintain the average of a fixed-size sliding window.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 7a — Moving average
#
# Implement a `MovingAverage` class:
#
# - `MovingAverage(k: int)` — fixed window size `k >= 1`
# - `next(x: float) -> float` — admit `x` into the window and return the average of the values currently in the window
#
# Until `k` values have been seen, the window contains all values seen so far.
#
# ```
# ma = MovingAverage(3)
# ma.next(1)    # 1.0
# ma.next(10)   # 5.5
# ma.next(3)    # 4.666...
# ma.next(5)    # 6.0     (window is now [10, 3, 5])
# ```

class MovingAverage:
    def __init__(self, k):
        raise NotImplementedError("Implement MovingAverage.__init__(k).")

    def next(self, x):
        raise NotImplementedError("Implement MovingAverage.next(x).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


def _assert_close(actual, expected, context, tolerance=1e-9):
    if abs(actual - expected) > tolerance:
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


def test_sample_sequence():
    ma = MovingAverage(3)
    _assert_close(ma.next(1), 1.0, "first average should use one value.")
    _assert_close(ma.next(10), 5.5, "second average should use two values.")
    _assert_close(ma.next(3), 14 / 3, "third average should use full window.")
    _assert_close(ma.next(5), 6.0, "fourth average should drop oldest value.")


def test_window_size_one():
    ma = MovingAverage(1)
    _assert_close(ma.next(5), 5.0, "k=1 should return the latest value.")
    _assert_close(ma.next(-2), -2.0, "k=1 should replace the whole window.")


def test_invalid_window_raises():
    _assert_raises(ValueError, lambda: MovingAverage(0), "k=0 should raise ValueError.")
    _assert_raises(ValueError, lambda: MovingAverage(-1), "negative k should raise ValueError.")


if __name__ == "__main__":
    TEST_CASES = [
        ("sample sequence", test_sample_sequence),
        ("window size one", test_window_size_one),
        ("invalid window raises", test_invalid_window_raises),
    ]
    _run_all_tests(TEST_CASES)
