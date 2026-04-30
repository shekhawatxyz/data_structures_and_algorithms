# Level 4c - Insert Fix-up: Uncle Red Case
# Handle only the uncle-red case of insert fix-up (recolor and move up).

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 4c. Insert fix-up — the uncle-red case alone
#
# The fix-up loop walks up the tree as long as `z.parent.color == RED`. There are three cases (and three mirror cases, depending on whether the parent is a left or right child of the grandparent). Implement only the uncle-red case for now:
#
# > If `z`'s uncle is red: recolor parent and uncle to black, recolor grandparent to red, move `z` up to the grandparent, repeat the loop.
#
# ```
# def insert_fixup_uncle_red_only(tree, z) -> None
# ```
#
# This will not produce a fully valid RBT in general — it handles only one of the cases. But it should produce a valid RBT on inputs where the uncle-red case is the only one that ever fires during the entire fix-up. Construct such an input by hand and verify.

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


def insert_fixup_uncle_red_only(tree, z):
    raise NotImplementedError('Implement insert_fixup_uncle_red_only(tree, z).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_uncle_red_recolors_parent_and_uncle():
    # Tree:     20B
    #          /    \
    #        10R    30R
    #       /
    #      5R  <-- z (red-red violation, uncle 30 is red)
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED), (30, RED), (5, RED)])
    insert_fixup_uncle_red_only(tree, nodes[5])
    _assert_equal(nodes[10].color, BLACK, "Parent should become BLACK.")
    _assert_equal(nodes[30].color, BLACK, "Uncle should become BLACK.")
    _assert_equal(nodes[20].color, RED, "Grandparent should become RED.")


def test_uncle_red_root_stays_black():
    # After recoloring grandparent (root) to red, root should be set back to black.
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED), (30, RED), (5, RED)])
    insert_fixup_uncle_red_only(tree, nodes[5])
    _assert_equal(tree.root.color, BLACK, "Root should be BLACK after fix-up.")


def test_uncle_red_no_violation_after():
    # After fix-up, no red-red violation should remain (in uncle-red only scenario).
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED), (30, RED), (25, RED)])
    insert_fixup_uncle_red_only(tree, nodes[25])
    # Check no red-red at the fixed nodes
    _assert_equal(nodes[10].color, BLACK, "Uncle (10) should become BLACK.")
    _assert_equal(nodes[30].color, BLACK, "Parent (30) should become BLACK.")


def test_uncle_red_mirror_case():
    # Mirror: z is right child, parent is right child, uncle is left child
    #     20B
    #    /    \
    #  10R    30R
    #            \
    #            35R  <-- z
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED), (30, RED), (35, RED)])
    insert_fixup_uncle_red_only(tree, nodes[35])
    _assert_equal(nodes[30].color, BLACK, "Parent should become BLACK.")
    _assert_equal(nodes[10].color, BLACK, "Uncle should become BLACK.")


if __name__ == "__main__":
    TEST_CASES = [
        ("uncle red recolors parent and uncle", test_uncle_red_recolors_parent_and_uncle),
        ("uncle red root stays black", test_uncle_red_root_stays_black),
        ("uncle red no violation after", test_uncle_red_no_violation_after),
        ("uncle red mirror case", test_uncle_red_mirror_case),
    ]
    _run_all_tests(TEST_CASES)
