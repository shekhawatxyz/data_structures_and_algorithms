# Level 3a - Iterative preorder
# Implement preorder_iterative(root) using a stack instead of recursion.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 3a — Iterative preorder
#
# Implement `preorder_iterative(root) -> list`. The output must match `preorder` from 2a.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _make_level_order(values):
    if not values:
        return None
    root = Node(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    return root


def preorder_iterative(root):
    raise NotImplementedError("Implement preorder_iterative(root).")

#
#
#
#
#


def _assert_equal(actual, expected, context):
    if actual != expected:
        raise AssertionError(f"{context} Expected {expected!r}, got {actual!r}.")


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
    for name, fn in test_cases:
        if _run_test(name, fn):
            passed += 1
    print(f"\nPassed {passed}/{len(test_cases)} tests.")
    if passed != len(test_cases):
        raise SystemExit(1)


def test_empty_tree():
    _assert_equal(preorder_iterative(None), [], "iterative preorder of empty tree should be [].")


def test_full_small_tree():
    tree = _make_level_order([1, 2, 3, 4, 5])
    _assert_equal(preorder_iterative(tree), [1, 2, 4, 5, 3],
                  "iterative preorder should match recursive preorder.")


def test_left_skewed_tree():
    tree = _make_level_order([1, 2, None, 3, None, 4])
    _assert_equal(preorder_iterative(tree), [1, 2, 3, 4],
                  "iterative preorder follows left chain on a left-skewed tree.")


def test_right_skewed_tree():
    tree = _make_level_order([1, None, 2, None, None, None, 3])
    _assert_equal(preorder_iterative(tree), [1, 2, 3],
                  "iterative preorder follows right chain on a right-skewed tree.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree", test_empty_tree),
        ("full small tree", test_full_small_tree),
        ("left-skewed tree", test_left_skewed_tree),
        ("right-skewed tree", test_right_skewed_tree),
    ]
    _run_all_tests(TEST_CASES)
