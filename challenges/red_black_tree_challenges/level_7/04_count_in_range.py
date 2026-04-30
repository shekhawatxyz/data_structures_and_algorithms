# Level 7d - Count in Range
# Count how many keys fall within [low, high] using the order-statistics tree.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 7d. Range count
#
# ```
# def count_in_range(tree, low, high) -> int
# ```
#
# How many keys are in `[low, high]`? Equivalent to `rank(predecessor_or_equal(high)) - rank(predecessor(low))` plus careful boundary handling, or a direct tree walk that prunes whole subtrees when their key range is fully outside `[low, high]`.

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


def count_in_range(tree, low, high):
    raise NotImplementedError('Implement count_in_range(tree, low, high).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_count_all_in_range():
    tree = _make_tree_with_sizes([(20, BLACK), (10, RED), (30, RED)])
    _assert_equal(count_in_range(tree, 1, 100), 3, "All 3 keys are in [1, 100].")


def test_count_none_in_range():
    tree = _make_tree_with_sizes([(20, BLACK), (10, RED), (30, RED)])
    _assert_equal(count_in_range(tree, 50, 100), 0, "No keys in [50, 100].")


def test_count_partial_range():
    # Keys: 10, 25, 30, 50, 60, 75, 90
    tree = _make_tree_with_sizes([
        (50, BLACK), (25, RED), (75, RED),
        (10, BLACK), (30, BLACK), (60, BLACK), (90, BLACK),
    ])
    _assert_equal(count_in_range(tree, 25, 60), 4, "Keys 25, 30, 50, 60 are in [25, 60].")


def test_count_single_key_range():
    tree = _make_tree_with_sizes([
        (50, BLACK), (25, RED), (75, RED),
        (10, BLACK), (30, BLACK), (60, BLACK), (90, BLACK),
    ])
    _assert_equal(count_in_range(tree, 50, 50), 1, "Exactly one key equals 50.")


def test_count_empty_tree():
    tree = Tree()
    _assert_equal(count_in_range(tree, 1, 100), 0, "Empty tree should have 0 in any range.")


if __name__ == "__main__":
    TEST_CASES = [
        ("count all in range", test_count_all_in_range),
        ("count none in range", test_count_none_in_range),
        ("count partial range", test_count_partial_range),
        ("count single key range", test_count_single_key_range),
        ("count empty tree", test_count_empty_tree),
    ]
    _run_all_tests(TEST_CASES)
