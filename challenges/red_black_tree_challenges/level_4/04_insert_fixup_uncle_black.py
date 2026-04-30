# Level 4d - Insert Fix-up: Uncle Black Cases
# Handle the uncle-black cases of insert fix-up (rotations and recolor).

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 4d. Insert fix-up — the uncle-black cases
#
# When the uncle is black, the fix is local: one or two rotations plus a recolor, and the loop terminates. There are two sub-cases:
#
# > Case 2: `z` is the "inner" grandchild (e.g. parent is a left child and `z` is a right child). Rotate to convert this to case 3.
# >
# > Case 3: `z` is the "outer" grandchild. Recolor parent and grandparent, rotate the grandparent, terminate.
#
# Implement these cases (still without combining with 4c yet):
#
# ```
# def insert_fixup_uncle_black_only(tree, z) -> None
# ```
#
# Test on hand-constructed inputs where the uncle is always black at the moment of fix-up.

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


def insert_fixup_uncle_black_only(tree, z):
    raise NotImplementedError('Implement insert_fixup_uncle_black_only(tree, z).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_case3_outer_left_left():
    # Case 3 (outer): parent is left child, z is left child. Uncle is black (nil).
    #     30B
    #    /
    #   20R
    #  /
    # 10R  <-- z
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(30, BLACK), (20, RED), (10, RED)])
    insert_fixup_uncle_black_only(tree, nodes[10])
    _assert_equal(tree.root.key, 20, "Root should become 20 after rotation.")
    _assert_equal(tree.root.color, BLACK, "New root should be BLACK.")


def test_case2_then_case3_inner():
    # Case 2 (inner) -> Case 3: parent is left child, z is right child. Uncle is black (nil).
    #     30B
    #    /
    #   10R
    #     \
    #     20R  <-- z
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(30, BLACK), (10, RED), (20, RED)])
    insert_fixup_uncle_black_only(tree, nodes[20])
    _assert_equal(tree.root.key, 20, "Root should become 20 after double rotation.")


def test_case3_outer_right_right():
    # Mirror: parent is right child, z is right child. Uncle is black (nil).
    #   10B
    #     \
    #     20R
    #       \
    #       30R  <-- z
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(10, BLACK), (20, RED), (30, RED)])
    insert_fixup_uncle_black_only(tree, nodes[30])
    _assert_equal(tree.root.key, 20, "Root should become 20 after rotation.")


def test_preserves_inorder():
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(30, BLACK), (20, RED), (10, RED)])
    before = _inorder(tree)
    insert_fixup_uncle_black_only(tree, nodes[10])
    after = _inorder(tree)
    _assert_equal(sorted(before), after, "In-order should be preserved after fix-up.")


if __name__ == "__main__":
    TEST_CASES = [
        ("case 3: outer left-left", test_case3_outer_left_left),
        ("case 2 then case 3: inner", test_case2_then_case3_inner),
        ("case 3: outer right-right (mirror)", test_case3_outer_right_right),
        ("preserves inorder", test_preserves_inorder),
    ]
    _run_all_tests(TEST_CASES)
