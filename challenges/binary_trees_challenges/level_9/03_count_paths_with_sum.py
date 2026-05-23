# Level 9c - Count paths with sum
# Implement count_paths_with_sum(root, target) counting downward paths with target sum.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 9c — Count paths with sum
#
# Implement `count_paths_with_sum(root, target) -> int`: the number of distinct downward paths (following `left`/`right` pointers, any start node, ending at or below it, length ≥ 1) whose values sum to `target`.
#
# ```
# count_paths_with_sum(from_level_order([1, 2, 3]), 3)   # 2
# # the single node 3, and the path 1 -> 2
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


def count_paths_with_sum(root, target):
    raise NotImplementedError("Implement count_paths_with_sum(root, target).")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_has_zero_paths():
    _assert_equal(count_paths_with_sum(None, 5), 0, "empty tree should have no paths.")


def test_single_node_match_and_miss():
    _assert_equal(count_paths_with_sum(Node(7), 7), 1, "single matching node is one path.")
    _assert_equal(count_paths_with_sum(Node(7), 8), 0, "single nonmatching node is no path.")


def test_spec_example_counts_two_paths():
    tree = _make_level_order([1, 2, 3])
    _assert_equal(count_paths_with_sum(tree, 3), 2, "spec example should count node 3 and path 1 -> 2.")


def test_paths_may_start_below_root():
    tree = _make_level_order([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    _assert_equal(count_paths_with_sum(tree, 8), 3, "valid paths may start below the root.")


def test_overlapping_zero_paths():
    tree = _make_level_order([0, 0, 0])
    _assert_equal(count_paths_with_sum(tree, 0), 5, "overlapping downward paths should all count.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree has zero paths", test_empty_tree_has_zero_paths),
        ("single node match and miss", test_single_node_match_and_miss),
        ("spec example counts two paths", test_spec_example_counts_two_paths),
        ("paths may start below root", test_paths_may_start_below_root),
        ("overlapping zero paths", test_overlapping_zero_paths),
    ]
    _run_all_tests(TEST_CASES)
