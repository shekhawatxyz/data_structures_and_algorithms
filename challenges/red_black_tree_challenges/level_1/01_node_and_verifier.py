# Level 1a - Node and Property Verifier
# Check all 5 RBT properties plus the BST ordering property.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 1a. `Node` class and property verifier
#
# Define your `Node` class with: `key`, `color`, `parent`, `left`, `right`. Then write:
#
# ```
# def is_valid_red_black_tree(tree) -> bool
# ```
#
# It should check all five properties. Internally, you will need to compute the black-height — the number of black nodes on any simple path from a node to a descendant NIL, not counting the node itself. (Decide your own convention for whether NIL counts; just be consistent.) Property 5 is verified by checking that the black-height is the same on both subtrees of every node.
#
# The function should also implicitly verify the BST property (in-order key ordering), since an RBT is a BST plus the color invariants.
#
# Bonus version: `diagnose(tree) -> List[str]` that returns a list of which specific properties are violated. This is the more useful version for debugging later levels.

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


def is_valid_red_black_tree(tree):
    raise NotImplementedError('Implement is_valid_red_black_tree(tree).')
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
    for key, color in keys_colors:
        node = Node(key=key, color=color, left=tree.nil, right=tree.nil)
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
    return tree


def test_empty_tree_is_valid():
    tree = Tree()
    _assert_true(is_valid_red_black_tree(tree), "Empty tree should be valid.")


def test_single_black_root_valid():
    tree = _make_simple_tree([(10, BLACK)])
    _assert_true(is_valid_red_black_tree(tree), "Single black root should be valid.")


def test_valid_three_node_tree():
    tree = _make_simple_tree([(20, BLACK), (10, RED), (30, RED)])
    _assert_true(
        is_valid_red_black_tree(tree),
        "Black root with two red children should be valid.",
    )


def test_red_root_invalid():
    tree = _make_simple_tree([(10, RED)])
    _assert_true(
        not is_valid_red_black_tree(tree),
        "Red root should violate property 2.",
    )


def test_red_red_violation():
    tree = _make_simple_tree([(20, BLACK), (10, RED), (30, BLACK)])
    # Manually add a red child to the red node to create violation
    node5 = Node(key=5, color=RED, left=tree.nil, right=tree.nil)
    tree.root.left.left = node5
    node5.parent = tree.root.left
    _assert_true(
        not is_valid_red_black_tree(tree),
        "Red parent with red child should violate property 4.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty tree is valid", test_empty_tree_is_valid),
        ("single black root valid", test_single_black_root_valid),
        ("valid three-node tree", test_valid_three_node_tree),
        ("red root invalid", test_red_root_invalid),
        ("red-red violation", test_red_red_violation),
    ]
    _run_all_tests(TEST_CASES)
