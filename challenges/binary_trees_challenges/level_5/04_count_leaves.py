# Level 5d - Count leaves
# Implement count_leaves(root) returning the number of leaf nodes.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 5d — Count leaves
#
# Implement `count_leaves(root) -> int`, the number of nodes with no children. The empty tree has `0` leaves; a single node is `1` leaf.


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


def count_leaves(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    return 0 + count_leaves(root.left) + count_leaves(root.right)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_has_zero_leaves():
    _assert_equal(count_leaves(None), 0, "empty tree should have 0 leaves.")


def test_single_node_is_one_leaf():
    _assert_equal(count_leaves(Node(7)), 1, "single node should be one leaf.")


def test_full_three_node_tree_has_two_leaves():
    _assert_equal(
        count_leaves(_make_level_order([1, 2, 3])),
        2,
        "two children of the root should both be leaves.",
    )


def test_uneven_tree_leaf_count():
    tree = _make_level_order([1, 2, 3, 4, None, 5, 6])
    _assert_equal(count_leaves(tree), 3, "leaves should be 4, 5, and 6.")


def test_skewed_tree_has_one_leaf():
    tree = _make_level_order([1, None, 2, None, 3])
    _assert_equal(count_leaves(tree), 1, "a chain has only its final node as a leaf.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree has zero leaves", test_empty_tree_has_zero_leaves),
        ("single node is one leaf", test_single_node_is_one_leaf),
        (
            "full three node tree has two leaves",
            test_full_three_node_tree_has_two_leaves,
        ),
        ("uneven tree leaf count", test_uneven_tree_leaf_count),
        ("skewed tree has one leaf", test_skewed_tree_has_one_leaf),
    ]
    _run_all_tests(TEST_CASES)
