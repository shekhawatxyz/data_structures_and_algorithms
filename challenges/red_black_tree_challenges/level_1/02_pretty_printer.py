# Level 1b - Pretty Printer
# Render a red-black tree as a readable string with colors marked.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 1b. Pretty-printer
#
# ```
# def render(tree) -> str
# ```
#
# Render the tree in a way that lets you actually see what's going on, with colors marked. Indented format works well:
#
# ```
# 30B
# ├── 20B
# │   ├── 10R
# │   └── 25R
# └── 40B
# ```
#
# Or sideways with R/B suffixes. Whatever you build, build it well — you will stare at it for hours during the rest of these levels.

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


def render(tree):
    raise NotImplementedError('Implement render(tree).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_render_empty_tree():
    tree = Tree()
    result = render(tree)
    _assert_true(isinstance(result, str), "render should return a string.")


def test_render_single_node():
    tree = _make_simple_tree([(10, BLACK)])
    result = render(tree)
    _assert_true("10" in result, "Render should contain the key '10'.")
    _assert_true("B" in result, "Render should contain the color 'B'.")


def test_render_three_node_tree():
    tree = _make_simple_tree([(20, BLACK), (10, RED), (30, RED)])
    result = render(tree)
    _assert_true("20" in result, "Render should contain root key '20'.")
    _assert_true("10" in result, "Render should contain left key '10'.")
    _assert_true("30" in result, "Render should contain right key '30'.")


def test_render_shows_colors():
    tree = _make_simple_tree([(20, BLACK), (10, RED), (30, BLACK)])
    result = render(tree)
    _assert_true("R" in result, "Render should show red color.")
    _assert_true("B" in result, "Render should show black color.")


def test_render_returns_nonempty_for_nonempty_tree():
    tree = _make_simple_tree([(50, BLACK), (25, RED), (75, RED), (10, BLACK), (30, BLACK)])
    result = render(tree)
    _assert_true(len(result) > 0, "Render of non-empty tree should be non-empty.")


if __name__ == "__main__":
    TEST_CASES = [
        ("render empty tree", test_render_empty_tree),
        ("render single node", test_render_single_node),
        ("render three-node tree", test_render_three_node_tree),
        ("render shows colors", test_render_shows_colors),
        ("render non-empty for non-empty tree", test_render_returns_nonempty_for_nonempty_tree),
    ]
    _run_all_tests(TEST_CASES)
