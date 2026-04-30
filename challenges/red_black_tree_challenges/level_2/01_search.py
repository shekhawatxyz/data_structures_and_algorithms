# Level 2a - Search
# Search for a key in a red-black tree, returning the node or None.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 2a. Search
#
# ```
# def search(tree, key) -> Optional[Node]
# ```
#
# Iterative version preferred.

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


def search(tree, key):
    raise NotImplementedError('Implement search(tree, key).')
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


def test_search_empty_tree():
    tree = Tree()
    result = search(tree, 10)
    _assert_true(result is None, "Search in empty tree should return None.")


def test_search_finds_root():
    tree = _make_simple_tree([(20, BLACK)])
    result = search(tree, 20)
    _assert_true(result is not None, "Should find key 20.")
    _assert_equal(result.key, 20, "Found node should have key 20.")


def test_search_finds_leaf():
    tree = _make_simple_tree([(20, BLACK), (10, RED), (30, RED)])
    result = search(tree, 30)
    _assert_true(result is not None, "Should find key 30.")
    _assert_equal(result.key, 30, "Found node should have key 30.")


def test_search_not_found():
    tree = _make_simple_tree([(20, BLACK), (10, RED), (30, RED)])
    result = search(tree, 25)
    _assert_true(result is None, "Key 25 not in tree; should return None.")


def test_search_in_larger_tree():
    tree = _make_simple_tree([
        (50, BLACK), (25, RED), (75, RED),
        (10, BLACK), (30, BLACK), (60, BLACK), (90, BLACK),
    ])
    for key in [50, 25, 75, 10, 30, 60, 90]:
        result = search(tree, key)
        _assert_true(result is not None, f"Should find key {key}.")
        _assert_equal(result.key, key, f"Found node should have key {key}.")
    _assert_true(search(tree, 99) is None, "Key 99 not in tree; should return None.")


if __name__ == "__main__":
    TEST_CASES = [
        ("search empty tree", test_search_empty_tree),
        ("search finds root", test_search_finds_root),
        ("search finds leaf", test_search_finds_leaf),
        ("search not found", test_search_not_found),
        ("search in larger tree", test_search_in_larger_tree),
    ]
    _run_all_tests(TEST_CASES)
