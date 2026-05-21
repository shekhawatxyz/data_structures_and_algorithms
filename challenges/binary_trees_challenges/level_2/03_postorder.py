# Level 2c - Postorder traversal
# Implement postorder(root) returning values in postorder (left, right, root).

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 2c — Postorder
#
# Implement `postorder(root) -> list` that returns the values in postorder (left, right, root). For an empty tree, return `[]`.
#
# ```
# postorder(from_level_order([1, 2, 3, 4, 5]))  # [4, 5, 2, 3, 1]
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


def postorder(root):
    result = []
    _postorder(root, result)
    return result


def _postorder(node, acc):
    if node is None:
        return
    _postorder(node.left, acc)
    _postorder(node.right, acc)
    acc.append(node.value)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    _assert_equal(postorder(None), [], "postorder of empty tree should be [].")


def test_single_node():
    _assert_equal(
        postorder(Node(7)), [7], "postorder of single node should be [value]."
    )


def test_full_small_tree():
    tree = _make_level_order([1, 2, 3, 4, 5])
    _assert_equal(
        postorder(tree),
        [4, 5, 2, 3, 1],
        "postorder visits left subtree, right subtree, then root.",
    )


def test_right_skewed_tree():
    tree = _make_level_order([1, None, 2, None, 3])
    _assert_equal(
        postorder(tree), [3, 2, 1], "postorder reaches deepest right descendant first."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree", test_empty_tree),
        ("single node", test_single_node),
        ("full small tree", test_full_small_tree),
        ("right-skewed tree", test_right_skewed_tree),
    ]
    _run_all_tests(TEST_CASES)
