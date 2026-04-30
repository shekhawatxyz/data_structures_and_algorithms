# Level 9b - Dijkstra Path
# Reconstruct the actual shortest path from s to t.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 9b — `dijkstra_path`
# As 9a, but reconstruct the actual path from `s` to `t`.

def dijkstra_path(adj, s, t):
    raise NotImplementedError('Implement dijkstra_path(adj, s, t).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_same_vertex():
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 1)])
    path = dijkstra_path(adj, 0, 0)
    _assert_equal(path, [0], "Path from vertex to itself.")


def test_02_triangle_path():
    # 0-1 weight 1, 1-2 weight 1, 0-2 weight 3
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 1), (0, 2, 3)])
    path = dijkstra_path(adj, 0, 2)
    _assert_equal(path, [0, 1, 2], "Shortest path 0->1->2.")


def test_03_no_path():
    adj = _build_weighted_adj(3, [(0, 1, 1)], directed=True)
    path = dijkstra_path(adj, 0, 2)
    _assert_true(path is None, "No path should return None.")


def test_04_direct_edge_is_shortest():
    # Direct edge 0->2 with weight 1 is better than 0->1->2 with total 5
    adj = _build_weighted_adj(3, [(0, 1, 2), (1, 2, 3), (0, 2, 1)])
    path = dijkstra_path(adj, 0, 2)
    _assert_equal(path, [0, 2], "Direct edge is shorter.")


def test_05_longer_path():
    edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 10)]
    adj = _build_weighted_adj(4, edges)
    path = dijkstra_path(adj, 0, 3)
    _assert_equal(path, [0, 1, 2, 3], "Path through intermediate nodes.")


if __name__ == "__main__":
    TEST_CASES = [
        ("same vertex", test_01_pedagogy_same_vertex),
        ("triangle path", test_02_triangle_path),
        ("no path exists", test_03_no_path),
        ("direct edge shortest", test_04_direct_edge_is_shortest),
        ("longer path", test_05_longer_path),
    ]
    _run_all_tests(TEST_CASES)
