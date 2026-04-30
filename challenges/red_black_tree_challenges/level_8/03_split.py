# Level 8c - Split
# Split an RBT at a key into two valid RBTs.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 8c. Split an RBT at a key
#
# ```
# def split(tree, k) -> Tuple[Tree, Tree]
# ```
#
# Given an RBT and a key `k`, produce two valid RBTs `(t_lt, t_ge)` containing the keys less than `k` and the keys greater than or equal to `k` respectively. In O(log n) using `join`.
#
# The technique walks down the tree from the root looking for `k`. At each step you take a left or right turn; the *other* subtree, plus the current node, contributes to one of `t_lt` or `t_ge`. Accumulate by repeatedly joining. The amortized cost works out because at each level you're joining trees of geometrically growing size.
#
# This is the deepest test of your understanding of black-heights and the join primitive.

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


def split(tree, k):
    raise NotImplementedError('Implement split(tree, k).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_split_empty_tree():
    tree = Tree()
    t_lt, t_ge = split(tree, 10)
    _assert_true(t_lt.root is t_lt.nil, "Left split of empty tree should be empty.")
    _assert_true(t_ge.root is t_ge.nil, "Right split of empty tree should be empty.")


def test_split_all_left():
    tree = _build_simple_rbt([1, 2, 3, 4, 5])
    t_lt, t_ge = split(tree, 10)
    _assert_true(_is_valid_rbt(t_lt), "t_lt should be valid.")
    _assert_true(_is_valid_rbt(t_ge), "t_ge should be valid.")
    _assert_equal(_inorder(t_lt), [1, 2, 3, 4, 5], "All keys should be in t_lt.")
    _assert_equal(_inorder(t_ge), [], "t_ge should be empty.")


def test_split_all_right():
    tree = _build_simple_rbt([10, 20, 30, 40, 50])
    t_lt, t_ge = split(tree, 5)
    _assert_true(_is_valid_rbt(t_lt), "t_lt should be valid.")
    _assert_true(_is_valid_rbt(t_ge), "t_ge should be valid.")
    _assert_equal(_inorder(t_lt), [], "t_lt should be empty.")
    _assert_equal(_inorder(t_ge), [10, 20, 30, 40, 50], "All keys should be in t_ge.")


def test_split_middle():
    tree = _build_simple_rbt([10, 20, 30, 40, 50, 60, 70])
    t_lt, t_ge = split(tree, 40)
    _assert_true(_is_valid_rbt(t_lt), "t_lt should be valid.")
    _assert_true(_is_valid_rbt(t_ge), "t_ge should be valid.")
    lt_keys = _inorder(t_lt)
    ge_keys = _inorder(t_ge)
    _assert_true(all(k < 40 for k in lt_keys), "All keys in t_lt should be < 40.")
    _assert_true(all(k >= 40 for k in ge_keys), "All keys in t_ge should be >= 40.")
    _assert_equal(sorted(lt_keys + ge_keys), [10, 20, 30, 40, 50, 60, 70], "Union should be all keys.")


def test_split_at_existing_key():
    tree = _build_simple_rbt([5, 10, 15, 20, 25])
    t_lt, t_ge = split(tree, 15)
    _assert_true(_is_valid_rbt(t_lt), "t_lt should be valid.")
    _assert_true(_is_valid_rbt(t_ge), "t_ge should be valid.")
    _assert_equal(_inorder(t_lt), [5, 10], "Keys < 15 should be [5, 10].")
    _assert_equal(_inorder(t_ge), [15, 20, 25], "Keys >= 15 should be [15, 20, 25].")


if __name__ == "__main__":
    TEST_CASES = [
        ("split empty tree", test_split_empty_tree),
        ("split all left", test_split_all_left),
        ("split all right", test_split_all_right),
        ("split middle", test_split_middle),
        ("split at existing key", test_split_at_existing_key),
    ]
    _run_all_tests(TEST_CASES)
