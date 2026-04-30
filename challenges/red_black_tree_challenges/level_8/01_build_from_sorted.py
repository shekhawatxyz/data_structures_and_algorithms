# Level 8a - Build from Sorted
# Build an optimal RBT from a sorted array in O(n).

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 8a. Build an optimal RBT from a sorted array in O(n)
#
# ```
# def build_from_sorted(keys: List[int]) -> Tree
# ```
#
# Given a sorted array of `n` keys, construct a valid RBT in O(n). The naive approach (insert one by one) is O(n log n). The trick is to build the tree recursively by midpoint partitioning — this gives a balanced BST. The wrinkle is *coloring* it: most levels can be all black, but the bottom (incomplete) level needs to be red so that black-heights match across all root-to-leaf paths.
#
# The key insight: if `n + 1` is a power of 2, the tree is perfectly complete and can be all black. Otherwise, the bottom level is incomplete; the lowest-level *real* nodes that sit above NIL leaves need to be red, so that paths through them have the same black count as paths that end one level higher.

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


def build_from_sorted(keys):
    raise NotImplementedError('Implement build_from_sorted(keys).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _is_valid_rbt(tree):
    """Minimal RBT verifier."""
    nil = tree.nil
    if tree.root is nil:
        return True
    if tree.root.color != BLACK:
        return False
    def _no_red_red(node):
        if node is nil:
            return True
        if node.color == RED:
            if node.left.color == RED or node.right.color == RED:
                return False
        return _no_red_red(node.left) and _no_red_red(node.right)
    if not _no_red_red(tree.root):
        return False
    def _check_bh(node):
        if node is nil:
            return 0
        l = _check_bh(node.left)
        r = _check_bh(node.right)
        if l == -1 or r == -1 or l != r:
            return -1
        return l + (1 if node.color == BLACK else 0)
    if _check_bh(tree.root) == -1:
        return False
    def _check_bst(node, lo, hi):
        if node is nil:
            return True
        if lo is not None and node.key <= lo:
            return False
        if hi is not None and node.key >= hi:
            return False
        return _check_bst(node.left, lo, node.key) and _check_bst(node.right, node.key, hi)
    return _check_bst(tree.root, None, None)


def test_build_empty():
    tree = build_from_sorted([])
    _assert_true(tree.root is tree.nil, "Empty input should give empty tree.")
    _assert_true(_is_valid_rbt(tree), "Empty tree is valid.")


def test_build_single():
    tree = build_from_sorted([10])
    _assert_true(_is_valid_rbt(tree), "Single-element tree should be valid.")
    _assert_equal(_inorder(tree), [10], "Inorder should be [10].")


def test_build_power_of_two_minus_one():
    keys = list(range(1, 8))  # 7 = 2^3 - 1
    tree = build_from_sorted(keys)
    _assert_true(_is_valid_rbt(tree), "Tree from 7 sorted keys should be valid.")
    _assert_equal(_inorder(tree), keys, "Inorder should match input.")


def test_build_non_power_of_two():
    keys = list(range(1, 11))  # 10 keys
    tree = build_from_sorted(keys)
    _assert_true(_is_valid_rbt(tree), "Tree from 10 sorted keys should be valid.")
    _assert_equal(_inorder(tree), keys, "Inorder should match input.")


def test_build_larger():
    keys = list(range(1, 101))  # 100 keys
    tree = build_from_sorted(keys)
    _assert_true(_is_valid_rbt(tree), "Tree from 100 sorted keys should be valid.")
    _assert_equal(_inorder(tree), keys, "Inorder should match input.")


if __name__ == "__main__":
    TEST_CASES = [
        ("build empty", test_build_empty),
        ("build single", test_build_single),
        ("build power-of-two-minus-one", test_build_power_of_two_minus_one),
        ("build non-power-of-two", test_build_non_power_of_two),
        ("build larger (100 keys)", test_build_larger),
    ]
    _run_all_tests(TEST_CASES)
