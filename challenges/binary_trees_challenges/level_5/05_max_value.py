# Level 5e - Max value
# Implement max_value(root) returning the largest value in the tree.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 5e — Max value
#
# Implement `max_value(root) -> int`, the largest value in the tree. Choose and document a behaviour for the empty tree (e.g. raise `ValueError`).
#
# This scaffold expects `ValueError` for the empty tree.


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


def max_value(root):
    if root is None:
        raise ValueError
    candidates = [root.value]
    if root.left:
        candidates.append(max_value(root.left))
    if root.right:
        candidates.append(max_value(root.right))
    return max(candidates)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _assert_raises(expected_exception, fn, context):
    try:
        fn()
    except expected_exception:
        return
    except Exception as exc:
        raise AssertionError(
            f"{context} Expected {expected_exception.__name__}, got {type(exc).__name__}."
        )
    raise AssertionError(f"{context} Expected {expected_exception.__name__}.")


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


def test_empty_tree_raises_value_error():
    _assert_raises(
        ValueError, lambda: max_value(None), "empty tree behavior should be documented."
    )


def test_single_node_max():
    _assert_equal(max_value(Node(7)), 7, "single node maximum should be its value.")


def test_max_in_right_subtree():
    tree = _make_level_order([1, 2, 9, 4, 5])
    _assert_equal(max_value(tree), 9, "maximum may appear in the right subtree.")


def test_max_in_left_subtree():
    tree = _make_level_order([1, 12, 3, 4, 5])
    _assert_equal(max_value(tree), 12, "maximum may appear in the left subtree.")


def test_all_negative_values():
    tree = _make_level_order([-10, -4, -7, -20])
    _assert_equal(
        max_value(tree), -4, "maximum among negatives is the least negative value."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree raises ValueError", test_empty_tree_raises_value_error),
        ("single node max", test_single_node_max),
        ("max in right subtree", test_max_in_right_subtree),
        ("max in left subtree", test_max_in_left_subtree),
        ("all negative values", test_all_negative_values),
    ]
    _run_all_tests(TEST_CASES)
