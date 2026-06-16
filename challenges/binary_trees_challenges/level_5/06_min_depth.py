# Level 5f - Min depth
# Implement min_depth(root) returning the shortest root-to-leaf path length in edges.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 5f — Min depth
#
# Implement `min_depth(root) -> int`, the number of edges on the shortest path from the root to *any leaf*. Empty: `-1`. Single node: `0`. Mind the case where a node has only one child:
#
# ```
# min_depth(from_level_order([1, None, 2, None, 3]))   # 2
# #   1
# #    \
# #     2
# #      \
# #       3
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


def min_depth(root):
    if root is None:
        return -1
    if not root.left and not root.right:
        return 0
    if root.left:
        if root.right:
            return 1 + min(min_depth(root.left), min_depth(root.right))
        else:
            return 1 + min_depth(root.left)
    if root.right:
        return 1 + min_depth(root.right)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_min_depth_is_minus_one():
    _assert_equal(min_depth(None), -1, "empty tree should have min depth -1.")


def test_single_node_min_depth_is_zero():
    _assert_equal(min_depth(Node(7)), 0, "single node should have min depth 0.")


def test_balanced_three_node_tree():
    _assert_equal(
        min_depth(_make_level_order([1, 2, 3])), 1, "nearest leaf is one edge away."
    )


def test_spec_right_chain():
    tree = _make_level_order([1, None, 2, None, 3])
    _assert_equal(min_depth(tree), 2, "one-child nodes must not be treated as leaves.")


def test_shorter_leaf_on_one_side():
    tree = _make_level_order([1, 2, 3, None, None, 4, None, 5])
    _assert_equal(min_depth(tree), 1, "the left child is the nearest leaf.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree min depth is -1", test_empty_tree_min_depth_is_minus_one),
        ("single node min depth is 0", test_single_node_min_depth_is_zero),
        ("balanced three node tree", test_balanced_three_node_tree),
        ("spec right chain", test_spec_right_chain),
        ("shorter leaf on one side", test_shorter_leaf_on_one_side),
    ]
    _run_all_tests(TEST_CASES)
