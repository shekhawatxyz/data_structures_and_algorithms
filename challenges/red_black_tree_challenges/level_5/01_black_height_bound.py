# Level 5a - Black Height Bound
# Compute black-height and tree height; verify the logarithmic bound empirically.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 5a. Black-height bound
#
# After 5a inserts of n random keys, plot or print:
# - Tree height (longest root-to-leaf simple path, counting nodes).
# - Black-height of the root.
# - The bound `2 * log2(n + 1)`.
#
# The height should always be at most `2 * bh(root)`, and `bh(root)` should be at most `log2(n + 1)`. Convince yourself empirically that `height ≤ 2 * log2(n + 1)`.

import math

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


def black_height(tree):
    raise NotImplementedError('Implement black_height(tree).')


def tree_height(tree):
    raise NotImplementedError('Implement tree_height(tree).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    """Build a minimal RBT for testing."""
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


def test_empty_tree_heights():
    tree = Tree()
    _assert_equal(black_height(tree), 0, "Empty tree black-height should be 0.")
    _assert_equal(tree_height(tree), 0, "Empty tree height should be 0.")


def test_single_node_heights():
    tree = _make_simple_tree([(10, BLACK)])
    bh = black_height(tree)
    th = tree_height(tree)
    _assert_equal(bh, 1, "Single black node: black-height should be 1.")
    _assert_equal(th, 1, "Single node: tree height should be 1.")


def test_three_node_heights():
    tree = _make_simple_tree([(20, BLACK), (10, RED), (30, RED)])
    bh = black_height(tree)
    th = tree_height(tree)
    _assert_equal(bh, 1, "Black root with two red children: bh should be 1.")
    _assert_equal(th, 2, "Three-node tree height should be 2.")


def test_height_bound_holds():
    # Build a known valid tree and check the bound
    tree = _make_simple_tree([
        (50, BLACK), (25, BLACK), (75, BLACK),
        (10, RED), (30, RED), (60, RED), (90, RED),
    ])
    n = 7
    bh = black_height(tree)
    th = tree_height(tree)
    bound = 2 * math.log2(n + 1)
    _assert_true(th <= bound, f"Height {th} should be <= 2*log2({n}+1)={bound:.2f}.")
    _assert_true(th <= 2 * bh, f"Height {th} should be <= 2*bh={2*bh}.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree heights", test_empty_tree_heights),
        ("single node heights", test_single_node_heights),
        ("three-node heights", test_three_node_heights),
        ("height bound holds", test_height_bound_holds),
    ]
    _run_all_tests(TEST_CASES)
