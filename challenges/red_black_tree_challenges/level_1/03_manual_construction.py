# Level 1c - Manual Construction
# Manually construct valid and invalid RBTs by setting node fields directly.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 1c. Manual construction
#
# Construct, by hand (i.e. by directly assigning fields), at least:
# - Three valid RBTs of differing shapes.
# - One tree that violates property 2 only.
# - One that violates property 4 only.
# - One that violates property 5 only.
#
# Run them through your verifier from 1a. Confirm valid trees pass and invalid trees fail with the correct diagnosis.

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


def build_valid_tree_1():
    raise NotImplementedError('Implement build_valid_tree_1().')


def build_valid_tree_2():
    raise NotImplementedError('Implement build_valid_tree_2().')


def build_valid_tree_3():
    raise NotImplementedError('Implement build_valid_tree_3().')


def build_invalid_prop2():
    raise NotImplementedError('Implement build_invalid_prop2().')


def build_invalid_prop4():
    raise NotImplementedError('Implement build_invalid_prop4().')


def build_invalid_prop5():
    raise NotImplementedError('Implement build_invalid_prop5().')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _is_valid_rbt(tree):
    """Minimal verifier for testing manual constructions."""
    def _check_bst(node, nil, lo, hi):
        if node is nil:
            return True
        if node.key is None:
            return False
        if lo is not None and node.key <= lo:
            return False
        if hi is not None and node.key >= hi:
            return False
        return _check_bst(node.left, nil, lo, node.key) and _check_bst(node.right, nil, node.key, hi)

    def _check_black_height(node, nil):
        if node is nil:
            return 0
        left_bh = _check_black_height(node.left, nil)
        right_bh = _check_black_height(node.right, nil)
        if left_bh == -1 or right_bh == -1 or left_bh != right_bh:
            return -1
        return left_bh + (1 if node.color == BLACK else 0)

    nil = tree.nil
    if tree.root is nil:
        return True
    # Property 2: root is black
    if tree.root.color != BLACK:
        return False
    # Property 4: no red-red
    def _no_red_red(node):
        if node is nil:
            return True
        if node.color == RED:
            if node.left.color == RED or node.right.color == RED:
                return False
        return _no_red_red(node.left) and _no_red_red(node.right)
    if not _no_red_red(tree.root):
        return False
    # Property 5: consistent black-height
    if _check_black_height(tree.root, nil) == -1:
        return False
    # BST property
    if not _check_bst(tree.root, nil, None, None):
        return False
    return True


def test_valid_tree_1():
    tree = build_valid_tree_1()
    _assert_true(_is_valid_rbt(tree), "build_valid_tree_1 should produce a valid RBT.")


def test_valid_tree_2():
    tree = build_valid_tree_2()
    _assert_true(_is_valid_rbt(tree), "build_valid_tree_2 should produce a valid RBT.")


def test_valid_tree_3():
    tree = build_valid_tree_3()
    _assert_true(_is_valid_rbt(tree), "build_valid_tree_3 should produce a valid RBT.")


def test_invalid_prop2():
    tree = build_invalid_prop2()
    _assert_true(
        tree.root.color == RED,
        "build_invalid_prop2 should have a red root (violates property 2).",
    )


def test_invalid_prop4():
    tree = build_invalid_prop4()
    _assert_true(
        not _is_valid_rbt(tree),
        "build_invalid_prop4 should not be a valid RBT.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("valid tree 1", test_valid_tree_1),
        ("valid tree 2", test_valid_tree_2),
        ("valid tree 3", test_valid_tree_3),
        ("invalid prop2 (red root)", test_invalid_prop2),
        ("invalid prop4 (red-red)", test_invalid_prop4),
    ]
    _run_all_tests(TEST_CASES)
