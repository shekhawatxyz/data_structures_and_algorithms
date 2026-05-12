# Level 4a - Level-order flat
# Implement level_order(root) returning all values in BFS order using a queue.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 4a — Level-order flat
#
# Implement `level_order(root) -> list` that returns all values in BFS order (top-to-bottom, left-to-right within each level). For an empty tree, return `[]`.
#
# ```
# level_order(from_level_order([1, 2, 3, 4, None, 5]))   # [1, 2, 3, 4, 5]
# ```

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


def level_order(root):
    raise NotImplementedError("Implement level_order(root).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    _assert_equal(level_order(None), [], "level-order of empty tree should be [].")


def test_single_node():
    _assert_equal(level_order(Node(7)), [7], "level-order of single node should be [value].")


def test_full_small_tree():
    tree = _make_level_order([1, 2, 3, 4, None, 5])
    _assert_equal(level_order(tree), [1, 2, 3, 4, 5],
                  "level-order should visit each level top-to-bottom, left-to-right.")


def test_skewed_tree():
    tree = _make_level_order([1, 2, None, 3])
    _assert_equal(level_order(tree), [1, 2, 3],
                  "level-order should descend through skewed tree level by level.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree", test_empty_tree),
        ("single node", test_single_node),
        ("full small tree", test_full_small_tree),
        ("skewed tree", test_skewed_tree),
    ]
    _run_all_tests(TEST_CASES)
