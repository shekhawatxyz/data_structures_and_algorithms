# Level 12d - Biconnected Components
# Decompose an undirected graph into biconnected components.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 12d — `biconnected_components`
# Decompose an undirected graph into biconnected components. Maintain a stack of edges during DFS and pop the right ones at each articulation point.

def biconnected_components(adj):
    raise NotImplementedError('Implement biconnected_components(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_single_edge():
    adj = _build_undirected_adj(2, [(0, 1)])
    comps = biconnected_components(adj)
    _assert_equal(len(comps), 1, "Single edge is one biconnected component.")
    edges_in_comp = {(min(u, v), max(u, v)) for u, v in comps[0]}
    _assert_equal(edges_in_comp, {(0, 1)}, "The component contains the edge.")


def test_02_triangle_is_one_component():
    adj = _build_undirected_adj(3, [(0, 1), (1, 2), (0, 2)])
    comps = biconnected_components(adj)
    _assert_equal(len(comps), 1, "Triangle is one biconnected component.")
    edges_in_comp = {(min(u, v), max(u, v)) for u, v in comps[0]}
    _assert_equal(edges_in_comp, {(0, 1), (1, 2), (0, 2)}, "All three edges.")


def test_03_two_components():
    # 0-1-2-0 and 2-3: two biconnected components
    adj = _build_undirected_adj(4, [(0, 1), (1, 2), (2, 0), (2, 3)])
    comps = biconnected_components(adj)
    _assert_equal(len(comps), 2, "Two biconnected components.")
    all_edges = []
    for comp in comps:
        all_edges.append({(min(u, v), max(u, v)) for u, v in comp})
    all_edges_sorted = sorted(all_edges, key=len)
    _assert_equal(all_edges_sorted[0], {(2, 3)}, "Bridge component.")
    _assert_equal(all_edges_sorted[1], {(0, 1), (0, 2), (1, 2)}, "Triangle component.")


def test_04_path_graph():
    # 0-1-2-3: each edge is its own biconnected component
    adj = _build_undirected_adj(4, [(0, 1), (1, 2), (2, 3)])
    comps = biconnected_components(adj)
    _assert_equal(len(comps), 3, "Path of 4 vertices has 3 biconnected components.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single edge", test_01_pedagogy_single_edge),
        ("triangle", test_02_triangle_is_one_component),
        ("two components", test_03_two_components),
        ("path graph", test_04_path_graph),
    ]
    _run_all_tests(TEST_CASES)
