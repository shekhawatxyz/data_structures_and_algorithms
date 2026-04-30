# Level 6e - Mixed Stress Test
# Randomized insert/delete sequences with verification after each operation.

# Complete Exact Problem Statement (from red-black-tree-challenges.md):
# ### 6e. Mixed insert/delete stress test
#
# Run a randomized sequence of inserts and deletes of length 10,000, each from a small key universe (say 1..1000) so deletes hit. After each operation, assert:
# - Verifier passes.
# - In-order traversal matches the multiset (or set) of keys you've tracked separately.
#
# When something breaks, the trace + your renderer is your debugging path.

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


def insert_delete_verify(tree, operations):
    raise NotImplementedError('Implement insert_delete_verify(tree, operations).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_simple_insert_delete_sequence():
    tree = Tree()
    ops = [("insert", 10), ("insert", 20), ("insert", 30), ("delete", 20)]
    insert_delete_verify(tree, ops)


def test_delete_nonexistent_key():
    tree = Tree()
    ops = [("insert", 5), ("delete", 99), ("insert", 10)]
    insert_delete_verify(tree, ops)


def test_insert_delete_same_key():
    tree = Tree()
    ops = [("insert", 42), ("delete", 42)]
    insert_delete_verify(tree, ops)


def test_mixed_50_operations():
    import random
    random.seed(7)
    ops = []
    for _ in range(50):
        if random.random() < 0.6:
            ops.append(("insert", random.randint(1, 30)))
        else:
            ops.append(("delete", random.randint(1, 30)))
    tree = Tree()
    insert_delete_verify(tree, ops)


def test_all_inserts_then_all_deletes():
    tree = Tree()
    keys = [15, 3, 27, 8, 42, 1, 19]
    ops = [("insert", k) for k in keys] + [("delete", k) for k in keys]
    insert_delete_verify(tree, ops)


if __name__ == "__main__":
    TEST_CASES = [
        ("simple insert/delete sequence", test_simple_insert_delete_sequence),
        ("delete nonexistent key", test_delete_nonexistent_key),
        ("insert/delete same key", test_insert_delete_same_key),
        ("mixed 50 operations", test_mixed_50_operations),
        ("all inserts then all deletes", test_all_inserts_then_all_deletes),
    ]
    _run_all_tests(TEST_CASES)
