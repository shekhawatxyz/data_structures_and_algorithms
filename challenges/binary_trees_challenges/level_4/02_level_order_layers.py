# Level 4b - Level-order by layer
# Implement level_order_layers(root) returning a list of layers.

# Complete Exact Problem Statement (from binary-tree-challenges.md):
# ### 4b — Level-order by layer
#
# Implement `level_order_layers(root) -> list[list]` where each inner list is one layer, top-to-bottom.
#
# ```
# level_order_layers(from_level_order([1, 2, 3, 4, None, 5]))
# # [[1], [2, 3], [4, 5]]
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


def level_order_layers(root):
    raise NotImplementedError("Implement level_order_layers(root).")

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
    _assert_equal(level_order_layers(None), [], "empty tree should produce no layers.")


def test_single_node():
    _assert_equal(level_order_layers(Node(7)), [[7]],
                  "single node should produce one layer with one value.")


def test_three_layers():
    tree = _make_level_order([1, 2, 3, 4, None, 5])
    _assert_equal(level_order_layers(tree), [[1], [2, 3], [4, 5]],
                  "layers should match the level-order grouping.")


def test_left_skew_layers():
    tree = _make_level_order([1, 2, None, 3])
    _assert_equal(level_order_layers(tree), [[1], [2], [3]],
                  "skewed tree should produce one value per layer.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree", test_empty_tree),
        ("single node", test_single_node),
        ("three layers", test_three_layers),
        ("left-skew layers", test_left_skew_layers),
    ]
    _run_all_tests(TEST_CASES)
