# Level 3a - First n binary numbers
# Generate binary representations using a queue.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 3a — First n binary numbers
#
# ```python
# def binary_numbers(n: int) -> list[str]:
#     ...
# ```
#
# Return the binary representations (as strings) of the integers `1, 2, ..., n`, in order.
#
# ```
# binary_numbers(5)   # ["1", "10", "11", "100", "101"]
# ```
#
# The intended technique uses a queue. Don't just call `bin(i)` in a loop.

def binary_numbers(n):
    raise NotImplementedError("Implement binary_numbers(n).")

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
    _assert_equal(binary_numbers(5), ["1", "10", "11", "100", "101"],
                  "first five binary numbers should match the sample.")


def test_boundary_zero():
    _assert_equal(binary_numbers(0), [], "n=0 should return an empty list.")


def test_larger_prefix():
    expected = ["1", "10", "11", "100", "101", "110", "111", "1000"]
    _assert_equal(binary_numbers(8), expected, "binary sequence should stay ordered.")


def test_negative_raises():
    _assert_raises(ValueError, lambda: binary_numbers(-1), "negative n should raise ValueError.")


if __name__ == "__main__":
    TEST_CASES = [
        ("sample", test_sample),
        ("boundary zero", test_boundary_zero),
        ("larger prefix", test_larger_prefix),
        ("negative raises", test_negative_raises),
    ]
    _run_all_tests(TEST_CASES)
