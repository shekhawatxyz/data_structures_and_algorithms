# Level 9b - Diameter
# Implement diameter(root) - longest path (in edges) between any two nodes.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 9b — Diameter
#
# Implement `diameter(root) -> int`. The diameter is the number of edges on the longest path between any two nodes in the tree. The diameter of an empty or single-node tree is `0`. Total runtime should be O(n).
#
# ```
# diameter(from_level_order([1, 2, 3, 4, 5]))   # 3
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


def diameter(root):
    raise NotImplementedError("Implement diameter(root).")

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


def test_empty_tree_diameter_is_zero():
    _assert_equal(diameter(None), 0, "empty tree should have diameter 0.")


def test_single_node_diameter_is_zero():
    _assert_equal(diameter(Node(7)), 0, "single node should have diameter 0.")


def test_spec_example_diameter():
    _assert_equal(diameter(_make_level_order([1, 2, 3, 4, 5])), 3,
                  "spec example tree should have diameter 3.")


def test_diameter_through_root():
    # Path 4 -> 2 -> 1 -> 3 -> 6: 4 edges
    tree = _make_level_order([1, 2, 3, 4, None, None, 6])
    _assert_equal(diameter(tree), 4,
                  "diameter should pass through the root when both subtrees extend.")


def test_diameter_off_root():
    # Tree: longest path lives entirely in the left subtree, not crossing root.
    # 1 -> 2 -> 4 -> 6 -> 8 (and 4 -> 7 -> 9 branch off):
    # Build by hand to control shape.
    n8 = Node(8)
    n6 = Node(6, left=n8)
    n4 = Node(4, left=n6, right=Node(7, left=Node(9)))
    n2 = Node(2, left=n4)
    root = Node(1, left=n2, right=Node(3))
    # Longest path inside the left subtree: 8 - 6 - 4 - 7 - 9 = 4 edges.
    _assert_equal(diameter(root), 4,
                  "longest path may live entirely off the root.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree diameter is 0", test_empty_tree_diameter_is_zero),
        ("single node diameter is 0", test_single_node_diameter_is_zero),
        ("spec example diameter", test_spec_example_diameter),
        ("diameter through root", test_diameter_through_root),
        ("diameter off root", test_diameter_off_root),
    ]
    _run_all_tests(TEST_CASES)
