# Level 8d - K-Colourable Check
# Decide if the graph admits a k-colouring using backtracking.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 8d — `k_colourable_check`
# Given `k`, decide if the graph admits a `k`-colouring. NP-hard in general — backtracking is the expected approach.

def k_colourable_check(adj, k):
    raise NotImplementedError('Implement k_colourable_check(adj, k).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_bipartite_2_colourable():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    _assert_equal(k_colourable_check(adj, 2), True, "Even cycle is 2-colourable.")


def test_02_triangle_not_2_colourable():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)])
    _assert_equal(k_colourable_check(adj, 2), False, "Triangle not 2-colourable.")


def test_03_triangle_3_colourable():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)])
    _assert_equal(k_colourable_check(adj, 3), True, "Triangle is 3-colourable.")


def test_04_k4_not_3_colourable():
    adj = _build_adj_list(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    _assert_equal(k_colourable_check(adj, 3), False, "K4 not 3-colourable.")
    _assert_equal(k_colourable_check(adj, 4), True, "K4 is 4-colourable.")


def test_05_empty_graph_1_colourable():
    adj = [[], [], []]
    _assert_equal(k_colourable_check(adj, 1), True,
                  "Empty graph is 1-colourable (no edges to violate).")


def test_06_single_edge_not_1_colourable():
    adj = _build_adj_list(2, [(0, 1)])
    _assert_equal(k_colourable_check(adj, 1), False,
                  "Graph with edge not 1-colourable.")
    _assert_equal(k_colourable_check(adj, 2), True,
                  "Graph with single edge is 2-colourable.")


if __name__ == "__main__":
    TEST_CASES = [
        ("bipartite 2-colourable", test_01_bipartite_2_colourable),
        ("triangle not 2-colourable", test_02_triangle_not_2_colourable),
        ("triangle 3-colourable", test_03_triangle_3_colourable),
        ("k4 colouring", test_04_k4_not_3_colourable),
        ("empty graph 1-colourable", test_05_empty_graph_1_colourable),
        ("single edge colouring", test_06_single_edge_not_1_colourable),
    ]
    _run_all_tests(TEST_CASES)
