# Level 3b - Right Rotate
# Perform a right rotation on node x in the red-black tree.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 3b. Right rotate
#
# Mirror of 3a. Should fall out almost mechanically once 3a is right.

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


def right_rotate(tree, x):
    raise NotImplementedError('Implement right_rotate(tree, x).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_right_rotate_root():
    tree, nodes = _make_simple_tree([(20, BLACK), (10, RED)])
    right_rotate(tree, nodes[20])
    _assert_equal(tree.root.key, 10, "After right_rotate on root, new root should be 10.")
    _assert_equal(tree.root.right.key, 20, "Old root should be right child of new root.")


def test_right_rotate_preserves_inorder():
    tree, nodes = _make_simple_tree([(30, BLACK), (20, RED), (40, BLACK), (10, BLACK), (25, BLACK)])
    before = _inorder(tree)
    right_rotate(tree, nodes[30])
    after = _inorder(tree)
    _assert_equal(after, before, "Right rotate should preserve in-order traversal.")


def test_right_rotate_parent_pointers():
    tree, nodes = _make_simple_tree([(20, BLACK), (10, RED), (5, BLACK)])
    right_rotate(tree, nodes[20])
    _assert_true(
        nodes[20].parent is nodes[10],
        "After right rotate, x.parent should be the old left child.",
    )
    _assert_true(
        nodes[10].parent is tree.nil,
        "New root's parent should be tree.nil.",
    )


def test_right_rotate_non_root():
    tree, nodes = _make_simple_tree([
        (30, BLACK), (20, BLACK), (40, BLACK), (10, RED), (25, RED),
    ])
    right_rotate(tree, nodes[20])
    _assert_equal(tree.root.key, 30, "Root should remain 30.")
    _assert_equal(tree.root.left.key, 10, "Left child of root should be 10.")
    _assert_equal(tree.root.left.right.key, 20, "20 should be right child of 10.")


if __name__ == "__main__":
    TEST_CASES = [
        ("right rotate root", test_right_rotate_root),
        ("right rotate preserves inorder", test_right_rotate_preserves_inorder),
        ("right rotate parent pointers", test_right_rotate_parent_pointers),
        ("right rotate non-root", test_right_rotate_non_root),
    ]
    _run_all_tests(TEST_CASES)
