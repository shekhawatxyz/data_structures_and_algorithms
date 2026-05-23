# Level 12b - Boundary traversal
# Implement boundary_traversal(root) returning the anti-clockwise boundary.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 12b — Boundary traversal
#
# Implement `boundary_traversal(root) -> list`, the anti-clockwise boundary as a list of values:
#
# 1. The root.
# 2. The left boundary (excluding the root and excluding leaves), top to bottom.
# 3. All leaves, left to right.
# 4. The right boundary (excluding the root and excluding leaves), bottom to top.
#
# Each node appears exactly once.
#
# ```
# boundary_traversal(from_level_order([1, 2, 3, 4, 5, None, 6, None, None, 7, 8]))
# # [1, 2, 4, 7, 8, 6, 3]
# #         1
# #        / \
# #       2   3
# #      / \   \
# #     4   5   6
# #        / \
# #       7   8
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


def boundary_traversal(root):
    raise NotImplementedError("Implement boundary_traversal(root).")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    _assert_equal(boundary_traversal(None), [], "empty tree should have empty boundary.")


def test_single_node_appears_once():
    _assert_equal(boundary_traversal(Node(7)), [7], "single node should appear once.")


def test_spec_example():
    root = _make_level_order([1, 2, 3, 4, 5, None, 6, None, None, 7, 8])
    _assert_equal(boundary_traversal(root), [1, 2, 4, 7, 8, 6, 3], "spec example boundary.")


def test_full_tree_boundary():
    root = _make_level_order([1, 2, 3, 4, 5, 6, 7])
    _assert_equal(boundary_traversal(root), [1, 2, 4, 5, 6, 7, 3], "full tree boundary.")


def test_left_skewed_tree():
    root = _make_level_order([1, 2, None, 3])
    _assert_equal(boundary_traversal(root), [1, 2, 3], "left chain boundary should be top to bottom.")


def test_right_skewed_tree():
    root = _make_level_order([1, None, 2, None, 3])
    _assert_equal(boundary_traversal(root), [1, 3, 2], "right boundary should be appended bottom to top.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree", test_empty_tree),
        ("single node appears once", test_single_node_appears_once),
        ("spec example", test_spec_example),
        ("full tree boundary", test_full_tree_boundary),
        ("left-skewed tree", test_left_skewed_tree),
        ("right-skewed tree", test_right_skewed_tree),
    ]
    _run_all_tests(TEST_CASES)
