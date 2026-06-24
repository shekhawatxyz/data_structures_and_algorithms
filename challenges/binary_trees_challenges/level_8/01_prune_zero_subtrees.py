# Level 8a - Prune zero subtrees
# Implement prune_zero_subtrees(root) removing every all-zero subtree.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 8a — Prune zero subtrees
#
# Implement `prune_zero_subtrees(root) -> Node | None`. Remove every subtree all of whose nodes have value `0`. Return the (possibly `None`) modified root.
#
# ```
# prune_zero_subtrees(from_level_order([5, 0, 3, 0, 0]))
# # Before:        After:
# #     5              5
# #    / \              \
# #   0   3              3
# #  / \
# # 0   0
# ```


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


def prune_zero_subtrees(root):
    if root is None:
        return None
    root.left = prune_zero_subtrees(root.left)
    root.right = prune_zero_subtrees(root.right)
    if root.left is None and root.right is None and root.value == 0:
        root = None
    return root


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_stays_none():
    _assert_true(prune_zero_subtrees(None) is None, "empty tree should return None.")


def test_single_zero_node_is_pruned():
    _assert_true(
        prune_zero_subtrees(Node(0)) is None, "single zero node is an all-zero subtree."
    )


def test_single_nonzero_node_is_kept():
    root = Node(5)
    result = prune_zero_subtrees(root)
    _assert_true(result is root, "nonzero node should be kept.")
    _assert_equal(result.value, 5, "kept node should retain its value.")


def test_spec_example_prunes_left_subtree():
    tree = _make_level_order([5, 0, 3, 0, 0])
    result = prune_zero_subtrees(tree)
    _assert_equal(result.value, 5, "root should be kept.")
    _assert_true(result.left is None, "all-zero left subtree should be removed.")
    _assert_equal(result.right.value, 3, "nonzero right subtree should remain.")


def test_zero_node_with_nonzero_descendant_is_kept():
    tree = _make_level_order([1, 0, 0, None, 1])
    result = prune_zero_subtrees(tree)
    _assert_true(
        result.left is not None, "zero node with nonzero descendant should remain."
    )
    _assert_equal(result.left.right.value, 1, "nonzero descendant should remain.")
    _assert_true(result.right is None, "all-zero right child should be pruned.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree stays None", test_empty_tree_stays_none),
        ("single zero node is pruned", test_single_zero_node_is_pruned),
        ("single nonzero node is kept", test_single_nonzero_node_is_kept),
        ("spec example prunes left subtree", test_spec_example_prunes_left_subtree),
        (
            "zero node with nonzero descendant is kept",
            test_zero_node_with_nonzero_descendant_is_kept,
        ),
    ]
    _run_all_tests(TEST_CASES)
