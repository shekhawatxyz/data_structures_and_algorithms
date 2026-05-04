# Level 8b - BST insert
# Implement bst_insert(root, value) returning the (possibly new) root.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 8b — BST insert
#
# Implement `bst_insert(root, value) -> Node`. Return the (possibly new) root. Duplicates go to the right. Build the tree by chained calls:
#
# ```
# root = None
# for v in [5, 2, 8, 1, 3]:
#     root = bst_insert(root, v)
# inorder(root)   # [1, 2, 3, 5, 8]
# ```

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _inorder(root):
    if root is None:
        return []
    return _inorder(root.left) + [root.value] + _inorder(root.right)


def bst_insert(root, value) -> "Node":
    raise NotImplementedError("Implement bst_insert(root, value).")

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


def test_insert_into_empty_tree():
    root = bst_insert(None, 5)
    assert root is not None
    _assert_equal(root.value, 5, "new root should hold inserted value.")
    _assert_true(root.left is None and root.right is None, "new root should have no children.")


def test_chained_inserts_yield_sorted_inorder():
    root = None
    for v in [5, 2, 8, 1, 3]:
        root = bst_insert(root, v)
    _assert_equal(_inorder(root), [1, 2, 3, 5, 8],
                  "chained inserts should produce a sorted inorder traversal.")


def test_duplicates_go_right():
    root = bst_insert(None, 5)
    root = bst_insert(root, 5)
    assert root.right is not None
    _assert_equal(root.right.value, 5, "right child should hold duplicate value.")
    _assert_true(root.left is None, "duplicate should not land on the left.")


def test_inserts_preserve_structure():
    root = None
    for v in [10, 5, 15, 3]:
        root = bst_insert(root, v)
    assert root is not None
    assert root.left is not None
    assert root.right is not None
    assert root.left.left is not None
    _assert_equal(root.value, 10, "first inserted should remain root.")
    _assert_equal(root.left.value, 5, "smaller value should go left of root.")
    _assert_equal(root.right.value, 15, "larger value should go right of root.")
    _assert_equal(root.left.left.value, 3, "value smaller than 5 should go left of 5.")


def test_insert_returns_existing_root_for_non_empty_tree():
    root = bst_insert(None, 10)
    same_root = bst_insert(root, 12)
    _assert_true(same_root is root, "inserting into a non-empty tree should return the existing root.")


if __name__ == "__main__":
    TEST_CASES = [
        ("insert into empty tree", test_insert_into_empty_tree),
        ("chained inserts yield sorted inorder", test_chained_inserts_yield_sorted_inorder),
        ("duplicates go right", test_duplicates_go_right),
        ("inserts preserve structure", test_inserts_preserve_structure),
        ("insert returns existing root", test_insert_returns_existing_root_for_non_empty_tree),
    ]
    _run_all_tests(TEST_CASES)
