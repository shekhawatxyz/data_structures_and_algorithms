# Level 6a - Transplant
# Replace subtree rooted at u with subtree rooted at v.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 6a. Transplant
#
# ```
# def transplant(tree, u, v) -> None
# ```
#
# Replace the subtree rooted at `u` with the subtree rooted at `v`. Update `u.parent`'s child pointer (or the tree root if `u` was the root) and set `v.parent`. Does not touch `u`'s children. This is your delete primitive.

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


def transplant(tree, u, v):
    raise NotImplementedError('Implement transplant(tree, u, v).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_transplant_root():
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED), (30, RED)])
    transplant(tree, nodes[20], nodes[30])
    _assert_true(tree.root is nodes[30], "After transplanting root, new root should be node 30.")
    _assert_true(nodes[30].parent is tree.nil, "New root's parent should be tree.nil.")


def test_transplant_left_child():
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED), (30, RED), (5, BLACK)])
    transplant(tree, nodes[10], nodes[5])
    _assert_true(tree.root.left is nodes[5], "Left child of root should now be node 5.")
    _assert_true(nodes[5].parent is tree.root, "Node 5's parent should be root.")


def test_transplant_right_child():
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED), (30, RED), (35, BLACK)])
    transplant(tree, nodes[30], nodes[35])
    _assert_true(tree.root.right is nodes[35], "Right child of root should now be node 35.")
    _assert_true(nodes[35].parent is tree.root, "Node 35's parent should be root.")


def test_transplant_with_nil():
    tree = Tree()
    nodes = _make_tree_with_nodes(tree, [(20, BLACK), (10, RED), (30, RED)])
    transplant(tree, nodes[10], tree.nil)
    _assert_true(tree.root.left is tree.nil, "After transplant with nil, left should be nil.")


if __name__ == "__main__":
    TEST_CASES = [
        ("transplant root", test_transplant_root),
        ("transplant left child", test_transplant_left_child),
        ("transplant right child", test_transplant_right_child),
        ("transplant with nil", test_transplant_with_nil),
    ]
    _run_all_tests(TEST_CASES)
