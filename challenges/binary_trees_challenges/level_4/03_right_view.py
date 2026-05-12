# Level 4c - Right view
# Implement right_view(root) returning the rightmost value at each level.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 4c — Right view
#
# Implement `right_view(root) -> list` returning the rightmost value at each level, top-to-bottom. For an empty tree, return `[]`.
#
# ```
# right_view(from_level_order([1, 2, 3, None, 4, None, None]))
# # [1, 3, 4]
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


def right_view(root):
    raise NotImplementedError("Implement right_view(root).")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    _assert_equal(right_view(None), [], "right-view of empty tree should be [].")


def test_single_node():
    _assert_equal(right_view(Node(7)), [7], "right-view of single node should be [value].")


def test_spec_example():
    tree = _make_level_order([1, 2, 3, None, 4, None, None])
    _assert_equal(right_view(tree), [1, 3, 4],
                  "right-view should pick rightmost node visible from the right.")


def test_left_skew_visible_through_right():
    tree = _make_level_order([1, 2, None, 3])
    _assert_equal(right_view(tree), [1, 2, 3],
                  "with no right children, every level's only node is the rightmost.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree", test_empty_tree),
        ("single node", test_single_node),
        ("spec example", test_spec_example),
        ("left-skew visible through right", test_left_skew_visible_through_right),
    ]
    _run_all_tests(TEST_CASES)
