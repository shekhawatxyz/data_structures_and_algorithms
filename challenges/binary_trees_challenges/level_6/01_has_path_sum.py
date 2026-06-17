# Level 6a - Has path sum
# Implement has_path_sum(root, target) - True iff some root-to-leaf path sums to target.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 6a — Has path sum
#
# Implement `has_path_sum(root, target) -> bool`. Return `True` iff there exists a root-to-leaf path whose values sum to `target`. Return `False` for an empty tree.
#
# ```
# has_path_sum(from_level_order([5, 4, 8, 11, None, 13, 4, 7, 2]), 22)   # True
# has_path_sum(from_level_order([1, 2, 3]), 5)                            # False
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


def all_paths(root):
    if root is None:
        return []
    if not root.left and not root.right:
        return [[root.value]]
    child_paths = all_paths(root.left) + all_paths(root.right)
    return [[root.value] + p for p in child_paths]


def has_path_sum(root, target):
    new_list = all_paths(root)
    new_list = list(map(sum, new_list))
    return target in new_list


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_returns_false():
    _assert_equal(has_path_sum(None, 0), False, "empty tree has no root-to-leaf path.")


def test_spec_example_match():
    tree = _make_level_order([5, 4, 8, 11, None, 13, 4, 7, 2])
    _assert_equal(has_path_sum(tree, 22), True, "5->4->11->2 sums to 22.")


def test_spec_example_no_match():
    _assert_equal(
        has_path_sum(_make_level_order([1, 2, 3]), 5),
        False,
        "no root-to-leaf path in [1,2,3] sums to 5.",
    )


def test_partial_path_does_not_count():
    tree = _make_level_order([1, 2, None, 3])
    _assert_equal(
        has_path_sum(tree, 3),
        False,
        "1->2 sums to 3 but is not a root-to-leaf path; should not count.",
    )


def test_single_node_match():
    _assert_equal(
        has_path_sum(Node(7), 7), True, "single node is itself a root-to-leaf path."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree returns False", test_empty_tree_returns_false),
        ("spec example match", test_spec_example_match),
        ("spec example no match", test_spec_example_no_match),
        ("partial path does not count", test_partial_path_does_not_count),
        ("single node match", test_single_node_match),
    ]
    _run_all_tests(TEST_CASES)
