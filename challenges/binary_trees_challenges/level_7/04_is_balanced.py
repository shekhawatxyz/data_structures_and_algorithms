# Level 7d - Is balanced
# Implement is_balanced(root) - True iff every node's subtree heights differ by at most 1.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 7d — Is balanced
#
# Implement `is_balanced(root) -> bool`: at every node, the heights of its two subtrees differ by at most 1. The empty tree is balanced. A naive solution recomputes heights and runs in O(n²); an O(n) solution returns height information as it goes — that one-pass idea returns in Level 9.
#
# ```
# is_balanced(from_level_order([1, 2, 3]))         # True
# is_balanced(from_level_order([1, 2, None, 3]))   # False
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


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root):
    if root is None:
        return True
    left, right = root.left, root.right
    left_height, right_height = height(left), height(right)
    if is_balanced(left) and is_balanced(right):
        return abs(left_height - right_height) <= 1
    return False


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_is_balanced():
    _assert_equal(is_balanced(None), True, "empty tree should be balanced.")


def test_single_node_is_balanced():
    _assert_equal(is_balanced(Node(7)), True, "single node should be balanced.")


def test_spec_balanced_tree():
    _assert_equal(
        is_balanced(_make_level_order([1, 2, 3])),
        True,
        "spec balanced tree should pass.",
    )


def test_spec_unbalanced_tree():
    tree = _make_level_order([1, 2, None, 3])
    _assert_equal(is_balanced(tree), False, "spec unbalanced tree should fail.")


def test_unbalanced_below_root():
    tree = _make_level_order([1, 2, 3, 4, None, None, None, 5])
    _assert_equal(is_balanced(tree), False, "imbalance can occur below the root.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree is balanced", test_empty_tree_is_balanced),
        ("single node is balanced", test_single_node_is_balanced),
        ("spec balanced tree", test_spec_balanced_tree),
        ("spec unbalanced tree", test_spec_unbalanced_tree),
        ("unbalanced below root", test_unbalanced_below_root),
    ]
    _run_all_tests(TEST_CASES)
