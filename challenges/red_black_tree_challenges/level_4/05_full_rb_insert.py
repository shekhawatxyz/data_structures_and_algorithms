# Level 4e - Full RB Insert
# Complete red-black tree insertion with fix-up.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 4e. Full `rb_insert`
#
# ```
# def insert(tree, key) -> Node
# ```
#
# Combine 4a, 4c, and 4d into the full insert with fix-up. Don't forget to set the root to black at the end (handles the red-root case from 4b).

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


def insert(tree, key):
    raise NotImplementedError('Implement insert(tree, key).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_insert_single():
    tree = Tree()
    z = insert(tree, 10)
    _assert_equal(z.key, 10, "Inserted node should have key 10.")
    _assert_equal(tree.root.color, BLACK, "Root should be BLACK.")
    _assert_true(_is_valid_rbt(tree), "Tree should be valid after single insert.")


def test_insert_three_ascending():
    tree = Tree()
    insert(tree, 10)
    insert(tree, 20)
    insert(tree, 30)
    _assert_true(_is_valid_rbt(tree), "Tree should be valid after inserting 10, 20, 30.")
    _assert_equal(_inorder(tree), [10, 20, 30], "In-order should be [10, 20, 30].")


def test_insert_three_descending():
    tree = Tree()
    insert(tree, 30)
    insert(tree, 20)
    insert(tree, 10)
    _assert_true(_is_valid_rbt(tree), "Tree should be valid after inserting 30, 20, 10.")
    _assert_equal(_inorder(tree), [10, 20, 30], "In-order should be [10, 20, 30].")


def test_insert_seven_keys():
    tree = Tree()
    keys = [50, 25, 75, 10, 30, 60, 90]
    for k in keys:
        insert(tree, k)
    _assert_true(_is_valid_rbt(tree), "Tree should be valid after 7 inserts.")
    _assert_equal(_inorder(tree), sorted(keys), "In-order should be sorted.")


def test_insert_triggers_uncle_red_and_uncle_black():
    tree = Tree()
    keys = [20, 10, 30, 5, 15, 25, 35, 1]
    for k in keys:
        insert(tree, k)
    _assert_true(_is_valid_rbt(tree), "Tree should be valid after mixed fix-up cases.")
    _assert_equal(_inorder(tree), sorted(keys), "In-order should be sorted.")


if __name__ == "__main__":
    TEST_CASES = [
        ("insert single", test_insert_single),
        ("insert three ascending", test_insert_three_ascending),
        ("insert three descending", test_insert_three_descending),
        ("insert seven keys", test_insert_seven_keys),
        ("insert triggers uncle-red and uncle-black", test_insert_triggers_uncle_red_and_uncle_black),
    ]
    _run_all_tests(TEST_CASES)
