# Level 4f - Insertion Stress Test
# Insert many keys and verify validity after each insertion.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 4f. Insertion stress test
#
# Write a test that inserts a random sequence of N keys (try N = 100, 1000, 10000) and asserts after each insert that:
# - The verifier from 1a passes.
# - In-order traversal returns the sorted sequence of keys inserted so far.
#
# If anything fails, your `render` from 1b should be your first stop.

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


def insert_and_verify(tree, key):
    raise NotImplementedError('Implement insert_and_verify(tree, key).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _inorder(tree):
    result = []

    def walk(node):
        if node is tree.nil:
            return
        walk(node.left)
        result.append(node.key)
        walk(node.right)

    walk(tree.root)
    return result


def _insert_keys_and_check(keys):
    tree = Tree()
    inserted = []
    for k in keys:
        insert_and_verify(tree, k)
        inserted.append(k)
        _assert_equal(_inorder(tree), sorted(inserted),
                      f"in-order traversal should match inserted keys after inserting {k}.")


def test_stress_10_keys():
    import random
    random.seed(42)
    keys = random.sample(range(1, 100), 10)
    _insert_keys_and_check(keys)


def test_stress_100_keys():
    import random
    random.seed(123)
    keys = random.sample(range(1, 1000), 100)
    _insert_keys_and_check(keys)


def test_stress_ascending():
    _insert_keys_and_check(range(1, 51))


def test_stress_descending():
    _insert_keys_and_check(range(50, 0, -1))


if __name__ == "__main__":
    TEST_CASES = [
        ("stress 10 random keys", test_stress_10_keys),
        ("stress 100 random keys", test_stress_100_keys),
        ("stress 50 ascending keys", test_stress_ascending),
        ("stress 50 descending keys", test_stress_descending),
    ]
    _run_all_tests(TEST_CASES)
