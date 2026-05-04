# Level 1a - Node class
# Implement a Node class with `value`, `left`, `right` and a `from_nested` classmethod.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 1a — Node class
#
# Implement a `Node` class with attributes `value`, `left`, `right`, where `left` and `right` are either `None` or another `Node`. Provide a classmethod `Node.from_nested(spec)` that builds a tree from nested tuples of the form `(value, left_subtree, right_subtree)`, where each subtree is either `None` or another such tuple.
#
# ```
# Node.from_nested((1, (2, None, None), (3, None, None)))
# #       1
# #      / \
# #     2   3
# ```
#
# `Node.from_nested(None)` returns `None`.

class Node:
    value: object
    left: "Node | None"
    right: "Node | None"

    def __init__(self, value, left=None, right=None):
        raise NotImplementedError("Implement Node.__init__(value, left, right).")

    @classmethod
    def from_nested(cls, spec):
        raise NotImplementedError("Implement Node.from_nested(spec).")

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


def test_single_node_attributes():
    node = Node(5)
    _assert_equal(node.value, 5, "single node should expose value attribute.")
    _assert_true(node.left is None, "single node should have no left child.")
    _assert_true(node.right is None, "single node should have no right child.")


def test_from_nested_builds_tree():
    tree = Node.from_nested((1, (2, None, None), (3, None, None)))
    _assert_equal(tree.value, 1, "root value should match spec.")
    _assert_equal(tree.left.value, 2, "left child value should match spec.")
    _assert_equal(tree.right.value, 3, "right child value should match spec.")
    _assert_true(tree.left.left is None and tree.left.right is None,
                 "leaf nodes should have no children.")
    _assert_true(tree.right.left is None and tree.right.right is None,
                 "leaf nodes should have no children.")


def test_from_nested_deeper_tree():
    tree = Node.from_nested((1, (2, (4, None, None), None), (3, None, (5, None, None))))
    _assert_equal(tree.left.left.value, 4, "deep left grandchild should match spec.")
    _assert_equal(tree.right.right.value, 5, "deep right grandchild should match spec.")
    _assert_true(tree.left.right is None, "missing children stay None.")
    _assert_true(tree.right.left is None, "missing children stay None.")


def test_from_nested_none_returns_none():
    _assert_true(Node.from_nested(None) is None, "from_nested(None) should return None.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single node attributes", test_single_node_attributes),
        ("from_nested builds tree", test_from_nested_builds_tree),
        ("from_nested deeper tree", test_from_nested_deeper_tree),
        ("from_nested(None) returns None", test_from_nested_none_returns_none),
    ]
    _run_all_tests(TEST_CASES)
