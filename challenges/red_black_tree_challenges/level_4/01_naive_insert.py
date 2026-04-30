# Level 4a - Naive Insert
# BST-style insert, color the new node red, no fix-up.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 4a. BST-style colored insert (no fix-up yet)
#
# ```
# def naive_insert(tree, key) -> Node
# ```
#
# Standard BST insert. Color the newly inserted node red. Return the inserted node.
#
# After the call, the tree may not be a valid RBT — it may violate property 2 (if the tree was empty and the new node is red root) or property 4 (if the parent is red). Property 5 is preserved because the new node is red and replaces a NIL leaf, contributing zero to black-height.
#
# Call your verifier from 1a — confirm it correctly identifies which property is violated.

RED = "R"
BLACK = "B"


class Node:
    def __init__(self, key, color=RED, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.nil = Node(key=None, color=BLACK)
        self.root = self.nil


def naive_insert(tree, key):
    raise NotImplementedError('Implement naive_insert(tree, key).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _assert_raises(callable_obj, context):
    try:
        callable_obj()
    except Exception:
        return
    raise AssertionError(f"{context} Expected an exception, but none was raised.")


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
    total = len(test_cases)

    for name, fn in test_cases:
        if _run_test(name, fn):
            passed += 1

    print(f"\nPassed {passed}/{total} tests.")
    if passed != total:
        raise SystemExit(1)


def _inorder(tree):
    result = []
    def walk(node):
        if node is tree.nil:
            return
        walk(node.left)
        result.append(node.key)
        walk(node.right)
    walk(tree.root)
    return result


def test_naive_insert_into_empty():
    tree = Tree()
    z = naive_insert(tree, 10)
    _assert_equal(z.key, 10, "Inserted node should have key 10.")
    _assert_equal(z.color, RED, "Inserted node should be RED.")
    _assert_true(tree.root is z, "Inserted node should become root.")


def test_naive_insert_left_child():
    tree = Tree()
    tree.root = Node(key=20, color=BLACK, left=tree.nil, right=tree.nil)
    tree.root.parent = tree.nil
    z = naive_insert(tree, 10)
    _assert_equal(z.key, 10, "Inserted node should have key 10.")
    _assert_true(tree.root.left is z, "10 should be left child of root.")
    _assert_true(z.parent is tree.root, "Parent of 10 should be root.")


def test_naive_insert_right_child():
    tree = Tree()
    tree.root = Node(key=20, color=BLACK, left=tree.nil, right=tree.nil)
    tree.root.parent = tree.nil
    z = naive_insert(tree, 30)
    _assert_equal(z.key, 30, "Inserted node should have key 30.")
    _assert_true(tree.root.right is z, "30 should be right child of root.")


def test_naive_insert_preserves_bst_order():
    tree = Tree()
    for key in [20, 10, 30, 5, 15]:
        naive_insert(tree, key)
    _assert_equal(_inorder(tree), [5, 10, 15, 20, 30], "In-order should be sorted.")


def test_naive_insert_all_red():
    tree = Tree()
    for key in [50, 25, 75, 10]:
        z = naive_insert(tree, key)
        _assert_equal(z.color, RED, f"All naively inserted nodes should be RED (key={key}).")


if __name__ == "__main__":
    TEST_CASES = [
        ("naive insert into empty", test_naive_insert_into_empty),
        ("naive insert left child", test_naive_insert_left_child),
        ("naive insert right child", test_naive_insert_right_child),
        ("naive insert preserves BST order", test_naive_insert_preserves_bst_order),
        ("naive insert all red", test_naive_insert_all_red),
    ]
    _run_all_tests(TEST_CASES)
