# Level 5b - Operation Counts
# Instrument insert to count rotations and recolorings per call.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 5b. Operation counts per insert
#
# Instrument your `insert` to count rotations performed and recolorings (color flips) per call. Insert n keys; record per-call counts. Compute the average and max. Both should look like `O(1)` amortized for rotations (insert does at most 2) and `O(log n)` worst case for recolorings.

RED = "R"
BLACK = "B"


class Node:
    def __init__(self, key, color=RED, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.nil = Node(key=None, color=BLACK)
        self.root = self.nil


def insert_with_counts(tree, key):
    raise NotImplementedError('Implement insert_with_counts(tree, key).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_first_insert_counts():
    tree = Tree()
    rotations, recolorings = insert_with_counts(tree, 10)
    _assert_true(isinstance(rotations, int), "Rotations should be an int.")
    _assert_true(isinstance(recolorings, int), "Recolorings should be an int.")
    # First insert: just color root black (1 recoloring), 0 rotations
    _assert_equal(rotations, 0, "First insert should need 0 rotations.")


def test_returns_tuple():
    tree = Tree()
    result = insert_with_counts(tree, 5)
    _assert_true(
        isinstance(result, tuple) and len(result) == 2,
        "insert_with_counts should return a 2-tuple.",
    )


def test_rotations_bounded_by_two():
    import random
    random.seed(99)
    tree = Tree()
    keys = random.sample(range(1, 200), 50)
    for k in keys:
        rotations, _ = insert_with_counts(tree, k)
        _assert_true(rotations <= 2, f"Rotations per insert should be at most 2, got {rotations}.")


def test_counts_accumulate_reasonably():
    tree = Tree()
    total_rotations = 0
    total_recolorings = 0
    for k in range(1, 21):
        r, c = insert_with_counts(tree, k)
        total_rotations += r
        total_recolorings += c
    _assert_true(total_rotations >= 0, "Total rotations should be non-negative.")
    _assert_true(total_recolorings >= 0, "Total recolorings should be non-negative.")


if __name__ == "__main__":
    TEST_CASES = [
        ("first insert counts", test_first_insert_counts),
        ("returns tuple", test_returns_tuple),
        ("rotations bounded by 2", test_rotations_bounded_by_two),
        ("counts accumulate reasonably", test_counts_accumulate_reasonably),
    ]
    _run_all_tests(TEST_CASES)
