# Level 12c - Find Articulation Points
# Find every articulation point whose removal disconnects the graph.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 12c — `find_articulation_points`
# In an undirected graph, find every articulation point: vertices whose removal disconnects the graph. Same lowlink machinery, different condition.

def find_articulation_points(adj):
    raise NotImplementedError('Implement find_articulation_points(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_path():
    # Path 0-1-2: vertex 1 is an AP
    adj = _build_undirected_adj(3, [(0, 1), (1, 2)])
    aps = find_articulation_points(adj)
    _assert_equal(set(aps), {1}, "Middle vertex in path is AP.")


def test_02_no_ap_in_triangle():
    adj = _build_undirected_adj(3, [(0, 1), (1, 2), (0, 2)])
    aps = find_articulation_points(adj)
    _assert_equal(set(aps), set(), "No AP in a triangle.")


def test_03_center_of_star():
    # Star: 0 connected to 1, 2, 3
    adj = _build_undirected_adj(4, [(0, 1), (0, 2), (0, 3)])
    aps = find_articulation_points(adj)
    _assert_equal(set(aps), {0}, "Center of star is AP.")


def test_04_two_biconnected_components():
    # 0-1-2-0 and 2-3-4-2: vertex 2 is AP
    adj = _build_undirected_adj(5, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2)])
    aps = find_articulation_points(adj)
    _assert_equal(set(aps), {2}, "Vertex connecting two cycles is AP.")


def test_05_chain():
    # 0-1-2-3-4: vertices 1, 2, 3 are APs
    adj = _build_undirected_adj(5, [(0, 1), (1, 2), (2, 3), (3, 4)])
    aps = find_articulation_points(adj)
    _assert_equal(set(aps), {1, 2, 3}, "Internal vertices in chain are APs.")


if __name__ == "__main__":
    TEST_CASES = [
        ("path graph", test_01_pedagogy_path),
        ("no AP in triangle", test_02_no_ap_in_triangle),
        ("star center", test_03_center_of_star),
        ("two biconnected components", test_04_two_biconnected_components),
        ("chain", test_05_chain),
    ]
    _run_all_tests(TEST_CASES)
