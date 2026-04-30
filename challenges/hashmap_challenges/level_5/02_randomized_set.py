# Level 5.2 - RandomizedSet
# Design a data structure with O(1) insert, remove, and get_random.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 16. `RandomizedSet`
#
# ```python
# class RandomizedSet:
#     def __init__(self): ...
#     def insert(self, val: int) -> bool: ...
#     def remove(self, val: int) -> bool: ...
#     def get_random(self) -> int: ...
# ```
#
# Design a data structure supporting all three operations in **O(1) average time**:
#
# - `insert(val)`: insert `val` if not already present; return `True` if newly inserted, else `False`.
# - `remove(val)`: remove `val` if present; return `True` if removed, else `False`.
# - `get_random()`: return a uniformly random element from the current set. You may assume the set is non-empty when this is called.
#
# You may use the `random` module. Alongside the dict you may use a list as auxiliary storage. The hard part is satisfying the O(1) constraint for *all three* operations — note that `list.remove(x)` and `del lst[i]` for non-final `i` are O(n) and so are forbidden by the constraint. `list.append(x)` and `list.pop()` (no index, popping the last element) are O(1) and are fine.
#
# Example:
# ```python
# rs = RandomizedSet()
# rs.insert(1)        # True
# rs.remove(2)        # False (2 not present)
# rs.insert(2)        # True
# rs.get_random()     # 1 or 2, each with probability 1/2
# rs.remove(1)        # True
# rs.insert(2)        # False (already present)
# rs.get_random()     # 2
# ```

import random


class RandomizedSet:
    def __init__(self):
        raise NotImplementedError('Implement RandomizedSet.__init__().')

    def insert(self, val):
        raise NotImplementedError('Implement RandomizedSet.insert(val).')

    def remove(self, val):
        raise NotImplementedError('Implement RandomizedSet.remove(val).')

    def get_random(self):
        raise NotImplementedError('Implement RandomizedSet.get_random().')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_insert_and_remove():
    rs = RandomizedSet()
    _assert_equal(rs.insert(1), True, "Insert 1 into empty set should return True.")
    _assert_equal(rs.remove(2), False, "Remove 2 (not present) should return False.")
    _assert_equal(rs.insert(2), True, "Insert 2 should return True.")


def test_02_pedagogy_duplicate_insert():
    rs = RandomizedSet()
    _assert_equal(rs.insert(1), True, "First insert of 1 returns True.")
    _assert_equal(rs.insert(1), False, "Duplicate insert of 1 returns False.")


def test_03_pedagogy_get_random_returns_valid_element():
    rs = RandomizedSet()
    rs.insert(10)
    rs.insert(20)
    rs.insert(30)
    result = rs.get_random()
    _assert_true(result in {10, 20, 30},
                 f"get_random() returned {result}, expected one of {{10, 20, 30}}.")


def test_04_boundaries_remove_then_get_random():
    rs = RandomizedSet()
    rs.insert(1)
    rs.insert(2)
    rs.remove(1)
    _assert_equal(rs.get_random(), 2, "After removing 1, only 2 remains.")


def test_05_interactions_insert_remove_insert():
    rs = RandomizedSet()
    rs.insert(5)
    _assert_equal(rs.remove(5), True, "Remove existing 5 returns True.")
    _assert_equal(rs.insert(5), True, "Re-inserting 5 after removal returns True.")
    _assert_equal(rs.get_random(), 5, "Only element is 5.")


def test_06_interactions_statistical_uniformity():
    rs = RandomizedSet()
    rs.insert(1)
    rs.insert(2)
    counts = {1: 0, 2: 0}
    for _ in range(1000):
        counts[rs.get_random()] += 1
    _assert_true(counts[1] > 300 and counts[2] > 300,
                 f"Distribution looks skewed: {counts}. Expected roughly 500/500.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: insert and remove", test_01_pedagogy_insert_and_remove),
        ("pedagogy: duplicate insert", test_02_pedagogy_duplicate_insert),
        ("pedagogy: get_random valid element", test_03_pedagogy_get_random_returns_valid_element),
        ("boundaries: remove then get_random", test_04_boundaries_remove_then_get_random),
        ("interactions: insert-remove-insert", test_05_interactions_insert_remove_insert),
        ("interactions: statistical uniformity", test_06_interactions_statistical_uniformity),
    ]
    _run_all_tests(TEST_CASES)
