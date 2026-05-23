# Level 9b - Lowest common ancestor
# Implement lowest_common_ancestor(root, a, b) returning the deepest shared ancestor.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 9b — Lowest common ancestor
#
# Implement `lowest_common_ancestor(root, a, b) -> Node | None`, where `a` and `b` are `Node` references known to be present in the tree rooted at `root`. Return the deepest node that is an ancestor of both `a` and `b`. A node is its own ancestor. Return `None` only if `root` is `None`.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _make_level_order_with_index(values):
    """Build the tree and return (root, list_of_nodes_indexed_by_levelorder_position)."""
    if not values:
        return None, []
    root = Node(values[0])
    nodes: "list[Node | None]" = [root]
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            nodes.append(node.left)
            queue.append(node.left)
        else:
            nodes.append(None)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            nodes.append(node.right)
            queue.append(node.right)
        else:
            nodes.append(None)
        i += 1
    while len(nodes) < len(values):
        nodes.append(None)
    return root, nodes


def lowest_common_ancestor(root, a, b) -> "Node | None":
    raise NotImplementedError("Implement lowest_common_ancestor(root, a, b).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_returns_none():
    _assert_true(lowest_common_ancestor(None, Node(1), Node(2)) is None,
                 "empty tree should return None.")


def test_lca_in_separate_subtrees():
    root, nodes = _make_level_order_with_index([1, 2, 3, 4, 5, 6, 7])
    a = nodes[3]  # value 4
    b = nodes[6]  # value 7
    result = lowest_common_ancestor(root, a, b)
    _assert_true(result is root, "LCA of 4 and 7 should be the root node.")


def test_lca_in_same_subtree():
    root, nodes = _make_level_order_with_index([1, 2, 3, 4, 5])
    a = nodes[3]  # value 4
    b = nodes[4]  # value 5
    result = lowest_common_ancestor(root, a, b)
    _assert_true(result is nodes[1], "LCA of 4 and 5 should be the node with value 2.")


def test_node_is_its_own_ancestor():
    root, nodes = _make_level_order_with_index([1, 2, 3, 4, 5])
    a = nodes[1]  # value 2
    b = nodes[3]  # value 4 (descendant of 2)
    result = lowest_common_ancestor(root, a, b)
    _assert_true(result is a, "ancestor and descendant should yield the ancestor node.")


def test_same_node_twice():
    root, nodes = _make_level_order_with_index([1, 2, 3])
    a = nodes[2]  # value 3
    result = lowest_common_ancestor(root, a, a)
    _assert_true(result is a, "LCA of a node with itself should be that exact node.")


def test_duplicate_values_use_node_identity():
    root = Node(1, Node(2), Node(2))
    result = lowest_common_ancestor(root, root.left, root.right)
    _assert_true(result is root, "duplicate values should not confuse node identity.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree returns None", test_empty_tree_returns_none),
        ("LCA in separate subtrees", test_lca_in_separate_subtrees),
        ("LCA in same subtree", test_lca_in_same_subtree),
        ("node is its own ancestor", test_node_is_its_own_ancestor),
        ("same node twice", test_same_node_twice),
        ("duplicate values use node identity", test_duplicate_values_use_node_identity),
    ]
    _run_all_tests(TEST_CASES)
