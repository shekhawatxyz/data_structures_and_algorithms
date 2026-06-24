# Level 8b - Merge two trees
# Implement merge_two_trees(t1, t2) combining overlapping nodes by value sum.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 8b — Merge two trees
#
# Implement `merge_two_trees(t1, t2) -> Node`. A position present in both inputs holds the sum of the two values; a position present in only one input holds that input's node. Mutating `t1` in place and returning it is fine.
#
# ```
# t1 = from_level_order([1, 3, 2, 5])
# t2 = from_level_order([2, 1, 3, None, 4, None, 7])
# level_order(merge_two_trees(t1, t2))   # [3, 4, 5, 5, 4, 7]
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
    values = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        values.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return values


def merge_two_trees(t1, t2):
    if t1 is None:
        return t2
    if t1 and t2:
        t1.left = merge_two_trees(t1.left, t2.left)
        t1.right = merge_two_trees(t1.right, t2.right)
        t1.value = t1.value + t2.value
    return t1


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_two_empty_trees_merge_to_none():
    _assert_true(
        merge_two_trees(None, None) is None, "two empty trees should merge to None."
    )


def test_one_empty_tree_returns_other_values():
    tree = _make_level_order([1, 2, 3])
    result = merge_two_trees(None, tree)
    _assert_equal(
        _level_order_values(result),
        [1, 2, 3],
        "empty plus tree should keep tree values.",
    )


def test_spec_example_values():
    t1 = _make_level_order([1, 3, 2, 5])
    t2 = _make_level_order([2, 1, 3, None, 4, None, 7])
    _assert_equal(
        _level_order_values(merge_two_trees(t1, t2)),
        [3, 4, 5, 5, 4, 7],
        "spec example should sum overlaps and keep one-sided nodes.",
    )


def test_one_sided_children_are_kept():
    t1 = _make_level_order([1, None, 2])
    t2 = _make_level_order([3, 4, None])
    result = merge_two_trees(t1, t2)
    _assert_equal(result.value, 4, "roots should be summed.")
    _assert_equal(result.left.value, 4, "left child from second tree should be kept.")
    _assert_equal(result.right.value, 2, "right child from first tree should be kept.")


if __name__ == "__main__":
    TEST_CASES = [
        ("two empty trees merge to None", test_two_empty_trees_merge_to_none),
        (
            "one empty tree returns other values",
            test_one_empty_tree_returns_other_values,
        ),
        ("spec example values", test_spec_example_values),
        ("one-sided children are kept", test_one_sided_children_are_kept),
    ]
    _run_all_tests(TEST_CASES)
