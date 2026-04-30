# Level 6b - Naive Delete
# BST-style delete adapted for RBT, tracking the color of the removed/moved node.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 6b. BST-style delete (adapted)
#
# ```
# def naive_delete(tree, z) -> Tuple[Node, Color]
# ```
#
# Three cases, as in standard BST delete:
# - `z` has no left child: transplant `z.right` for `z`.
# - `z` has no right child: transplant `z.left` for `z`.
# - `z` has two children: find `y = minimum(z.right)`. If `y` is `z.right`, transplant `y` for `z` and reassign `z.left` to `y`. Otherwise transplant `y.right` for `y`, then `y` for `z`, fixing up children.
#
# The wrinkle that makes this RBT-specific: track the *color of the node that was physically removed or moved within the tree* and the *node that took its place*. If a black node was removed/moved, the tree may now violate property 5 (some path lost a black node) or property 4 (red-red at the substitution site).
#
# Return the substituted node and the original color of the moved node, since that is what the fix-up needs.
#
# Run your verifier — confirm it diagnoses the violation correctly when a black node was removed.

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


def naive_delete(tree, z):
    raise NotImplementedError('Implement naive_delete(tree, z).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_delete_leaf():
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED), (30, RED)])
    x, original_color = naive_delete(tree, nodes[10])
    _assert_true(10 not in _inorder(tree), "Key 10 should be removed.")
    _assert_equal(original_color, RED, "Original color of deleted leaf should be RED.")


def test_delete_node_with_one_child():
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, BLACK), (30, BLACK), (5, RED)])
    x, original_color = naive_delete(tree, nodes[10])
    _assert_true(10 not in _inorder(tree), "Key 10 should be removed.")


def test_delete_node_with_two_children():
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [
        (20, BLACK), (10, RED), (30, RED), (5, BLACK), (15, BLACK),
    ])
    x, original_color = naive_delete(tree, nodes[10])
    _assert_true(10 not in _inorder(tree), "Key 10 should be removed.")
    remaining = _inorder(tree)
    _assert_equal(remaining, [5, 15, 20, 30], "Remaining keys should be sorted.")


def test_delete_root():
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED), (30, RED)])
    x, original_color = naive_delete(tree, nodes[20])
    _assert_true(20 not in _inorder(tree), "Key 20 should be removed.")
    _assert_equal(original_color, BLACK, "Root was BLACK.")


def test_returns_tuple():
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED)])
    result = naive_delete(tree, nodes[10])
    _assert_true(
        isinstance(result, tuple) and len(result) == 2,
        "naive_delete should return a 2-tuple (replacement_node, original_color).",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("delete leaf", test_delete_leaf),
        ("delete node with one child", test_delete_node_with_one_child),
        ("delete node with two children", test_delete_node_with_two_children),
        ("delete root", test_delete_root),
        ("returns tuple", test_returns_tuple),
    ]
    _run_all_tests(TEST_CASES)
