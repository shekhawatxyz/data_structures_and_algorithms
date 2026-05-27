# Level 3c - Iterative postorder
# Implement postorder_iterative(root) using a stack instead of recursion.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 3c — Iterative postorder
#
# Implement `postorder_iterative(root) -> list`. The output must match `postorder` from 2c. Of the three iterative traversals this one demands the most care: the visit-order constraint means a node is not ready to be emitted at the moment you first reach it.


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


def postorder_iterative(root):
    result = []
    if root is None:
        return result
    stack = []
    stack.append([root, 0, 0])
    while stack:
        current = stack[-1]
        if current[1] == 0:
            if current[0].left:
                stack.append([current[0].left, 0, 0])
            current[1] = 1
        elif current[2] == 0:
            if current[0].right:
                stack.append([current[0].right, 0, 0])
            current[2] = 1
        else:
            to_add = stack.pop()
            result.append(to_add[0].value)
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
    _assert_equal(
        postorder_iterative(None), [], "iterative postorder of empty tree should be []."
    )


def test_single_node():
    _assert_equal(
        postorder_iterative(Node(7)),
        [7],
        "iterative postorder of single node should be [value].",
    )


def test_full_small_tree_matches_recursive_postorder():
    tree = _make_level_order([1, 2, 3, 4, 5])
    _assert_equal(
        postorder_iterative(tree),
        [4, 5, 2, 3, 1],
        "iterative postorder should visit left, right, then root.",
    )


def test_right_skewed_tree():
    tree = _make_level_order([1, None, 2, None, 3])
    _assert_equal(
        postorder_iterative(tree),
        [3, 2, 1],
        "iterative postorder should handle a right-skewed tree.",
    )


def test_uneven_tree():
    tree = _make_level_order([1, 2, 3, None, 4, 5])
    _assert_equal(
        postorder_iterative(tree),
        [4, 2, 5, 3, 1],
        "iterative postorder should preserve shape-sensitive ordering.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree", test_empty_tree),
        ("single node", test_single_node),
        (
            "full small tree matches recursive postorder",
            test_full_small_tree_matches_recursive_postorder,
        ),
        ("right-skewed tree", test_right_skewed_tree),
        ("uneven tree", test_uneven_tree),
    ]
    _run_all_tests(TEST_CASES)
