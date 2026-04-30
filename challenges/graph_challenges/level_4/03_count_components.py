# Level 4c - Count Components
# Return the number of connected components in an undirected graph.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 4c — `count_components`
# Number of connected components in an undirected graph. Repeated DFS from each unvisited vertex.

def count_components(adj):
    raise NotImplementedError('Implement count_components(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _build_adj_list(n, edges, directed=False):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj


def test_01_single_component():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)])
    _assert_equal(count_components(adj), 1, "Connected path graph has 1 component.")


def test_02_two_components():
    adj = _build_adj_list(4, [(0, 1), (2, 3)])
    _assert_equal(count_components(adj), 2, "Two disconnected pairs.")


def test_03_all_isolated():
    adj = [[], [], [], []]
    _assert_equal(count_components(adj), 4, "Four isolated vertices = 4 components.")


def test_04_complete_graph():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (0, 2)])
    _assert_equal(count_components(adj), 1, "K3 has 1 component.")


def test_05_single_node():
    adj = [[]]
    _assert_equal(count_components(adj), 1, "Single node is 1 component.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single component", test_01_single_component),
        ("two components", test_02_two_components),
        ("all isolated", test_03_all_isolated),
        ("complete graph", test_04_complete_graph),
        ("single node", test_05_single_node),
    ]
    _run_all_tests(TEST_CASES)
