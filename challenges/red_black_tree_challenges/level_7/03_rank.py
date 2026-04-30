# Level 7c - Rank
# Find the rank (1-indexed position in sorted order) of a given node.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 7c. `rank(x)` — find the rank of node x
#
# ```
# def rank(tree, x) -> int
# ```
#
# In O(log n). Start with rank `x.left.size + 1`. Walk up to root: every time you came up from a right child, add `parent.left.size + 1` to the rank.

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


def rank(tree, x):
    raise NotImplementedError('Implement rank(tree, x).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    """Build a tree with correct sizes, return (tree, nodes_dict)."""
    tree = Tree()
    nodes = {}
    if not keys_colors:
        return tree, nodes
    for key, color in keys_colors:
        node = Node(key=key, color=color, left=tree.nil, right=tree.nil)
        node.size = 1
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
    def _fix_size(node):
        if node is tree.nil:
            return 0
        left_size = _fix_size(node.left)
        right_size = _fix_size(node.right)
        node.size = left_size + right_size + 1
        return node.size
    _fix_size(tree.root)
    return tree, nodes


def test_rank_of_root():
    tree, nodes = _make_tree_with_sizes([(20, BLACK), (10, RED), (30, RED)])
    _assert_equal(rank(tree, nodes[20]), 2, "Root 20 should have rank 2.")


def test_rank_of_minimum():
    tree, nodes = _make_tree_with_sizes([(20, BLACK), (10, RED), (30, RED)])
    _assert_equal(rank(tree, nodes[10]), 1, "Minimum 10 should have rank 1.")


def test_rank_of_maximum():
    tree, nodes = _make_tree_with_sizes([(20, BLACK), (10, RED), (30, RED)])
    _assert_equal(rank(tree, nodes[30]), 3, "Maximum 30 should have rank 3.")


def test_rank_in_larger_tree():
    tree, nodes = _make_tree_with_sizes([
        (50, BLACK), (25, RED), (75, RED),
        (10, BLACK), (30, BLACK), (60, BLACK), (90, BLACK),
    ])
    # Sorted: 10, 25, 30, 50, 60, 75, 90
    _assert_equal(rank(tree, nodes[10]), 1, "10 should have rank 1.")
    _assert_equal(rank(tree, nodes[50]), 4, "50 should have rank 4.")
    _assert_equal(rank(tree, nodes[90]), 7, "90 should have rank 7.")


def test_rank_single_node():
    tree, nodes = _make_tree_with_sizes([(42, BLACK)])
    _assert_equal(rank(tree, nodes[42]), 1, "Single node should have rank 1.")


if __name__ == "__main__":
    TEST_CASES = [
        ("rank of root", test_rank_of_root),
        ("rank of minimum", test_rank_of_minimum),
        ("rank of maximum", test_rank_of_maximum),
        ("rank in larger tree", test_rank_in_larger_tree),
        ("rank single node", test_rank_single_node),
    ]
    _run_all_tests(TEST_CASES)
