# Level 2b - Min, Max, Successor, Predecessor
# Find minimum, maximum, successor, and predecessor nodes in a red-black tree.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 2b. Min, max, successor, predecessor
#
# ```
# def minimum(node) -> Node
# def maximum(node) -> Node
# def successor(node) -> Optional[Node]
# def predecessor(node) -> Optional[Node]
# ```
#
# These take a node, not a key. Successor uses the parent pointer when there is no right subtree.

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


def minimum(node):
    raise NotImplementedError('Implement minimum(node).')


def maximum(node):
    raise NotImplementedError('Implement maximum(node).')


def successor(node):
    raise NotImplementedError('Implement successor(node).')


def predecessor(node):
    raise NotImplementedError('Implement predecessor(node).')
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


def _make_simple_tree(keys_colors):
    """Build a minimal RBT for testing. keys_colors: list of (key, color)
    inserted manually in BST fashion."""
    tree = Tree()
    if not keys_colors:
        return tree
    nodes = {}
    for key, color in keys_colors:
        node = Node(key=key, color=color, left=tree.nil, right=tree.nil)
        nodes[key] = node
        if tree.root is tree.nil:
            tree.root = node
            node.parent = tree.nil
        else:
            current = tree.root
            while True:
                if key < current.key:
                    if current.left is tree.nil:
                        current.left = node
                        node.parent = current
                        break
                    current = current.left
                else:
                    if current.right is tree.nil:
                        current.right = node
                        node.parent = current
                        break
                    current = current.right
    return tree, nodes


def test_minimum_and_maximum():
    tree, nodes = _make_simple_tree([
        (20, BLACK), (10, RED), (30, RED), (5, BLACK), (15, BLACK),
    ])
    _assert_equal(minimum(tree.root).key, 5, "Minimum should be 5.")
    _assert_equal(maximum(tree.root).key, 30, "Maximum should be 30.")


def test_minimum_single_node():
    tree, nodes = _make_simple_tree([(42, BLACK)])
    _assert_equal(minimum(tree.root).key, 42, "Minimum of single node is itself.")
    _assert_equal(maximum(tree.root).key, 42, "Maximum of single node is itself.")


def test_successor_basic():
    tree, nodes = _make_simple_tree([
        (20, BLACK), (10, RED), (30, RED), (5, BLACK), (15, BLACK),
    ])
    _assert_equal(successor(nodes[10]).key, 15, "Successor of 10 should be 15.")
    _assert_equal(successor(nodes[15]).key, 20, "Successor of 15 should be 20.")
    _assert_equal(successor(nodes[20]).key, 30, "Successor of 20 should be 30.")


def test_predecessor_basic():
    tree, nodes = _make_simple_tree([
        (20, BLACK), (10, RED), (30, RED), (5, BLACK), (15, BLACK),
    ])
    _assert_equal(predecessor(nodes[20]).key, 15, "Predecessor of 20 should be 15.")
    _assert_equal(predecessor(nodes[15]).key, 10, "Predecessor of 15 should be 10.")
    _assert_equal(predecessor(nodes[10]).key, 5, "Predecessor of 10 should be 5.")


def test_successor_of_max_is_none():
    tree, nodes = _make_simple_tree([
        (20, BLACK), (10, RED), (30, RED),
    ])
    result = successor(nodes[30])
    _assert_true(
        result is None or result.key is None,
        "Successor of maximum should be None or sentinel.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("minimum and maximum", test_minimum_and_maximum),
        ("minimum/maximum single node", test_minimum_single_node),
        ("successor basic", test_successor_basic),
        ("predecessor basic", test_predecessor_basic),
        ("successor of max is None", test_successor_of_max_is_none),
    ]
    _run_all_tests(TEST_CASES)
