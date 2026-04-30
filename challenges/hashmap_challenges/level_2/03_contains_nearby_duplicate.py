# Level 2.3 - contains_nearby_duplicate
# Check if any duplicate exists within distance k.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 7. `contains_nearby_duplicate`
#
# ```python
# def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
# ```
#
# Return `True` if there exist two distinct indices `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`.
#
# Examples:
# - `contains_nearby_duplicate([1, 2, 3, 1], 3)` → `True`
# - `contains_nearby_duplicate([1, 0, 1, 1], 1)` → `True`
# - `contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)` → `False`

def contains_nearby_duplicate(nums, k):
    raise NotImplementedError('Implement contains_nearby_duplicate(nums, k).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_duplicate_within_k():
    _assert_equal(contains_nearby_duplicate([1, 2, 3, 1], 3), True,
                  "1 at index 0 and 3, distance 3 <= k=3.")


def test_02_pedagogy_adjacent_duplicate():
    _assert_equal(contains_nearby_duplicate([1, 0, 1, 1], 1), True,
                  "1 at index 2 and 3, distance 1 <= k=1.")


def test_03_boundaries_duplicate_beyond_k():
    _assert_equal(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2), False,
                  "Nearest duplicates are distance 3, which exceeds k=2.")


def test_04_boundaries_no_duplicates():
    _assert_equal(contains_nearby_duplicate([1, 2, 3, 4], 3), False,
                  "No duplicates at all means False.")


def test_05_boundaries_empty_and_single():
    _assert_equal(contains_nearby_duplicate([], 1), False,
                  "Empty list has no duplicates.")
    _assert_equal(contains_nearby_duplicate([1], 1), False,
                  "Single element has no duplicates.")


def test_06_interactions_k_zero():
    _assert_equal(contains_nearby_duplicate([1, 1, 1], 0), False,
                  "k=0 means same index required, which is impossible for distinct indices.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: duplicate within k", test_01_pedagogy_duplicate_within_k),
        ("pedagogy: adjacent duplicate", test_02_pedagogy_adjacent_duplicate),
        ("boundaries: duplicate beyond k", test_03_boundaries_duplicate_beyond_k),
        ("boundaries: no duplicates", test_04_boundaries_no_duplicates),
        ("boundaries: empty and single", test_05_boundaries_empty_and_single),
        ("interactions: k zero", test_06_interactions_k_zero),
    ]
    _run_all_tests(TEST_CASES)
