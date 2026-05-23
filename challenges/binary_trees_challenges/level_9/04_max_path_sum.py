# Level 9d - Max path sum
# Implement max_path_sum(root) returning the largest sum over any connected path.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 9d — Max path sum
#
# Implement `max_path_sum(root) -> int`: the largest possible sum of values along any path, where a path is a sequence of distinct nodes in which each consecutive pair is joined by an edge. A single node is a valid path. Values may be negative; assume at least one node.
#
# ```
# max_path_sum(from_level_order([-10, 9, 20, None, None, 15, 7]))   # 42
# # 15 -> 20 -> 7
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


def max_path_sum(root):
    raise NotImplementedError("Implement max_path_sum(root).")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_single_negative_node():
    _assert_equal(max_path_sum(Node(-3)), -3, "single node path should be valid even if negative.")


def test_simple_path_through_root():
    tree = _make_level_order([1, 2, 3])
    _assert_equal(max_path_sum(tree), 6, "best path should be 2 -> 1 -> 3.")


def test_spec_example():
    tree = _make_level_order([-10, 9, 20, None, None, 15, 7])
    _assert_equal(max_path_sum(tree), 42, "spec example should use path 15 -> 20 -> 7.")


def test_all_negative_values():
    tree = _make_level_order([-2, -1, -3])
    _assert_equal(max_path_sum(tree), -1, "with all negatives, the best path is one node.")


def test_larger_tree_combines_profitable_branches():
    tree = _make_level_order([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    _assert_equal(max_path_sum(tree), 48, "best path may combine profitable branches.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single negative node", test_single_negative_node),
        ("simple path through root", test_simple_path_through_root),
        ("spec example", test_spec_example),
        ("all negative values", test_all_negative_values),
        ("larger tree combines profitable branches", test_larger_tree_combines_profitable_branches),
    ]
    _run_all_tests(TEST_CASES)
