# Level 3b - Iterative inorder
# Implement inorder_iterative(root) using a stack instead of recursion.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 3b — Iterative inorder
#
# Implement `inorder_iterative(root) -> list`. The output must match `inorder` from 2b.

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


def inorder_iterative(root):
    raise NotImplementedError("Implement inorder_iterative(root).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    _assert_equal(inorder_iterative(None), [], "iterative inorder of empty tree should be [].")


def test_full_small_tree():
    tree = _make_level_order([1, 2, 3, 4, 5])
    _assert_equal(inorder_iterative(tree), [4, 2, 5, 1, 3],
                  "iterative inorder should match recursive inorder.")


def test_bst_inorder_is_sorted():
    tree = _make_level_order([4, 2, 6, 1, 3, 5, 7])
    _assert_equal(inorder_iterative(tree), [1, 2, 3, 4, 5, 6, 7],
                  "iterative inorder over a BST yields sorted values.")


def test_deep_left_chain():
    tree = _make_level_order([1, 2, None, 3, None, 4])
    _assert_equal(inorder_iterative(tree), [4, 3, 2, 1],
                  "iterative inorder unwinds a left chain in reverse.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree", test_empty_tree),
        ("full small tree", test_full_small_tree),
        ("BST inorder is sorted", test_bst_inorder_is_sorted),
        ("deep left chain", test_deep_left_chain),
    ]
    _run_all_tests(TEST_CASES)
