# Level 10d - Graph Diameter
# The largest shortest-path distance between any pair of vertices.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 10d — `graph_diameter`
# The largest shortest-path distance between any pair of vertices. For unweighted graphs, BFS-from-each-vertex is also viable — compare.

def graph_diameter(adj):
    raise NotImplementedError('Implement graph_diameter(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_single_edge():
    # 2 vertices connected by weight 5
    adj = _build_weighted_adj(2, [(0, 1, 5)])
    d = graph_diameter(adj)
    _assert_equal(d, 5, "Diameter of single-edge graph is the edge weight.")


def test_02_triangle():
    # Triangle: 0-1 weight 1, 1-2 weight 1, 0-2 weight 1
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 1), (0, 2, 1)])
    d = graph_diameter(adj)
    _assert_equal(d, 1, "All pairs distance 1 in unit-weight triangle.")


def test_03_path_graph():
    # Path: 0-1-2-3 each weight 1, diameter is 3
    adj = _build_weighted_adj(4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)])
    d = graph_diameter(adj)
    _assert_equal(d, 3, "Path graph diameter is end-to-end distance.")


def test_04_weighted_path():
    # Path: 0-1 weight 2, 1-2 weight 3; diameter = 5 (0 to 2)
    adj = _build_weighted_adj(3, [(0, 1, 2), (1, 2, 3)])
    d = graph_diameter(adj)
    _assert_equal(d, 5, "Diameter is sum of path weights.")


def test_05_single_vertex():
    adj = _build_weighted_adj(1, [])
    d = graph_diameter(adj)
    _assert_equal(d, 0, "Single vertex has diameter 0.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single edge", test_01_pedagogy_single_edge),
        ("triangle", test_02_triangle),
        ("path graph", test_03_path_graph),
        ("weighted path", test_04_weighted_path),
        ("single vertex", test_05_single_vertex),
    ]
    _run_all_tests(TEST_CASES)
