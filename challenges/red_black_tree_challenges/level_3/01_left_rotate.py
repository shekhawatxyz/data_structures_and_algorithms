# Level 3a - Left Rotate
# Perform a left rotation on node x in the red-black tree.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 3a. Left rotate
#
# ```
# def left_rotate(tree, x) -> None
# ```
#
# Pre: `x.right` is not NIL. Post: `x.right` becomes `x`'s old right child's left child, and `x.right` (the old one) becomes the parent of `x`.
#
# Get the pointer surgery exactly right:
# - Three pointers change going *down* (children).
# - Three pointers change going *up* (parents).
# - The root may change (if `x` was the root, the new root is `x`'s old right child).
#
# Draw it on paper before coding. Pointers in both directions must remain consistent.

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


def left_rotate(tree, x):
    raise NotImplementedError('Implement left_rotate(tree, x).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _make_simple_tree(keys_colors):
    """Build a minimal RBT for testing. keys_colors: list of (key, color)
    inserted manually in BST fashion."""
    tree = Tree()
    nodes = {}
    if not keys_colors:
        return tree, nodes
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
    return tree, nodes


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


def test_left_rotate_root():
    tree, nodes = _make_simple_tree([(10, BLACK), (20, RED)])
    left_rotate(tree, nodes[10])
    _assert_equal(tree.root.key, 20, "After left_rotate on root, new root should be 20.")
    _assert_equal(tree.root.left.key, 10, "Old root should be left child of new root.")


def test_left_rotate_preserves_inorder():
    tree, nodes = _make_simple_tree([(20, BLACK), (10, RED), (30, RED), (25, BLACK), (35, BLACK)])
    before = _inorder(tree)
    left_rotate(tree, nodes[30])
    after = _inorder(tree)
    _assert_equal(after, before, "Left rotate should preserve in-order traversal.")


def test_left_rotate_parent_pointers():
    tree, nodes = _make_simple_tree([(20, BLACK), (30, RED), (25, BLACK)])
    left_rotate(tree, nodes[20])
    _assert_true(
        nodes[20].parent is nodes[30],
        "After left rotate, x.parent should be the old right child.",
    )
    _assert_true(
        nodes[30].parent is tree.nil,
        "New root's parent should be tree.nil.",
    )


def test_left_rotate_non_root():
    tree, nodes = _make_simple_tree([
        (20, BLACK), (10, BLACK), (30, BLACK), (25, RED), (35, RED),
    ])
    left_rotate(tree, nodes[30])
    _assert_equal(tree.root.key, 20, "Root should remain 20.")
    _assert_equal(tree.root.right.key, 35, "Right child of root should be 35.")
    _assert_equal(tree.root.right.left.key, 30, "30 should be left child of 35.")


if __name__ == "__main__":
    TEST_CASES = [
        ("left rotate root", test_left_rotate_root),
        ("left rotate preserves inorder", test_left_rotate_preserves_inorder),
        ("left rotate parent pointers", test_left_rotate_parent_pointers),
        ("left rotate non-root", test_left_rotate_non_root),
    ]
    _run_all_tests(TEST_CASES)
