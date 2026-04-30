# Level 11a - Prim MST
# Minimum spanning tree via Prim's algorithm with a min-heap.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 11a — `prim_mst`
# Minimum spanning tree of a connected undirected weighted graph, via Prim's algorithm with a min-heap. Return the MST as a list of edges.

def prim_mst(adj):
    raise NotImplementedError('Implement prim_mst(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_two_vertices():
    adj = _build_weighted_adj(2, [(0, 1, 7)])
    mst = prim_mst(adj)
    edges_sorted = sorted((min(u, v), max(u, v), w) for u, v, w in mst)
    _assert_equal(edges_sorted, [(0, 1, 7)], "MST of 2 vertices is the single edge.")


def test_02_triangle():
    # Triangle: 0-1 weight 1, 1-2 weight 2, 0-2 weight 3
    # MST picks edges of weight 1 and 2
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 2), (0, 2, 3)])
    mst = prim_mst(adj)
    total = sum(w for _, _, w in mst)
    _assert_equal(total, 3, "MST total weight for triangle.")
    _assert_equal(len(mst), 2, "MST has n-1 edges.")


def test_03_four_vertex_graph():
    # Square with diagonal: 0-1(1), 1-2(4), 2-3(2), 0-3(3), 0-2(5)
    # MST: 0-1(1), 2-3(2), 0-3(3) = total 6
    adj = _build_weighted_adj(4, [(0, 1, 1), (1, 2, 4), (2, 3, 2), (0, 3, 3), (0, 2, 5)])
    mst = prim_mst(adj)
    total = sum(w for _, _, w in mst)
    _assert_equal(total, 6, "MST of 4-vertex graph.")
    _assert_equal(len(mst), 3, "MST has n-1 edges.")


def test_04_single_vertex():
    adj = _build_weighted_adj(1, [])
    mst = prim_mst(adj)
    _assert_equal(len(mst), 0, "Single vertex MST has no edges.")


def test_05_path_graph_is_mst():
    # Path 0-1(1), 1-2(1), 2-3(1) — already a tree
    adj = _build_weighted_adj(4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)])
    mst = prim_mst(adj)
    total = sum(w for _, _, w in mst)
    _assert_equal(total, 3, "Path graph is its own MST.")
    _assert_equal(len(mst), 3, "MST has n-1 edges.")


if __name__ == "__main__":
    TEST_CASES = [
        ("two vertices", test_01_pedagogy_two_vertices),
        ("triangle", test_02_triangle),
        ("four vertex graph", test_03_four_vertex_graph),
        ("single vertex", test_04_single_vertex),
        ("path graph is MST", test_05_path_graph_is_mst),
    ]
    _run_all_tests(TEST_CASES)
