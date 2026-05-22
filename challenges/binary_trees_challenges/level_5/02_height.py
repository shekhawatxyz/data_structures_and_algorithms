# Level 5b - Height
# Implement height(root). Empty tree -> -1, single node -> 0.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 5b — Height
#
# Implement `height(root) -> int`. The height of an empty tree is `-1`; a single-node tree has height `0`.


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
        return -1
    return 1 + max(height(root.left), height(root.right))


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_height_is_minus_one():
    _assert_equal(height(None), -1, "empty tree should have height -1.")


def test_single_node_height_is_zero():
    _assert_equal(height(Node(1)), 0, "single node should have height 0.")


def test_balanced_height():
    _assert_equal(
        height(_make_level_order([1, 2, 3, 4, 5])),
        2,
        "balanced tree of three layers should have height 2.",
    )


def test_left_skewed_height():
    _assert_equal(
        height(_make_level_order([1, 2, None, 3, None, 4])),
        3,
        "left-skewed chain of four nodes should have height 3.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree height is -1", test_empty_tree_height_is_minus_one),
        ("single node height is 0", test_single_node_height_is_zero),
        ("balanced height", test_balanced_height),
        ("left-skewed height", test_left_skewed_height),
    ]
    _run_all_tests(TEST_CASES)
