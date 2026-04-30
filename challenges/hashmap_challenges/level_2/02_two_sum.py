# Level 2.2 - two_sum
# Find two indices whose values sum to the target.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 6. `two_sum`
#
# ```python
# def two_sum(nums: list[int], target: int) -> list[int]:
# ```
#
# Given a list of integers and a target, return the indices `[i, j]` (in any order, with `i != j`) of two numbers such that `nums[i] + nums[j] == target`. You may assume exactly one solution exists.
#
# Examples:
# - `two_sum([2, 7, 11, 15], 9)` → `[0, 1]`
# - `two_sum([3, 2, 4], 6)` → `[1, 2]`
# - `two_sum([3, 3], 6)` → `[0, 1]`

def two_sum(nums, target):
    raise NotImplementedError('Implement two_sum(nums, target).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_basic_case():
    result = two_sum([2, 7, 11, 15], 9)
    _assert_equal(sorted(result), [0, 1],
                  "2 + 7 = 9, indices [0, 1].")


def test_02_pedagogy_not_first_two():
    result = two_sum([3, 2, 4], 6)
    _assert_equal(sorted(result), [1, 2],
                  "2 + 4 = 6, indices [1, 2].")


def test_03_boundaries_duplicate_values():
    result = two_sum([3, 3], 6)
    _assert_equal(sorted(result), [0, 1],
                  "3 + 3 = 6, indices [0, 1].")


def test_04_boundaries_negative_numbers():
    result = two_sum([-1, -2, -3, -4, -5], -8)
    _assert_equal(sorted(result), [2, 4],
                  "-3 + -5 = -8, indices [2, 4].")


def test_05_interactions_large_list():
    nums = list(range(1, 101))
    result = two_sum(nums, 199)
    _assert_equal(sorted(result), [98, 99],
                  "99 + 100 = 199, indices [98, 99].")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic case", test_01_pedagogy_basic_case),
        ("pedagogy: not first two", test_02_pedagogy_not_first_two),
        ("boundaries: duplicate values", test_03_boundaries_duplicate_values),
        ("boundaries: negative numbers", test_04_boundaries_negative_numbers),
        ("interactions: large list", test_05_interactions_large_list),
    ]
    _run_all_tests(TEST_CASES)
