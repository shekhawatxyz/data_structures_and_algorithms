# Level 6a - Has Cycle (Undirected)
# Return True iff the undirected graph contains a cycle.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 6a — `has_cycle_undirected`
# Return `True` iff the undirected graph contains a cycle. Subtle point: how do you avoid a false positive on the parent edge during DFS?

def has_cycle_undirected(adj):
    raise NotImplementedError('Implement has_cycle_undirected(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_triangle_has_cycle():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (0, 2)])
    _assert_equal(has_cycle_undirected(adj), True, "Triangle is a cycle.")


def test_02_tree_no_cycle():
    adj = _build_adj_list(4, [(0, 1), (0, 2), (0, 3)])
    _assert_equal(has_cycle_undirected(adj), False, "Star tree has no cycle.")


def test_03_path_no_cycle():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)])
    _assert_equal(has_cycle_undirected(adj), False, "Path has no cycle.")


def test_04_disconnected_with_cycle():
    # Component 1: 0-1 (no cycle), Component 2: 2-3-4-2 (cycle)
    adj = _build_adj_list(5, [(0, 1), (2, 3), (3, 4), (4, 2)])
    _assert_equal(has_cycle_undirected(adj), True,
                  "Cycle in one component is enough.")


def test_05_single_node():
    adj = [[]]
    _assert_equal(has_cycle_undirected(adj), False, "Single node has no cycle.")


def test_06_empty_graph():
    adj = [[], [], []]
    _assert_equal(has_cycle_undirected(adj), False, "Empty graph has no cycle.")


if __name__ == "__main__":
    TEST_CASES = [
        ("triangle has cycle", test_01_triangle_has_cycle),
        ("tree no cycle", test_02_tree_no_cycle),
        ("path no cycle", test_03_path_no_cycle),
        ("disconnected with cycle", test_04_disconnected_with_cycle),
        ("single node", test_05_single_node),
        ("empty graph", test_06_empty_graph),
    ]
    _run_all_tests(TEST_CASES)
