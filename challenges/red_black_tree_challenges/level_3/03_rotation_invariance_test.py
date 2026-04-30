# Level 3c - Rotation Invariance Test
# Verify that rotations preserve in-order traversal order.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 3c. In-order invariance test
#
# Write a test: take any tree, perform any sequence of rotations on any nodes, and confirm in-order traversal is unchanged. Rotations rearrange the tree but never the sorted order — this is the invariant that makes them safe. Build a property-based test that performs random valid rotations and verifies invariance.

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


def rotation_preserves_inorder(tree):
    raise NotImplementedError('Implement rotation_preserves_inorder(tree).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_rotation_preserves_inorder_small_tree():
    tree, _ = _make_simple_tree([(20, BLACK), (10, RED), (30, RED)])
    result = rotation_preserves_inorder(tree)
    _assert_true(result, "Rotations should preserve in-order on a small tree.")


def test_rotation_preserves_inorder_larger_tree():
    tree, _ = _make_simple_tree([
        (50, BLACK), (25, RED), (75, RED),
        (10, BLACK), (30, BLACK), (60, BLACK), (90, BLACK),
    ])
    result = rotation_preserves_inorder(tree)
    _assert_true(result, "Rotations should preserve in-order on a larger tree.")


def test_rotation_preserves_inorder_single_node():
    tree, _ = _make_simple_tree([(42, BLACK)])
    result = rotation_preserves_inorder(tree)
    _assert_true(result, "Single-node tree trivially preserved.")


def test_rotation_preserves_inorder_left_chain():
    tree, _ = _make_simple_tree([(30, BLACK), (20, RED), (10, BLACK)])
    result = rotation_preserves_inorder(tree)
    _assert_true(result, "Rotations should preserve in-order on left chain.")


if __name__ == "__main__":
    TEST_CASES = [
        ("rotation preserves inorder small tree", test_rotation_preserves_inorder_small_tree),
        ("rotation preserves inorder larger tree", test_rotation_preserves_inorder_larger_tree),
        ("rotation preserves inorder single node", test_rotation_preserves_inorder_single_node),
        ("rotation preserves inorder left chain", test_rotation_preserves_inorder_left_chain),
    ]
    _run_all_tests(TEST_CASES)
