# Level 6d - Full RB Delete
# Complete red-black tree deletion with fix-up.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 6d. Full `rb_delete`
#
# ```
# def delete(tree, key) -> bool
# ```
#
# Find the node, run 6b, run 6c if the displaced node was black. Return whether deletion happened (False if key not found).

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


def delete(tree, key):
    raise NotImplementedError('Implement delete(tree, key).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _is_valid_rbt(tree):
    """Minimal RBT verifier."""
    nil = tree.nil
    if tree.root is nil:
        return True
    if tree.root.color != BLACK:
        return False
    def _no_red_red(node):
        if node is nil:
            return True
        if node.color == RED:
            if node.left.color == RED or node.right.color == RED:
                return False
        return _no_red_red(node.left) and _no_red_red(node.right)
    if not _no_red_red(tree.root):
        return False
    def _check_bh(node):
        if node is nil:
            return 0
        l = _check_bh(node.left)
        r = _check_bh(node.right)
        if l == -1 or r == -1 or l != r:
            return -1
        return l + (1 if node.color == BLACK else 0)
    if _check_bh(tree.root) == -1:
        return False
    return True


def _insert(tree, key):
    """Minimal insert for building test trees."""
    z = Node(key=key, color=RED, left=tree.nil, right=tree.nil)
    y = tree.nil
    x = tree.root
    while x is not tree.nil:
        y = x
        if key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y is tree.nil:
        tree.root = z
    elif key < y.key:
        y.left = z
    else:
        y.right = z
    # Simple fix-up
    _insert_fixup(tree, z)


def _insert_fixup(tree, z):
    while z.parent.color == RED:
        if z.parent is z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == RED:
                z.parent.color = BLACK
                y.color = BLACK
                z.parent.parent.color = RED
                z = z.parent.parent
            else:
                if z is z.parent.right:
                    z = z.parent
                    _left_rotate(tree, z)
                z.parent.color = BLACK
                z.parent.parent.color = RED
                _right_rotate(tree, z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == RED:
                z.parent.color = BLACK
                y.color = BLACK
                z.parent.parent.color = RED
                z = z.parent.parent
            else:
                if z is z.parent.left:
                    z = z.parent
                    _right_rotate(tree, z)
                z.parent.color = BLACK
                z.parent.parent.color = RED
                _left_rotate(tree, z.parent.parent)
    tree.root.color = BLACK


def _left_rotate(tree, x):
    y = x.right
    x.right = y.left
    if y.left is not tree.nil:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is tree.nil:
        tree.root = y
    elif x is x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y


def _right_rotate(tree, x):
    y = x.left
    x.left = y.right
    if y.right is not tree.nil:
        y.right.parent = x
    y.parent = x.parent
    if x.parent is tree.nil:
        tree.root = y
    elif x is x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y


def test_delete_not_found():
    tree = Tree()
    _insert(tree, 10)
    _insert(tree, 20)
    result = delete(tree, 99)
    _assert_equal(result, False, "Deleting non-existent key should return False.")


def test_delete_single_node():
    tree = Tree()
    _insert(tree, 10)
    result = delete(tree, 10)
    _assert_equal(result, True, "Deleting existing key should return True.")
    _assert_true(tree.root is tree.nil, "Tree should be empty after deleting only node.")


def test_delete_preserves_validity():
    tree = Tree()
    for k in [20, 10, 30, 5, 15, 25, 35]:
        _insert(tree, k)
    delete(tree, 10)
    _assert_true(_is_valid_rbt(tree), "Tree should remain valid after deletion.")
    _assert_true(10 not in _inorder(tree), "Deleted key should not appear in inorder.")


def test_delete_all_keys():
    tree = Tree()
    keys = [50, 25, 75, 10, 30, 60, 90]
    for k in keys:
        _insert(tree, k)
    for k in keys:
        result = delete(tree, k)
        _assert_equal(result, True, f"Deleting {k} should return True.")
        _assert_true(_is_valid_rbt(tree), f"Tree should be valid after deleting {k}.")
    _assert_true(tree.root is tree.nil, "Tree should be empty after deleting all keys.")


def test_delete_root_of_three():
    tree = Tree()
    _insert(tree, 20)
    _insert(tree, 10)
    _insert(tree, 30)
    delete(tree, 20)
    _assert_true(_is_valid_rbt(tree), "Tree should be valid after deleting root.")
    _assert_equal(sorted(_inorder(tree)), [10, 30], "Remaining keys should be [10, 30].")


if __name__ == "__main__":
    TEST_CASES = [
        ("delete not found", test_delete_not_found),
        ("delete single node", test_delete_single_node),
        ("delete preserves validity", test_delete_preserves_validity),
        ("delete all keys", test_delete_all_keys),
        ("delete root of three", test_delete_root_of_three),
    ]
    _run_all_tests(TEST_CASES)
