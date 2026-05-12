# Level 2b - Round-robin elimination
# Return the final survivor after repeatedly eliminating every kth person.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 2b — Round-robin elimination
#
# ```python
# def eliminate(names: list[str], k: int) -> str:
#     ...
# ```
#
# People stand in a circle in the given order. Starting from the first, you skip `k - 1` people and eliminate the `k`-th. You then continue from the next person, skipping `k - 1` and eliminating the next `k`-th. Repeat until one person remains. Return that person.
#
# ```
# eliminate(["A", "B", "C", "D", "E"], 3)  # "D"
# eliminate(["A", "B", "C"], 1)            # "C"
# ```

def eliminate(names, k):
    raise NotImplementedError("Implement eliminate(names, k).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    _assert_equal(eliminate(["A", "B", "C", "D", "E"], 3), "D",
                  "sample with k=3 should leave D.")
    _assert_equal(eliminate(["A", "B", "C"], 1), "C",
                  "k=1 should eliminate from front until the last original name.")


def test_single_person():
    _assert_equal(eliminate(["Only"], 5), "Only",
                  "single participant should survive regardless of k.")


def test_invalid_input_raises():
    _assert_raises(ValueError, lambda: eliminate([], 2), "empty names should raise ValueError.")
    _assert_raises(ValueError, lambda: eliminate(["A"], 0), "non-positive k should raise ValueError.")


if __name__ == "__main__":
    TEST_CASES = [
        ("samples", test_samples),
        ("single person", test_single_person),
        ("invalid input raises", test_invalid_input_raises),
    ]
    _run_all_tests(TEST_CASES)
