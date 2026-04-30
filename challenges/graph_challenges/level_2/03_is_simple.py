# Level 2c - Is Simple
# Return whether the input graph has no self-loops and no parallel edges.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 2c — `is_simple`
# Return whether the input graph (which may have been given carelessly) has no self-loops and no parallel edges.

def is_simple(adj):
    raise NotImplementedError('Implement is_simple(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_simple_graph():
    adj = [[1, 2], [0, 2], [0, 1]]  # triangle
    _assert_equal(is_simple(adj), True, "Triangle is simple.")


def test_02_self_loop():
    adj = [[0, 1], [0]]  # vertex 0 has self-loop
    _assert_equal(is_simple(adj), False, "Self-loop makes it not simple.")


def test_03_parallel_edges():
    adj = [[1, 1], [0, 0]]  # parallel edges between 0 and 1
    _assert_equal(is_simple(adj), False, "Parallel edges make it not simple.")


def test_04_empty_graph():
    adj = [[], [], []]
    _assert_equal(is_simple(adj), True, "Empty graph is simple.")


def test_05_single_node_no_loop():
    adj = [[]]
    _assert_equal(is_simple(adj), True, "Single node without self-loop is simple.")


def test_06_single_node_with_loop():
    adj = [[0]]
    _assert_equal(is_simple(adj), False, "Single node with self-loop is not simple.")


if __name__ == "__main__":
    TEST_CASES = [
        ("simple graph", test_01_simple_graph),
        ("self loop", test_02_self_loop),
        ("parallel edges", test_03_parallel_edges),
        ("empty graph", test_04_empty_graph),
        ("single node no loop", test_05_single_node_no_loop),
        ("single node with loop", test_06_single_node_with_loop),
    ]
    _run_all_tests(TEST_CASES)
