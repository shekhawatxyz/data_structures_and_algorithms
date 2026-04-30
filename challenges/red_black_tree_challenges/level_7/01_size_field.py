# Level 7a - Size Field
# Verify that the size augmentation field is consistent across the tree.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 7a. Add `size` field; maintain it
#
# Add `size` to your `Node`: the number of nodes in the subtree rooted at that node. NIL has size 0.
#
# Update insert, delete, left rotate, and right rotate to maintain `size` correctly. Rotation only changes the size of two nodes — the one rotated over and its replacement. Insert and delete update sizes along the path from the affected leaf up to the root.
#
# Write a verifier:
#
# ```
# def is_size_consistent(tree) -> bool
# ```
#
# That recomputes sizes from scratch and compares them to the stored values. Run after every insert and delete in a stress test.

RED = "R"
BLACK = "B"


class Node:
    def __init__(self, key, color=RED, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right
        self.size = 1


class Tree:
    def __init__(self):
        self.nil = Node(key=None, color=BLACK)
        self.nil.size = 0
        self.root = self.nil


def is_size_consistent(tree):
    raise NotImplementedError('Implement is_size_consistent(tree).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _make_tree_with_sizes(keys_colors):
    """Build a tree with correct sizes."""
    tree = Tree()
    if not keys_colors:
        return tree
    for key, color in keys_colors:
        node = Node(key=key, color=color, left=tree.nil, right=tree.nil)
        node.size = 1
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
    # Fix sizes bottom-up
    def _fix_size(node):
        if node is tree.nil:
            return 0
        left_size = _fix_size(node.left)
        right_size = _fix_size(node.right)
        node.size = left_size + right_size + 1
        return node.size
    _fix_size(tree.root)
    return tree


def test_empty_tree_consistent():
    tree = Tree()
    _assert_true(is_size_consistent(tree), "Empty tree should be size-consistent.")


def test_single_node_consistent():
    tree = _make_tree_with_sizes([(10, BLACK)])
    _assert_true(is_size_consistent(tree), "Single node tree should be size-consistent.")


def test_three_node_consistent():
    tree = _make_tree_with_sizes([(20, BLACK), (10, RED), (30, RED)])
    _assert_true(is_size_consistent(tree), "Three-node tree should be size-consistent.")


def test_incorrect_size_detected():
    tree = _make_tree_with_sizes([(20, BLACK), (10, RED), (30, RED)])
    tree.root.size = 99  # Wrong!
    _assert_true(not is_size_consistent(tree), "Incorrect root size should be detected.")


def test_larger_tree_consistent():
    tree = _make_tree_with_sizes([
        (50, BLACK), (25, RED), (75, RED),
        (10, BLACK), (30, BLACK), (60, BLACK), (90, BLACK),
    ])
    _assert_true(is_size_consistent(tree), "Seven-node tree should be size-consistent.")
    _assert_equal(tree.root.size, 7, "Root size should be 7.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree consistent", test_empty_tree_consistent),
        ("single node consistent", test_single_node_consistent),
        ("three-node consistent", test_three_node_consistent),
        ("incorrect size detected", test_incorrect_size_detected),
        ("larger tree consistent", test_larger_tree_consistent),
    ]
    _run_all_tests(TEST_CASES)
