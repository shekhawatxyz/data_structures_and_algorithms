# Level 14d - Find Eulerian Path
# Return one Eulerian path.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 14d — `find_eulerian_path`
# Return one Eulerian path. The standard trick: add a virtual edge between the two odd-degree vertices to reduce to the circuit case, then remove it from the result.

def find_eulerian_path(adj, directed):
    raise NotImplementedError('Implement find_eulerian_path(adj, directed).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _edge_counts(adj, directed):
    counts = {}
    for u, neighbors in enumerate(adj):
        for v in neighbors:
            edge = (u, v) if directed else tuple(sorted((u, v)))
            counts[edge] = counts.get(edge, 0) + 1
    if directed:
        return counts
    return {edge: count // 2 for edge, count in counts.items()}


def _path_edge_counts(path, directed):
    counts = {}
    for u, v in zip(path, path[1:]):
        edge = (u, v) if directed else tuple(sorted((u, v)))
        counts[edge] = counts.get(edge, 0) + 1
    return counts


def _assert_eulerian_path(adj, directed, path):
    _assert_equal(
        _path_edge_counts(path, directed),
        _edge_counts(adj, directed),
        "Path should use every graph edge exactly once.",
    )


def test_01_pedagogy_directed_path():
    # 0->1->2: Eulerian path from 0 to 2
    adj = [[1], [2], []]
    path = find_eulerian_path(adj, directed=True)
    _assert_equal(path, [0, 1, 2], "Simple directed Eulerian path.")
    _assert_eulerian_path(adj, True, path)


def test_02_undirected_path():
    # 0-1-2 (path): Eulerian path from 0 to 2 (or 2 to 0)
    adj = _build_undirected_adj(3, [(0, 1), (1, 2)])
    path = find_eulerian_path(adj, directed=False)
    _assert_eulerian_path(adj, False, path)
    # Must start and end at odd-degree vertices (0 and 2)
    _assert_true({path[0], path[-1]} == {0, 2},
                 "Path starts and ends at odd-degree vertices.")


def test_03_directed_larger():
    # 0->1->2->0->2: edges (0,1),(1,2),(2,0),(0,2)
    # out-degrees: 0:2, 1:1, 2:1; in-degrees: 0:1, 1:1, 2:2
    # start at 0 (out-in=1), end at 2 (in-out=1)
    adj = [[1, 2], [2], [0]]
    path = find_eulerian_path(adj, directed=True)
    _assert_eulerian_path(adj, True, path)
    _assert_equal(path[0], 0, "Starts at vertex with extra out-degree.")
    _assert_equal(path[-1], 2, "Ends at vertex with extra in-degree.")


def test_04_undirected_uses_all_edges():
    # 0-1, 1-2, 2-3: path graph with 3 edges
    adj = _build_undirected_adj(4, [(0, 1), (1, 2), (2, 3)])
    path = find_eulerian_path(adj, directed=False)
    _assert_eulerian_path(adj, False, path)


if __name__ == "__main__":
    TEST_CASES = [
        ("directed simple path", test_01_pedagogy_directed_path),
        ("undirected path", test_02_undirected_path),
        ("directed larger", test_03_directed_larger),
        ("undirected all edges used", test_04_undirected_uses_all_edges),
    ]
    _run_all_tests(TEST_CASES)
