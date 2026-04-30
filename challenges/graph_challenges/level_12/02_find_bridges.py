# Level 12b - Find Bridges
# Find every bridge edge whose removal disconnects the graph.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 12b — `find_bridges`
# In an undirected graph, find every bridge: edges whose removal disconnects the graph. Tarjan's lowlink technique.

def find_bridges(adj):
    raise NotImplementedError('Implement find_bridges(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _build_undirected_adj(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def test_01_pedagogy_single_bridge():
    # 0-1-2, edge 1-2 is a bridge, edge 0-1 is a bridge
    adj = _build_undirected_adj(3, [(0, 1), (1, 2)])
    bridges = find_bridges(adj)
    bridge_set = {(min(u, v), max(u, v)) for u, v in bridges}
    _assert_equal(bridge_set, {(0, 1), (1, 2)}, "Both edges in a path are bridges.")


def test_02_no_bridges_in_cycle():
    # Triangle: no bridges
    adj = _build_undirected_adj(3, [(0, 1), (1, 2), (0, 2)])
    bridges = find_bridges(adj)
    _assert_equal(len(bridges), 0, "Triangle has no bridges.")


def test_03_mixed():
    # 0-1-2-0 (cycle) plus 2-3 (bridge)
    adj = _build_undirected_adj(4, [(0, 1), (1, 2), (2, 0), (2, 3)])
    bridges = find_bridges(adj)
    bridge_set = {(min(u, v), max(u, v)) for u, v in bridges}
    _assert_equal(bridge_set, {(2, 3)}, "Only 2-3 is a bridge.")


def test_04_two_components_connected_by_bridge():
    # Two triangles connected by a bridge: 0-1-2-0 and 3-4-5-3, bridge 2-3
    adj = _build_undirected_adj(6, [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (2, 3)])
    bridges = find_bridges(adj)
    bridge_set = {(min(u, v), max(u, v)) for u, v in bridges}
    _assert_equal(bridge_set, {(2, 3)}, "Bridge connecting two biconnected components.")


def test_05_single_edge():
    adj = _build_undirected_adj(2, [(0, 1)])
    bridges = find_bridges(adj)
    bridge_set = {(min(u, v), max(u, v)) for u, v in bridges}
    _assert_equal(bridge_set, {(0, 1)}, "Single edge is a bridge.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single bridge in path", test_01_pedagogy_single_bridge),
        ("no bridges in cycle", test_02_no_bridges_in_cycle),
        ("mixed bridges", test_03_mixed),
        ("two components with bridge", test_04_two_components_connected_by_bridge),
        ("single edge", test_05_single_edge),
    ]
    _run_all_tests(TEST_CASES)
