# Level 11b - Serialize
# Implement serialize(root) encoding a tree as a string.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 11b — Serialize
#
# Implement `serialize(root) -> str`, encoding the tree as preorder tokens separated by commas.
# Use `#` for null children, so the empty tree is `#` and a single node `7` is `7,#,#`.
# `deserialize` (11c) must invert this same format.


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


def serialize(root):
    raise NotImplementedError("Implement serialize(root).")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_tree_serializes_as_null_marker():
    _assert_equal(serialize(None), "#", "empty tree should serialize to the null marker.")


def test_single_node():
    _assert_equal(serialize(Node(7)), "7,#,#", "single node should include both null children.")


def test_spec_shape_uses_preorder_tokens():
    root = _make_level_order([1, 2, 3, 4, 5])
    _assert_equal(
        serialize(root),
        "1,2,4,#,#,5,#,#,3,#,#",
        "tree should serialize in preorder with null markers.",
    )


def test_missing_left_child_is_preserved():
    root = Node(1, right=Node(2))
    _assert_equal(serialize(root), "1,#,2,#,#", "missing left child should be represented.")


def test_negative_values():
    root = Node(-1, Node(-2), Node(3))
    _assert_equal(serialize(root), "-1,-2,#,#,3,#,#", "negative values should serialize.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree serializes as null marker", test_empty_tree_serializes_as_null_marker),
        ("single node", test_single_node),
        ("spec shape uses preorder tokens", test_spec_shape_uses_preorder_tokens),
        ("missing left child is preserved", test_missing_left_child_is_preserved),
        ("negative values", test_negative_values),
    ]
    _run_all_tests(TEST_CASES)
