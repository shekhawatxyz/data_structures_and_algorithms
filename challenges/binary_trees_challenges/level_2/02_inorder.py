# Level 2b - Inorder traversal
# Implement inorder(root) returning values in inorder (left, root, right).

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 2b — Inorder
#
# Implement `inorder(root) -> list` that returns the values in inorder (left, root, right). For an empty tree, return `[]`.
#
# ```
# inorder(from_level_order([1, 2, 3, 4, 5]))    # [4, 2, 5, 1, 3]
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


def inorder(root):
    result = []
    _inorder(root, result)
    return result


def _inorder(node, acc):
    if node is None:
        return
    _inorder(node.left, acc)
    acc.append(node.value)
    _inorder(node.right, acc)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    _assert_equal(inorder(None), [], "inorder of empty tree should be [].")


def test_single_node():
    _assert_equal(inorder(Node(7)), [7], "inorder of single node should be [value].")


def test_full_small_tree():
    tree = _make_level_order([1, 2, 3, 4, 5])
    _assert_equal(
        inorder(tree),
        [4, 2, 5, 1, 3],
        "inorder visits left subtree, root, right subtree.",
    )


def test_bst_inorder_is_sorted():
    tree = _make_level_order([4, 2, 6, 1, 3, 5, 7])
    _assert_equal(
        inorder(tree), [1, 2, 3, 4, 5, 6, 7], "inorder over a BST yields sorted values."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree", test_empty_tree),
        ("single node", test_single_node),
        ("full small tree", test_full_small_tree),
        ("BST inorder is sorted", test_bst_inorder_is_sorted),
    ]
    _run_all_tests(TEST_CASES)
