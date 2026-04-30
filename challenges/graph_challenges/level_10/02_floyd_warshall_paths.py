# Level 10b - Floyd-Warshall Paths
# All-pairs shortest paths with path reconstruction via a next matrix.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 10b — `floyd_warshall_paths`
# As 10a, with path reconstruction. Maintain a `next` (or predecessor) matrix during the DP.

def floyd_warshall_paths(n, adj):
    raise NotImplementedError('Implement floyd_warshall_paths(n, adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _reconstruct_path(nxt, s, t):
    """Reconstruct path from s to t using next matrix."""
    if nxt[s][t] is None:
        return None
    path = [s]
    while s != t:
        s = nxt[s][t]
        path.append(s)
    return path


def test_01_pedagogy_direct_edge():
    adj = _build_weighted_adj(2, [(0, 1, 3)], directed=True)
    dist, nxt = floyd_warshall_paths(2, adj)
    _assert_equal(dist[0][1], 3, "Direct edge distance.")
    path = _reconstruct_path(nxt, 0, 1)
    _assert_equal(path, [0, 1], "Direct edge path.")


def test_02_intermediate_vertex():
    # 0->1 weight 1, 1->2 weight 2, 0->2 weight 10
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 2), (0, 2, 10)], directed=True)
    dist, nxt = floyd_warshall_paths(3, adj)
    _assert_equal(dist[0][2], 3, "Shortest via intermediate.")
    path = _reconstruct_path(nxt, 0, 2)
    _assert_equal(path, [0, 1, 2], "Path goes through vertex 1.")


def test_03_no_path():
    adj = _build_weighted_adj(3, [(0, 1, 1)], directed=True)
    dist, nxt = floyd_warshall_paths(3, adj)
    _assert_true(dist[0][2] == float('inf'), "No path from 0 to 2.")
    _assert_true(nxt[0][2] is None, "Next should be None for unreachable.")


def test_04_self_distance():
    adj = _build_weighted_adj(2, [(0, 1, 5)], directed=True)
    dist, nxt = floyd_warshall_paths(2, adj)
    _assert_equal(dist[0][0], 0, "Self distance is 0.")
    _assert_equal(dist[1][1], 0, "Self distance is 0.")


if __name__ == "__main__":
    TEST_CASES = [
        ("direct edge", test_01_pedagogy_direct_edge),
        ("intermediate vertex", test_02_intermediate_vertex),
        ("no path", test_03_no_path),
        ("self distance", test_04_self_distance),
    ]
    _run_all_tests(TEST_CASES)
