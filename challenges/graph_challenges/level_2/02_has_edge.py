# Level 2b - Has Edge
# Given a representation and (u, v), return whether the edge exists.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 2b — `has_edge`
# Given a representation and `(u, v)`, return whether the edge exists. Implement for both adjacency list and matrix; note the cost difference.

def has_edge(adj, u, v):
    raise NotImplementedError('Implement has_edge(adj, u, v).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_edge_exists():
    adj = _build_adj_list(3, [(0, 1), (1, 2)])
    _assert_equal(has_edge(adj, 0, 1), True, "Edge 0-1 exists.")
    _assert_equal(has_edge(adj, 1, 0), True, "Edge 1-0 exists (undirected).")


def test_02_edge_not_exists():
    adj = _build_adj_list(3, [(0, 1)])
    _assert_equal(has_edge(adj, 0, 2), False, "Edge 0-2 does not exist.")
    _assert_equal(has_edge(adj, 1, 2), False, "Edge 1-2 does not exist.")


def test_03_directed_edge():
    adj = _build_adj_list(3, [(0, 1), (1, 2)], directed=True)
    _assert_equal(has_edge(adj, 0, 1), True, "Directed edge 0->1 exists.")
    _assert_equal(has_edge(adj, 1, 0), False, "No edge 1->0 in directed graph.")


def test_04_self_check():
    adj = _build_adj_list(3, [(0, 1)])
    _assert_equal(has_edge(adj, 0, 0), False, "No self-loop at 0.")


def test_05_empty_graph():
    adj = [[], [], []]
    _assert_equal(has_edge(adj, 0, 1), False, "No edges in empty graph.")
    _assert_equal(has_edge(adj, 2, 0), False, "No edges in empty graph.")


if __name__ == "__main__":
    TEST_CASES = [
        ("edge exists", test_01_edge_exists),
        ("edge not exists", test_02_edge_not_exists),
        ("directed edge", test_03_directed_edge),
        ("self check", test_04_self_check),
        ("empty graph", test_05_empty_graph),
    ]
    _run_all_tests(TEST_CASES)
