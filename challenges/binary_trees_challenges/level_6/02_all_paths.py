# Level 6b - All root-to-leaf paths
# Implement all_paths(root) returning each root-to-leaf path as a list of values.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 6b — All root-to-leaf paths
#
# Implement `all_paths(root) -> list[list]`. Each inner list is the values along one root-to-leaf path, in root-to-leaf order. The relative order of paths must be the order in which their leaves appear in a left-to-right preorder traversal. For an empty tree, return `[]`.
#
# ```
# all_paths(from_level_order([1, 2, 3, 4, 5]))
# # [[1, 2, 4], [1, 2, 5], [1, 3]]
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


def path_function(root, path, result):
    if not root:
        return
    path_function(root.left, path + [root.value], result)
    path_function(root.right, path + [root.value], result)
    if root.left is None and root.right is None:
        result.append(path + [root.value])


def all_paths(root):
    result = []
    path = []
    path_function(root, path, result)
    return result


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_has_no_paths():
    _assert_equal(all_paths(None), [], "empty tree should produce no paths.")


def test_single_node_path():
    _assert_equal(all_paths(Node(7)), [[7]], "single node is itself a path.")


def test_three_paths_in_preorder_leaf_order():
    tree = _make_level_order([1, 2, 3, 4, 5])
    _assert_equal(
        all_paths(tree),
        [[1, 2, 4], [1, 2, 5], [1, 3]],
        "paths should appear in left-to-right preorder leaf order.",
    )


def test_left_skew_one_path():
    tree = _make_level_order([1, 2, None, 3])
    _assert_equal(
        all_paths(tree), [[1, 2, 3]], "left-skewed tree should produce a single path."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree has no paths", test_empty_tree_has_no_paths),
        ("single node path", test_single_node_path),
        ("three paths in preorder leaf order", test_three_paths_in_preorder_leaf_order),
        ("left-skew one path", test_left_skew_one_path),
    ]
    _run_all_tests(TEST_CASES)
