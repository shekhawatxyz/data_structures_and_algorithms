# Level 1b - Build from level-order
# Implement from_level_order(values) to build a tree from a level-order list with None for gaps.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 1b — Build from level-order
#
# Implement `from_level_order(values)` that builds a binary tree from a level-order list where `None` denotes a missing node. Children of a `None` slot are not represented in the list at all. Return the root, or `None` if `values` is empty.
#
# ```
# from_level_order([1, 2, 3, None, 4, 5, None])
# #       1
# #      / \
# #     2   3
# #      \  /
# #       4 5
# ```

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def from_level_order(values):
    raise NotImplementedError("Implement from_level_order(values).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_list_returns_none():
    _assert_true(from_level_order([]) is None, "empty list should produce None.")


def test_single_node():
    root = from_level_order([7])
    _assert_equal(root.value, 7, "single-element list should produce a single root.")
    _assert_true(root.left is None and root.right is None,
                 "single-node tree should have no children.")


def test_full_three_node_tree():
    root = from_level_order([1, 2, 3])
    _assert_equal(root.value, 1, "root value should match.")
    _assert_equal(root.left.value, 2, "left child value should match.")
    _assert_equal(root.right.value, 3, "right child value should match.")


def test_with_none_gaps():
    root = from_level_order([1, 2, 3, None, 4, 5, None])
    _assert_equal(root.value, 1, "root value should match.")
    _assert_equal(root.left.value, 2, "left child value should match.")
    _assert_equal(root.right.value, 3, "right child value should match.")
    _assert_true(root.left.left is None, "left.left should be None per spec.")
    _assert_equal(root.left.right.value, 4, "left.right should be 4.")
    _assert_equal(root.right.left.value, 5, "right.left should be 5.")
    _assert_true(root.right.right is None, "right.right should be None per spec.")


def test_compressed_right_skewed_tree():
    root = from_level_order([1, None, 2, None, 3])
    _assert_equal(root.value, 1, "root value should match.")
    _assert_true(root.left is None, "root.left should be None.")
    _assert_equal(root.right.value, 2, "root.right should be 2.")
    _assert_true(root.right.left is None, "node 2 should have no left child.")
    _assert_equal(root.right.right.value, 3, "node 2 right child should be 3.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty list returns None", test_empty_list_returns_none),
        ("single node", test_single_node),
        ("full three node tree", test_full_three_node_tree),
        ("with None gaps", test_with_none_gaps),
        ("compressed right-skewed tree", test_compressed_right_skewed_tree),
    ]
    _run_all_tests(TEST_CASES)
