# Level 7a - Equal trees
# Implement equals(a, b) - True iff both trees have the same shape and values.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 7a — Equal
#
# Implement `equals(a, b) -> bool`. Two trees are equal iff they have the same shape and the same values at corresponding positions. Two empty trees are equal.

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


def equals(a, b):
    raise NotImplementedError("Implement equals(a, b).")

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


def test_two_empty_trees_are_equal():
    _assert_equal(equals(None, None), True, "two empty trees should be equal.")


def test_empty_vs_non_empty():
    _assert_equal(equals(None, Node(1)), False, "empty tree should not equal non-empty.")
    _assert_equal(equals(Node(1), None), False, "non-empty tree should not equal empty.")


def test_same_shape_and_values():
    a = _make_level_order([1, 2, 3, 4, 5])
    b = _make_level_order([1, 2, 3, 4, 5])
    _assert_equal(equals(a, b), True, "structurally identical trees should be equal.")


def test_same_shape_different_values():
    a = _make_level_order([1, 2, 3])
    b = _make_level_order([1, 2, 4])
    _assert_equal(equals(a, b), False, "value mismatch should make trees unequal.")


def test_different_shape_same_values():
    a = _make_level_order([1, 2, None, 3])
    b = _make_level_order([1, None, 2, None, 3])
    _assert_equal(equals(a, b), False, "different shapes should make trees unequal.")


if __name__ == "__main__":
    TEST_CASES = [
        ("two empty trees are equal", test_two_empty_trees_are_equal),
        ("empty vs non-empty", test_empty_vs_non_empty),
        ("same shape and values", test_same_shape_and_values),
        ("same shape different values", test_same_shape_different_values),
        ("different shape same values", test_different_shape_same_values),
    ]
    _run_all_tests(TEST_CASES)
