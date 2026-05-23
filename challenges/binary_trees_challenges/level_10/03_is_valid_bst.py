# Level 10c - Is valid BST
# Implement is_valid_bst(root) - True iff the tree satisfies BST ordering.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 10c — Is valid BST
#
# Implement `is_valid_bst(root) -> bool`. A valid BST satisfies: for every node, all values in its left subtree are strictly less than the node's value, and all values in its right subtree are greater than or equal to the node's value. The empty tree is a valid BST.
#
# ```
# is_valid_bst(from_level_order([2, 1, 3]))           # True
# is_valid_bst(from_level_order([5, 1, 4, None, None, 3, 6]))   # False
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


def is_valid_bst(root):
    raise NotImplementedError("Implement is_valid_bst(root).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_is_valid():
    _assert_equal(is_valid_bst(None), True, "empty tree should be a valid BST.")


def test_single_node_is_valid():
    _assert_equal(is_valid_bst(Node(7)), True, "single node should be a valid BST.")


def test_simple_valid():
    _assert_equal(is_valid_bst(_make_level_order([2, 1, 3])), True,
                  "balanced [2,1,3] should be a valid BST.")


def test_spec_invalid():
    tree = _make_level_order([5, 1, 4, None, None, 3, 6])
    _assert_equal(is_valid_bst(tree), False,
                  "spec example should be detected as invalid.")


def test_violation_in_left_subtree():
    # 10 > 5 but 12 ends up in left subtree of 10
    tree = _make_level_order([10, 5, 15, None, 12])
    _assert_equal(is_valid_bst(tree), False,
                  "value larger than ancestor in left subtree should be invalid.")


def test_duplicates_allowed_on_right():
    tree = _make_level_order([5, 1, 5])
    _assert_equal(is_valid_bst(tree), True,
                  "duplicates on the right are allowed by the spec.")


def test_duplicates_rejected_on_left():
    tree = _make_level_order([5, 5, 6])
    _assert_equal(is_valid_bst(tree), False,
                  "duplicates on the left violate the strict-left rule.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree is valid", test_empty_tree_is_valid),
        ("single node is valid", test_single_node_is_valid),
        ("simple valid", test_simple_valid),
        ("spec invalid", test_spec_invalid),
        ("violation in left subtree", test_violation_in_left_subtree),
        ("duplicates allowed on right", test_duplicates_allowed_on_right),
        ("duplicates rejected on left", test_duplicates_rejected_on_left),
    ]
    _run_all_tests(TEST_CASES)
