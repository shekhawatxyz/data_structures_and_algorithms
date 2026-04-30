# Level 9a - Dijkstra Distances
# Single-source shortest distances on a graph with non-negative edge weights.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 9a — `dijkstra_distances`
# Single-source shortest distances on a graph with non-negative edge weights. Use a min-heap.

def dijkstra_distances(adj, s):
    raise NotImplementedError('Implement dijkstra_distances(adj, s).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _build_weighted_adj(n, edges, directed=False):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))
    return adj


def test_01_pedagogy_single_vertex():
    # Single vertex, distance to itself is 0
    adj = _build_weighted_adj(1, [])
    dist = dijkstra_distances(adj, 0)
    _assert_equal(dist[0], 0, "Distance to self should be 0.")


def test_02_triangle_shortest():
    # Triangle: 0-1 weight 1, 1-2 weight 1, 0-2 weight 3
    # Shortest 0->2 is via 1: cost 2
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 1), (0, 2, 3)])
    dist = dijkstra_distances(adj, 0)
    _assert_equal(dist[0], 0, "Source distance.")
    _assert_equal(dist[1], 1, "Direct edge 0->1.")
    _assert_equal(dist[2], 2, "Shortest 0->2 via 1.")


def test_03_disconnected():
    # Vertex 2 is unreachable from 0
    adj = _build_weighted_adj(3, [(0, 1, 5)])
    dist = dijkstra_distances(adj, 0)
    _assert_equal(dist[0], 0, "Source.")
    _assert_equal(dist[1], 5, "Direct edge.")
    _assert_true(dist[2] == float('inf') or dist[2] == -1,
                 "Unreachable vertex should be inf or -1.")


def test_04_directed_graph():
    # Directed: 0->1 weight 2, 0->2 weight 5, 1->2 weight 1
    adj = _build_weighted_adj(3, [(0, 1, 2), (0, 2, 5), (1, 2, 1)], directed=True)
    dist = dijkstra_distances(adj, 0)
    _assert_equal(dist[0], 0, "Source.")
    _assert_equal(dist[1], 2, "Direct edge 0->1.")
    _assert_equal(dist[2], 3, "Shortest 0->2 via 1.")


def test_05_larger_graph():
    # 5 vertices, various paths
    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5), (3, 4, 3)]
    adj = _build_weighted_adj(5, edges, directed=True)
    dist = dijkstra_distances(adj, 0)
    _assert_equal(dist[0], 0, "Source.")
    _assert_equal(dist[1], 3, "0->2->1 costs 3.")
    _assert_equal(dist[2], 1, "Direct 0->2.")
    _assert_equal(dist[3], 4, "0->2->1->3 costs 4.")
    _assert_equal(dist[4], 7, "0->2->1->3->4 costs 7.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single vertex", test_01_pedagogy_single_vertex),
        ("triangle shortest path", test_02_triangle_shortest),
        ("disconnected vertex", test_03_disconnected),
        ("directed graph", test_04_directed_graph),
        ("larger graph", test_05_larger_graph),
    ]
    _run_all_tests(TEST_CASES)
