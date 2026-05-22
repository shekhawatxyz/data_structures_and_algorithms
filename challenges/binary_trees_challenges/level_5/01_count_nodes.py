# Level 5a - Count nodes
# Implement count_nodes(root) returning the number of nodes in the tree.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 5a — Count nodes
#
# Implement `count_nodes(root) -> int`. The empty tree has `0` nodes.
from collections import deque


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


def count_nodes(root):
    counter = 0
    if root is None:
        return counter
    level_buffer = deque()
    level_buffer.append(root)
    while level_buffer:
        level_length = len(level_buffer)
        for i in range(level_length):
            val = level_buffer.popleft()
            counter += 1
            if val.left:
                level_buffer.append(val.left)
            if val.right:
                level_buffer.append(val.right)
    return counter


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_has_zero_nodes():
    _assert_equal(count_nodes(None), 0, "empty tree should have 0 nodes.")


def test_single_node_count():
    _assert_equal(count_nodes(Node(1)), 1, "single node should count as 1.")


def test_full_three_node_tree_count():
    _assert_equal(
        count_nodes(_make_level_order([1, 2, 3])),
        3,
        "three-node tree should have count 3.",
    )


def test_uneven_tree_count():
    _assert_equal(
        count_nodes(_make_level_order([1, 2, 3, None, 4, 5, None])),
        5,
        "tree with five nodes should have count 5 regardless of shape.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree has zero nodes", test_empty_tree_has_zero_nodes),
        ("single node count", test_single_node_count),
        ("full three node tree count", test_full_three_node_tree_count),
        ("uneven tree count", test_uneven_tree_count),
    ]
    _run_all_tests(TEST_CASES)
