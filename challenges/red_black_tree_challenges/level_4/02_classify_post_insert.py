# Level 4b - Classify Post-Insert
# Classify the tree state after a naive insert as valid, red_root, or red_red.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 4b. Identify the violation
#
# Given the inserted red node `z` from 4a, write a function that classifies the tree state:
#
# ```
# def classify_post_insert(tree, z) -> str
# ```
#
# Returns one of: `"valid"`, `"red_root"`, `"red_red"`. The `"red_red"` case is the one that needs fix-up; if the parent is black or `z` is the root, you handle those trivially.
#
# This is just an exercise in being precise about the case structure before writing fix-up code.

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


def classify_post_insert(tree, z):
    raise NotImplementedError('Implement classify_post_insert(tree, z).')
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


def test_classify_red_root():
    tree = Tree()
    z = Node(key=10, color=RED, left=tree.nil, right=tree.nil)
    tree.root = z
    z.parent = tree.nil
    _assert_equal(classify_post_insert(tree, z), "red_root", "Red root should be classified as red_root.")


def test_classify_valid_black_parent():
    tree = Tree()
    root = Node(key=20, color=BLACK, left=tree.nil, right=tree.nil)
    tree.root = root
    root.parent = tree.nil
    z = Node(key=10, color=RED, left=tree.nil, right=tree.nil)
    root.left = z
    z.parent = root
    _assert_equal(classify_post_insert(tree, z), "valid", "Red child of black parent should be valid.")


def test_classify_red_red():
    tree = Tree()
    root = Node(key=30, color=BLACK, left=tree.nil, right=tree.nil)
    tree.root = root
    root.parent = tree.nil
    parent = Node(key=20, color=RED, left=tree.nil, right=tree.nil)
    root.left = parent
    parent.parent = root
    z = Node(key=10, color=RED, left=tree.nil, right=tree.nil)
    parent.left = z
    z.parent = parent
    _assert_equal(classify_post_insert(tree, z), "red_red", "Red child of red parent should be red_red.")


def test_classify_valid_after_proper_insert():
    tree = Tree()
    root = Node(key=20, color=BLACK, left=tree.nil, right=tree.nil)
    tree.root = root
    root.parent = tree.nil
    left = Node(key=10, color=BLACK, left=tree.nil, right=tree.nil)
    right = Node(key=30, color=BLACK, left=tree.nil, right=tree.nil)
    root.left = left
    root.right = right
    left.parent = root
    right.parent = root
    z = Node(key=5, color=RED, left=tree.nil, right=tree.nil)
    left.left = z
    z.parent = left
    _assert_equal(classify_post_insert(tree, z), "valid", "Red child of black parent should be valid.")


if __name__ == "__main__":
    TEST_CASES = [
        ("classify red root", test_classify_red_root),
        ("classify valid (black parent)", test_classify_valid_black_parent),
        ("classify red-red", test_classify_red_red),
        ("classify valid after proper insert", test_classify_valid_after_proper_insert),
    ]
    _run_all_tests(TEST_CASES)
