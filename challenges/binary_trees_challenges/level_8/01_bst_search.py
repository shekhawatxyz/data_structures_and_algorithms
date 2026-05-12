# Level 8a - BST search
# Implement bst_search(root, target) - find a node by key in BST traversal order.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 8a — BST search
#
# Implement `bst_search(root, target) -> Node | None`. Return the first node found (in BST search order) whose `value == target`, or `None`.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _make_bst(values):
    root = None
    for v in values:
        root = _bst_insert_helper(root, v)
    return root


def _bst_insert_helper(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = _bst_insert_helper(root.left, value)
    else:
        root.right = _bst_insert_helper(root.right, value)
    return root


def bst_search(root, target):
    raise NotImplementedError("Implement bst_search(root, target).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_returns_none():
    _assert_true(bst_search(None, 5) is None, "search in empty tree should return None.")


def test_root_match():
    tree = _make_bst([5, 2, 8])
    found = bst_search(tree, 5)
    _assert_true(found is not None, "search for root value should find a node.")
    _assert_equal(found.value, 5, "found node should have target value.")


def test_left_subtree_match():
    tree = _make_bst([5, 2, 8, 1, 3])
    found = bst_search(tree, 3)
    _assert_true(found is not None, "search for left-subtree value should find a node.")
    _assert_equal(found.value, 3, "found node should have target value.")


def test_right_subtree_match():
    tree = _make_bst([5, 2, 8, 6, 9])
    found = bst_search(tree, 9)
    _assert_true(found is not None, "search for right-subtree value should find a node.")
    _assert_equal(found.value, 9, "found node should have target value.")


def test_no_match_returns_none():
    tree = _make_bst([5, 2, 8, 1, 3])
    _assert_true(bst_search(tree, 4) is None, "missing value should return None.")


def test_duplicate_target_returns_first_match():
    root = Node(5, right=Node(5))
    _assert_true(bst_search(root, 5) is root,
                 "search should return the first matching node in BST search order.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree returns None", test_empty_tree_returns_none),
        ("root match", test_root_match),
        ("left subtree match", test_left_subtree_match),
        ("right subtree match", test_right_subtree_match),
        ("no match returns None", test_no_match_returns_none),
        ("duplicate target returns first match", test_duplicate_target_returns_first_match),
    ]
    _run_all_tests(TEST_CASES)
