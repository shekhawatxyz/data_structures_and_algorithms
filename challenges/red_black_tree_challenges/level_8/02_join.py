# Level 8b - Join Two RBTs
# Join two red-black trees where all keys in t1 are less than all keys in t2.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 8b. Join two RBTs
#
# ```
# def join(t1, t2) -> Tree
# ```
#
# Pre: every key in `t1` is less than every key in `t2`. Post: a single valid RBT containing all keys of both, in O(log n) time.
#
# The technique:
# - Find the larger of `t1`'s and `t2`'s black-heights. WLOG say `t1` has the larger black-height (call it `bh1 ≥ bh2`).
# - Find a node `x` on the right spine of `t1` whose black-height is exactly `bh2` and whose color is black. Walk down the right spine, decrementing the black-height counter on every black step, until you hit `bh2`.
# - Take the maximum of `t1` (or minimum of `t2`) as a new red "bridge" node, splice it between `x` and `t2`.
# - Run insert fix-up on the bridge node.
#
# Handling the case where one tree is empty, both are empty, the bridge insertion violates property 4, etc., is fiddly. Tracking black-heights correctly is the conceptual core.

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


def join(t1, t2):
    raise NotImplementedError('Implement join(t1, t2).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _build_simple_rbt(keys):
    """Build a valid RBT by repeated insertion for testing."""
    tree = Tree()
    for k in keys:
        z = Node(key=k, color=RED, left=tree.nil, right=tree.nil)
        y = tree.nil
        x = tree.root
        while x is not tree.nil:
            y = x
            if k < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is tree.nil:
            tree.root = z
        elif k < y.key:
            y.left = z
        else:
            y.right = z
        _insert_fixup(tree, z)
    return tree


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


def test_join_both_empty():
    t1 = Tree()
    t2 = Tree()
    result = join(t1, t2)
    _assert_true(result.root is result.nil, "Join of two empty trees should be empty.")


def test_join_left_empty():
    t1 = Tree()
    t2 = _build_simple_rbt([10, 20, 30])
    result = join(t1, t2)
    _assert_true(_is_valid_rbt(result), "Join with empty left should be valid.")
    _assert_equal(_inorder(result), [10, 20, 30], "Should contain all keys of t2.")


def test_join_right_empty():
    t1 = _build_simple_rbt([10, 20, 30])
    t2 = Tree()
    result = join(t1, t2)
    _assert_true(_is_valid_rbt(result), "Join with empty right should be valid.")
    _assert_equal(_inorder(result), [10, 20, 30], "Should contain all keys of t1.")


def test_join_equal_size():
    t1 = _build_simple_rbt([1, 2, 3, 4, 5])
    t2 = _build_simple_rbt([10, 20, 30, 40, 50])
    result = join(t1, t2)
    _assert_true(_is_valid_rbt(result), "Joined tree should be valid.")
    _assert_equal(
        _inorder(result),
        [1, 2, 3, 4, 5, 10, 20, 30, 40, 50],
        "Inorder should contain all keys sorted.",
    )


def test_join_unequal_size():
    t1 = _build_simple_rbt([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    t2 = _build_simple_rbt([100, 200])
    result = join(t1, t2)
    _assert_true(_is_valid_rbt(result), "Joined tree of unequal sizes should be valid.")
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200]
    _assert_equal(_inorder(result), expected, "Inorder should contain all keys sorted.")


if __name__ == "__main__":
    TEST_CASES = [
        ("join both empty", test_join_both_empty),
        ("join left empty", test_join_left_empty),
        ("join right empty", test_join_right_empty),
        ("join equal size", test_join_equal_size),
        ("join unequal size", test_join_unequal_size),
    ]
    _run_all_tests(TEST_CASES)
