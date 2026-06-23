# Level 7b - Mirror in place
# Implement mirror_in_place(root) swapping left/right at every node.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 7b — Mirror in place
#
# Implement `mirror_in_place(root) -> None`. Swap `left` and `right` at every node. The empty tree is a no-op.
#
# ```
# t = from_level_order([1, 2, 3, 4, 5])
# mirror_in_place(t)
# level_order(t)   # [1, 3, 2, 5, 4]
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


def _level_order_values(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result


def mirror_in_place(root):
    if root is None:
        return None
    right = root.right
    left = root.left
    root.right, root.left = left, right
    mirror_in_place(root.right)
    mirror_in_place(root.left)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_is_noop():
    result = mirror_in_place(None)
    _assert_true(result is None, "mirror_in_place should return None.")


def test_single_node_unchanged():
    node = Node(7)
    mirror_in_place(node)
    _assert_equal(_level_order_values(node), [7], "single node should be unchanged.")


def test_full_tree_mirrored():
    tree = _make_level_order([1, 2, 3, 4, 5])
    mirror_in_place(tree)
    _assert_equal(
        _level_order_values(tree),
        [1, 3, 2, 5, 4],
        "level-order of mirrored tree should match spec example.",
    )


def test_mirror_is_in_place():
    tree = _make_level_order([1, 2, 3])
    result = mirror_in_place(tree)
    _assert_true(result is None, "mirror_in_place should return None.")
    _assert_equal(
        _level_order_values(tree), [1, 3, 2], "tree should be modified in place."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree is noop", test_empty_tree_is_noop),
        ("single node unchanged", test_single_node_unchanged),
        ("full tree mirrored", test_full_tree_mirrored),
        ("mirror is in place", test_mirror_is_in_place),
    ]
    _run_all_tests(TEST_CASES)
