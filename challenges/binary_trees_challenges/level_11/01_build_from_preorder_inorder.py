# Level 11a - Build from preorder and inorder
# Implement build_from_preorder_inorder(preorder, inorder) reconstructing the unique tree.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 11a — Build from preorder and inorder
#
# Implement `build_from_preorder_inorder(preorder, inorder) -> Node | None`, reconstructing the unique tree with the given preorder and inorder traversals (two lists of the same distinct values). Return `None` for empty inputs.
#
# ```
# t = build_from_preorder_inorder([1, 2, 4, 5, 3], [4, 2, 5, 1, 3])
# level_order(t)   # [1, 2, 3, 4, 5]
# ```


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _level_order_values(root):
    if root is None:
        return []
    values = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        values.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return values


def build_from_preorder_inorder(preorder, inorder):
    raise NotImplementedError("Implement build_from_preorder_inorder(preorder, inorder).")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_inputs_return_none():
    _assert_true(build_from_preorder_inorder([], []) is None, "empty traversals should return None.")


def test_single_node_tree():
    root = build_from_preorder_inorder([7], [7])
    _assert_true(root is not None, "single value should build a node.")
    _assert_equal(root.value, 7, "single node should hold the only value.")
    _assert_true(root.left is None and root.right is None, "single node should have no children.")


def test_spec_example_level_order():
    root = build_from_preorder_inorder([1, 2, 4, 5, 3], [4, 2, 5, 1, 3])
    _assert_equal(_level_order_values(root), [1, 2, 3, 4, 5], "spec example should reconstruct shape.")


def test_right_skewed_tree_shape():
    root = build_from_preorder_inorder([1, 2, 3], [1, 2, 3])
    _assert_equal(_level_order_values(root), [1, 2, 3], "right chain should have values in order.")
    _assert_true(root.left is None, "right-skewed root should not have a left child.")
    _assert_true(root.right.right.value == 3, "right-skewed chain should continue to the right.")


def test_left_skewed_tree_shape():
    root = build_from_preorder_inorder([1, 2, 3], [3, 2, 1])
    _assert_equal(_level_order_values(root), [1, 2, 3], "left chain should have values in order.")
    _assert_true(root.right is None, "left-skewed root should not have a right child.")
    _assert_true(root.left.left.value == 3, "left-skewed chain should continue to the left.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty inputs return None", test_empty_inputs_return_none),
        ("single node tree", test_single_node_tree),
        ("spec example level order", test_spec_example_level_order),
        ("right-skewed tree shape", test_right_skewed_tree_shape),
        ("left-skewed tree shape", test_left_skewed_tree_shape),
    ]
    _run_all_tests(TEST_CASES)
