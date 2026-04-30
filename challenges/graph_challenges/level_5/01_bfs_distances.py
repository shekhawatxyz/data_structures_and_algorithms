# Level 5a - BFS Distances
# Return shortest path distances (in edges) from source s to all vertices.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 5a — `bfs_distances`
# Return `dist` where `dist[v]` is the shortest path length (in edges) from `s` to `v`, or `-1` if unreachable.

def bfs_distances(adj, s):
    raise NotImplementedError('Implement bfs_distances(adj, s).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_path_graph():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)])
    dist = bfs_distances(adj, 0)
    _assert_equal(dist, [0, 1, 2, 3], "Distances along a path from source 0.")


def test_02_unreachable():
    adj = _build_adj_list(4, [(0, 1), (2, 3)])
    dist = bfs_distances(adj, 0)
    _assert_equal(dist[0], 0, "Distance to self is 0.")
    _assert_equal(dist[1], 1, "Distance to neighbour is 1.")
    _assert_equal(dist[2], -1, "Unreachable vertex gets -1.")
    _assert_equal(dist[3], -1, "Unreachable vertex gets -1.")


def test_03_triangle():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (0, 2)])
    dist = bfs_distances(adj, 0)
    _assert_equal(dist, [0, 1, 1], "Triangle: all neighbours at distance 1.")


def test_04_single_node():
    adj = [[]]
    dist = bfs_distances(adj, 0)
    _assert_equal(dist, [0], "Single node: distance to self is 0.")


def test_05_star_graph():
    adj = _build_adj_list(5, [(0, 1), (0, 2), (0, 3), (0, 4)])
    dist = bfs_distances(adj, 0)
    _assert_equal(dist, [0, 1, 1, 1, 1], "Star: all leaves at distance 1 from center.")
    dist2 = bfs_distances(adj, 1)
    _assert_equal(dist2[0], 1, "Leaf to center is 1.")
    _assert_equal(dist2[2], 2, "Leaf to leaf through center is 2.")


if __name__ == "__main__":
    TEST_CASES = [
        ("path graph", test_01_path_graph),
        ("unreachable vertices", test_02_unreachable),
        ("triangle", test_03_triangle),
        ("single node", test_04_single_node),
        ("star graph", test_05_star_graph),
    ]
    _run_all_tests(TEST_CASES)
