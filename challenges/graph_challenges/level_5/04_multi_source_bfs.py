# Level 5d - Multi-Source BFS
# Return for each vertex its distance to the nearest source.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 5d — `multi_source_bfs`
# Given a set of sources `S`, return for each vertex its distance to the *nearest* source. The trick is in the initialisation.

def multi_source_bfs(adj, sources):
    raise NotImplementedError('Implement multi_source_bfs(adj, sources).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_single_source():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)])
    dist = multi_source_bfs(adj, [0])
    _assert_equal(dist, [0, 1, 2, 3], "Single source same as regular BFS.")


def test_02_two_sources():
    # Path: 0-1-2-3-4, sources at 0 and 4
    adj = _build_adj_list(5, [(0, 1), (1, 2), (2, 3), (3, 4)])
    dist = multi_source_bfs(adj, [0, 4])
    _assert_equal(dist, [0, 1, 2, 1, 0], "Distances to nearest of two endpoints.")


def test_03_all_sources():
    adj = _build_adj_list(3, [(0, 1), (1, 2)])
    dist = multi_source_bfs(adj, [0, 1, 2])
    _assert_equal(dist, [0, 0, 0], "All vertices are sources.")


def test_04_unreachable():
    adj = _build_adj_list(4, [(0, 1)])
    dist = multi_source_bfs(adj, [0])
    _assert_equal(dist[0], 0, "Source distance is 0.")
    _assert_equal(dist[1], 1, "Neighbour of source is 1.")
    _assert_equal(dist[2], -1, "Unreachable vertex is -1.")
    _assert_equal(dist[3], -1, "Unreachable vertex is -1.")


def test_05_source_in_middle():
    # Path: 0-1-2-3-4, source at 2
    adj = _build_adj_list(5, [(0, 1), (1, 2), (2, 3), (3, 4)])
    dist = multi_source_bfs(adj, [2])
    _assert_equal(dist, [2, 1, 0, 1, 2], "Source in middle of path.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single source", test_01_single_source),
        ("two sources", test_02_two_sources),
        ("all sources", test_03_all_sources),
        ("unreachable", test_04_unreachable),
        ("source in middle", test_05_source_in_middle),
    ]
    _run_all_tests(TEST_CASES)
