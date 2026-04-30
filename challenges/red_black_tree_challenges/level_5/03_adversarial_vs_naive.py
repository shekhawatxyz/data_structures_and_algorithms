# Level 5c - Adversarial vs Naive BST
# Compare RBT height against naive BST height on adversarial (sorted) input.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 5c. Adversarial input vs naive BST
#
# Insert keys `1, 2, 3, ..., n` into:
# - A naive BST.
# - Your RBT.
#
# Print the height of each. The BST will be `n`. The RBT will be roughly `2 log n`. This is the visible payoff of the balancing.

import math

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


def naive_bst_height(keys):
    raise NotImplementedError('Implement naive_bst_height(keys).')
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


def test_naive_bst_ascending_gives_linear_height():
    keys = list(range(1, 101))
    h = naive_bst_height(keys)
    _assert_equal(h, 100, "Naive BST on 1..100 ascending should have height 100.")


def test_naive_bst_single_key():
    h = naive_bst_height([42])
    _assert_equal(h, 1, "Single key BST should have height 1.")


def test_naive_bst_empty():
    h = naive_bst_height([])
    _assert_equal(h, 0, "Empty key list should give height 0.")


def test_naive_bst_balanced_input():
    # Inserting in balanced order gives log height
    keys = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    h = naive_bst_height(keys)
    _assert_equal(h, 4, "Balanced insertion of 15 keys should give height 4.")


def test_naive_bst_descending():
    keys = list(range(50, 0, -1))
    h = naive_bst_height(keys)
    _assert_equal(h, 50, "Naive BST on 50..1 descending should have height 50.")


if __name__ == "__main__":
    TEST_CASES = [
        ("naive BST ascending gives linear height", test_naive_bst_ascending_gives_linear_height),
        ("naive BST single key", test_naive_bst_single_key),
        ("naive BST empty", test_naive_bst_empty),
        ("naive BST balanced input", test_naive_bst_balanced_input),
        ("naive BST descending", test_naive_bst_descending),
    ]
    _run_all_tests(TEST_CASES)
