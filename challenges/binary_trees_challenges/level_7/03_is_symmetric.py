# Level 7c - Is symmetric
# Implement is_symmetric(root) - True iff left subtree mirrors right subtree.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 7c — Is symmetric
#
# Implement `is_symmetric(root) -> bool`. The tree is symmetric iff its left subtree is a mirror image of its right subtree (in both shape and values). The empty tree is symmetric.
#
# ```
# is_symmetric(from_level_order([1, 2, 2, 3, 4, 4, 3]))   # True
# is_symmetric(from_level_order([1, 2, 2, None, 3, None, 3]))   # False
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


def is_symmetric_helper(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.value != b.value:
        return False
    return is_symmetric_helper(a.left, b.right) and is_symmetric_helper(a.right, b.left)


def is_symmetric(root):
    if root is None:
        return True
    return is_symmetric_helper(root.left, root.right)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_is_symmetric():
    _assert_equal(is_symmetric(None), True, "empty tree should be symmetric.")


def test_single_node_is_symmetric():
    _assert_equal(is_symmetric(Node(7)), True, "single node should be symmetric.")


def test_symmetric_example():
    tree = _make_level_order([1, 2, 2, 3, 4, 4, 3])
    _assert_equal(
        is_symmetric(tree),
        True,
        "spec example with mirrored values should be symmetric.",
    )


def test_asymmetric_shape():
    tree = _make_level_order([1, 2, 2, None, 3, None, 3])
    _assert_equal(
        is_symmetric(tree),
        False,
        "asymmetric shape from spec example should not be symmetric.",
    )


def test_asymmetric_values():
    tree = _make_level_order([1, 2, 2, 3, 4, 5, 3])
    _assert_equal(
        is_symmetric(tree), False, "different inner values should break symmetry."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree is symmetric", test_empty_tree_is_symmetric),
        ("single node is symmetric", test_single_node_is_symmetric),
        ("symmetric example", test_symmetric_example),
        ("asymmetric shape", test_asymmetric_shape),
        ("asymmetric values", test_asymmetric_values),
    ]
    _run_all_tests(TEST_CASES)
