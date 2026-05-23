# Level 11c - Deserialize
# Implement deserialize(data) as the inverse of serialize.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 11c — Deserialize
#
# Implement `deserialize(data) -> Node | None`, the inverse of `serialize` (11b).
# The string contains preorder tokens separated by commas. `#` represents a null child,
# so `#` is the empty tree and `7,#,#` is a single node `7`.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _equals(a, b):
    if a is None or b is None:
        return a is b
    return a.value == b.value and _equals(a.left, b.left) and _equals(a.right, b.right)


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


def deserialize(data):
    raise NotImplementedError("Implement deserialize(data).")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


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


def test_null_marker_deserializes_to_none():
    _assert_true(deserialize("#") is None, "null marker should deserialize to None.")


def test_single_node():
    expected = Node(7)
    _assert_true(_equals(deserialize("7,#,#"), expected), "single node should round-trip from tokens.")


def test_spec_shape_from_preorder_tokens():
    expected = _make_level_order([1, 2, 3, 4, 5])
    data = "1,2,4,#,#,5,#,#,3,#,#"
    _assert_true(_equals(deserialize(data), expected), "preorder tokens should rebuild the spec shape.")


def test_missing_left_child_is_preserved():
    expected = Node(1, right=Node(2))
    _assert_true(_equals(deserialize("1,#,2,#,#"), expected), "missing left child should be preserved.")


def test_negative_values():
    expected = Node(-1, Node(-2), Node(3))
    _assert_true(_equals(deserialize("-1,-2,#,#,3,#,#"), expected), "negative values should parse.")


if __name__ == "__main__":
    TEST_CASES = [
        ("null marker deserializes to None", test_null_marker_deserializes_to_none),
        ("single node", test_single_node),
        ("spec shape from preorder tokens", test_spec_shape_from_preorder_tokens),
        ("missing left child is preserved", test_missing_left_child_is_preserved),
        ("negative values", test_negative_values),
    ]
    _run_all_tests(TEST_CASES)
