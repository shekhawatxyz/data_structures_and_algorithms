# Level 12a - Morris inorder
# Implement morris_inorder(root) using O(1) extra space besides the output list.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 12a — Morris inorder
#
# Implement `morris_inorder(root) -> list`, returning the inorder sequence (matching 2b) using **O(1) extra space**: no recursion, no explicit stack, queue, or set — only the output list. The tree must be unchanged when the call returns.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _make_level_order(values):
    if not values:
        return None
    root = Node(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    return root


def _preorder_with_nulls(root):
    if root is None:
        return ["#"]
    return [root.value] + _preorder_with_nulls(root.left) + _preorder_with_nulls(root.right)


def morris_inorder(root):
    raise NotImplementedError("Implement morris_inorder(root).")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree():
    _assert_equal(morris_inorder(None), [], "inorder of empty tree should be [].")


def test_single_node():
    _assert_equal(morris_inorder(Node(7)), [7], "single node inorder should be [value].")


def test_full_small_tree_matches_recursive_inorder():
    root = _make_level_order([1, 2, 3, 4, 5])
    _assert_equal(morris_inorder(root), [4, 2, 5, 1, 3], "Morris inorder should match recursive inorder.")


def test_right_skewed_tree():
    root = _make_level_order([1, None, 2, None, 3])
    _assert_equal(morris_inorder(root), [1, 2, 3], "right chain inorder should be top to bottom.")


def test_tree_is_restored_after_traversal():
    root = _make_level_order([1, 2, 3, 4, 5])
    before = _preorder_with_nulls(root)
    _assert_equal(morris_inorder(root), [4, 2, 5, 1, 3], "Morris traversal should produce inorder.")
    _assert_equal(_preorder_with_nulls(root), before, "tree structure should be restored after traversal.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree", test_empty_tree),
        ("single node", test_single_node),
        ("full small tree matches recursive inorder", test_full_small_tree_matches_recursive_inorder),
        ("right-skewed tree", test_right_skewed_tree),
        ("tree is restored after traversal", test_tree_is_restored_after_traversal),
    ]
    _run_all_tests(TEST_CASES)
