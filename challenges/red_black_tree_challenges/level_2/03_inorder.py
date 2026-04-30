# Level 2c - In-order Traversal
# Return a list of keys from an in-order traversal of the red-black tree.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 2c. In-order traversal
#
# ```
# def inorder(tree) -> List[key]
# ```
#
# Verify the result is sorted on every tree you have. This will be your sanity check after every rotation, insert, and delete.

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


def inorder(tree):
    raise NotImplementedError('Implement inorder(tree).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    if not keys_colors:
        return tree
    for key, color in keys_colors:
        node = Node(key=key, color=color, left=tree.nil, right=tree.nil)
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
    return tree


def test_inorder_empty_tree():
    tree = Tree()
    _assert_equal(inorder(tree), [], "In-order of empty tree should be [].")


def test_inorder_single_node():
    tree = _make_simple_tree([(10, BLACK)])
    _assert_equal(inorder(tree), [10], "In-order of single node should be [10].")


def test_inorder_three_nodes():
    tree = _make_simple_tree([(20, BLACK), (10, RED), (30, RED)])
    _assert_equal(inorder(tree), [10, 20, 30], "In-order should be [10, 20, 30].")


def test_inorder_is_sorted():
    tree = _make_simple_tree([
        (50, BLACK), (25, RED), (75, RED),
        (10, BLACK), (30, BLACK), (60, BLACK), (90, BLACK),
    ])
    result = inorder(tree)
    _assert_equal(result, sorted(result), "In-order traversal should produce sorted keys.")


def test_inorder_left_only_chain():
    tree = _make_simple_tree([(30, BLACK), (20, RED), (10, BLACK)])
    # Note: left-only chain shape depends on BST insertion order
    result = inorder(tree)
    _assert_equal(result, [10, 20, 30], "In-order of left chain should be sorted.")


if __name__ == "__main__":
    TEST_CASES = [
        ("inorder empty tree", test_inorder_empty_tree),
        ("inorder single node", test_inorder_single_node),
        ("inorder three nodes", test_inorder_three_nodes),
        ("inorder is sorted", test_inorder_is_sorted),
        ("inorder left-only chain", test_inorder_left_only_chain),
    ]
    _run_all_tests(TEST_CASES)
