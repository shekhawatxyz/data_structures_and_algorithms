# Level 7b - Select
# Find the i-th smallest element in the order-statistics tree.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 7b. `select(i)` — find the i-th smallest
#
# ```
# def select(tree, i) -> Node
# ```
#
# In O(log n). Walk down from the root: at each node, the rank of the node within its subtree is `node.left.size + 1`. If `i` matches, return; if `i` is smaller, go left; otherwise go right with `i` decreased by `node.left.size + 1`.

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


def select(tree, i):
    raise NotImplementedError('Implement select(tree, i).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    def _fix_size(node):
        if node is tree.nil:
            return 0
        left_size = _fix_size(node.left)
        right_size = _fix_size(node.right)
        node.size = left_size + right_size + 1
        return node.size
    _fix_size(tree.root)
    return tree


def test_select_first():
    tree = _make_tree_with_sizes([(20, BLACK), (10, RED), (30, RED)])
    result = select(tree, 1)
    _assert_equal(result.key, 10, "1st smallest should be 10.")


def test_select_last():
    tree = _make_tree_with_sizes([(20, BLACK), (10, RED), (30, RED)])
    result = select(tree, 3)
    _assert_equal(result.key, 30, "3rd smallest should be 30.")


def test_select_middle():
    tree = _make_tree_with_sizes([(20, BLACK), (10, RED), (30, RED)])
    result = select(tree, 2)
    _assert_equal(result.key, 20, "2nd smallest should be 20.")


def test_select_in_larger_tree():
    tree = _make_tree_with_sizes([
        (50, BLACK), (25, RED), (75, RED),
        (10, BLACK), (30, BLACK), (60, BLACK), (90, BLACK),
    ])
    # Sorted: 10, 25, 30, 50, 60, 75, 90
    _assert_equal(select(tree, 1).key, 10, "1st should be 10.")
    _assert_equal(select(tree, 4).key, 50, "4th should be 50.")
    _assert_equal(select(tree, 7).key, 90, "7th should be 90.")


def test_select_single_node():
    tree = _make_tree_with_sizes([(42, BLACK)])
    result = select(tree, 1)
    _assert_equal(result.key, 42, "Only element should be selectable at rank 1.")


if __name__ == "__main__":
    TEST_CASES = [
        ("select first", test_select_first),
        ("select last", test_select_last),
        ("select middle", test_select_middle),
        ("select in larger tree", test_select_in_larger_tree),
        ("select single node", test_select_single_node),
    ]
    _run_all_tests(TEST_CASES)
