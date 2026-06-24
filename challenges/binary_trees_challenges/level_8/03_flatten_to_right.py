# Level 8c - Flatten to the right
# Implement flatten_to_right(root) rearranging the tree into a preorder right chain.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 8c — Flatten to the right
#
# Implement `flatten_to_right(root) -> None`. Rearrange the tree in place into a right-leaning chain (every `left` is `None`) whose values, read down the `right` pointers, are the tree's preorder sequence.
#
# ```
# flatten_to_right(from_level_order([1, 2, 5, 3, 4, None, 6]))
# # Before:          After:  1
# #     1                     \
# #    / \                     2
# #   2   5                     \
# #  / \   \                     3
# # 3   4   6                     \
# #                                4
# #                                 \
# #                                  5
# #                                   \
# #                                    6
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


def _right_chain_values(root):
    values = []
    node = root
    while node is not None:
        if node.left is not None:
            raise AssertionError("flattened tree should not have left children.")
        values.append(node.value)
        node = node.right
    return values


def _flatten(root):
    if root is None or (root.right is None and root.left is None):
        return root
    if root.left is None:
        return _flatten(root.right)
    rr = root.right
    left = _flatten(root.left)
    right = _flatten(root.right)
    root.right = root.left
    left.right = rr
    root.left = None
    return right if right else left


def flatten_to_right(root):
    _flatten(root)
    return None


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_is_noop():
    _assert_equal(flatten_to_right(None), None, "empty tree should be a no-op.")


def test_single_node_stays_single_chain():
    root = Node(7)
    flatten_to_right(root)
    _assert_equal(
        _right_chain_values(root), [7], "single node should remain a one-node chain."
    )


def test_spec_example_preorder_chain():
    root = _make_level_order([1, 2, 5, 3, 4, None, 6])
    flatten_to_right(root)
    _assert_equal(
        _right_chain_values(root), [1, 2, 3, 4, 5, 6], "chain should follow preorder."
    )


def test_left_skewed_tree():
    root = _make_level_order([1, 2, None, 3])
    flatten_to_right(root)
    _assert_equal(
        _right_chain_values(root), [1, 2, 3], "left chain should become right chain."
    )


def test_right_skewed_tree_keeps_order():
    root = _make_level_order([1, None, 2, None, 3])
    flatten_to_right(root)
    _assert_equal(
        _right_chain_values(root), [1, 2, 3], "right chain should keep preorder order."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree is no-op", test_empty_tree_is_noop),
        ("single node stays single chain", test_single_node_stays_single_chain),
        ("spec example preorder chain", test_spec_example_preorder_chain),
        ("left-skewed tree", test_left_skewed_tree),
        ("right-skewed tree keeps order", test_right_skewed_tree_keeps_order),
    ]
    _run_all_tests(TEST_CASES)
