# Level 6c - Delete Fix-up
# Fix the red-black tree after deletion of a black node.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 6c. Delete fix-up
#
# The fix-up walks up the tree from the substituted node `x`, treating `x` as carrying an "extra black" (the doubly-black sentinel of CLRS). Four cases:
#
# > Case 1: `x`'s sibling `w` is red. Rotate to make `w` black; reduces to one of cases 2, 3, 4.
# >
# > Case 2: `w` is black, both of `w`'s children are black. Recolor `w` red, push the extra black up to `x.parent`.
# >
# > Case 3: `w` is black, `w`'s left child is red, `w`'s right child is black (when `x` is a left child; mirror otherwise). Rotate `w` to convert to case 4.
# >
# > Case 4: `w` is black, `w`'s right child is red (when `x` is a left child). Rotate `x.parent`, recolor, terminate.
#
# ```
# def delete_fixup(tree, x) -> None
# ```
#
# This is the hardest single piece of the entire RBT machinery. Take it slowly. Each case has a mirror; do them one mirror at a time and lean hard on the verifier. Hand-construct minimal inputs that exercise each case in isolation before testing combinations.

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


def delete_fixup(tree, x):
    raise NotImplementedError('Implement delete_fixup(tree, x).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _make_tree_with_nodes(tree, keys_colors):
    """Build tree manually in BST fashion, return dict of nodes."""
    nodes = {}
    for key, color in keys_colors:
        node = Node(key=key, color=color, left=tree.nil, right=tree.nil)
        nodes[key] = node
        if tree.root is tree.nil:
            tree.root = node
            node.parent = tree.nil
        else:
            current = tree.root
            while True:
                if key < current.key:
                    if current.left is tree.nil:
                        current.left = node
                        node.parent = current
                        break
                    current = current.left
                else:
                    if current.right is tree.nil:
                        current.right = node
                        node.parent = current
                        break
                    current = current.right
    return nodes


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


def test_fixup_case2_both_children_black():
    # Sibling is black with both children black -> recolor sibling red
    # Tree:   20B
    #        /    \
    #      10B    30B
    # Delete 10's content, x = nil at 10's position, sibling = 30B
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, BLACK), (30, BLACK)])
    # Simulate: 10 was removed, x = tree.nil sitting at left of 20
    tree.root.left = tree.nil
    x = tree.nil
    x.parent = tree.root
    delete_fixup(tree, x)
    _assert_equal(tree.root.color, BLACK, "Root should remain BLACK.")


def test_fixup_case4_sibling_right_child_red():
    # Case 4: sibling is black, sibling's right child is red.
    #       20B
    #      /    \
    #    10B    30B
    #              \
    #              40R
    # x = nil at 10's old position
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, BLACK), (30, BLACK), (40, RED)])
    tree.root.left = tree.nil
    x = tree.nil
    x.parent = tree.root
    delete_fixup(tree, x)
    _assert_true(_is_valid_rbt(tree), "Tree should be valid after case 4 fix-up.")


def test_fixup_x_is_red():
    # If x is red, just color it black and done.
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED), (30, BLACK)])
    # x is red node 10
    delete_fixup(tree, nodes[10])
    _assert_equal(nodes[10].color, BLACK, "Red x should be colored BLACK.")


def test_fixup_x_is_root():
    # If x is root, just color black.
    tree = Tree()
    root = Node(key=10, color=RED, left=tree.nil, right=tree.nil)
    tree.root = root
    root.parent = tree.nil
    delete_fixup(tree, root)
    _assert_equal(root.color, BLACK, "Root x should be colored BLACK.")


if __name__ == "__main__":
    TEST_CASES = [
        ("fixup case 2: both children black", test_fixup_case2_both_children_black),
        ("fixup case 4: sibling right child red", test_fixup_case4_sibling_right_child_red),
        ("fixup x is red", test_fixup_x_is_red),
        ("fixup x is root", test_fixup_x_is_root),
    ]
    _run_all_tests(TEST_CASES)
