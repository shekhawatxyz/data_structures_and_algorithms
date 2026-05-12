# Level 5c - Sum values
# Implement sum_values(root) summing the integer values across the tree.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 5c — Sum values
#
# Implement `sum_values(root) -> int`. The sum over an empty tree is `0`. Assume node values are integers.

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


def sum_values(root):
    raise NotImplementedError("Implement sum_values(root).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_sum_is_zero():
    _assert_equal(sum_values(None), 0, "empty tree should sum to 0.")


def test_single_node_sum():
    _assert_equal(sum_values(Node(7)), 7, "single node should sum to its value.")


def test_full_tree_sum():
    _assert_equal(sum_values(_make_level_order([1, 2, 3, 4, 5])), 15,
                  "tree of values 1..5 should sum to 15.")


def test_negative_values_sum():
    _assert_equal(sum_values(_make_level_order([-1, -2, 3, None, 4])), 4,
                  "negative and positive values should combine correctly.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree sum is 0", test_empty_tree_sum_is_zero),
        ("single node sum", test_single_node_sum),
        ("full tree sum", test_full_tree_sum),
        ("negative values sum", test_negative_values_sum),
    ]
    _run_all_tests(TEST_CASES)
