# Level 10a - Floyd-Warshall
# Return distance matrix where D[i][j] is the shortest distance from i to j.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 10a — `floyd_warshall`
# Return distance matrix `D` where `D[i][j]` is the shortest distance from `i` to `j`. Handles negative edges; assume no negative cycles.

def floyd_warshall(n, adj):
    raise NotImplementedError('Implement floyd_warshall(n, adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_single_vertex():
    adj = _build_weighted_adj(1, [])
    D = floyd_warshall(1, adj)
    _assert_equal(D[0][0], 0, "Distance from vertex to itself.")


def test_02_triangle():
    # Directed: 0->1 weight 1, 1->2 weight 2, 0->2 weight 10
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 2), (0, 2, 10)], directed=True)
    D = floyd_warshall(3, adj)
    _assert_equal(D[0][0], 0, "Self distance.")
    _assert_equal(D[0][1], 1, "Direct 0->1.")
    _assert_equal(D[0][2], 3, "0->1->2 = 3 beats direct 10.")
    _assert_true(D[2][0] == float('inf'), "No path from 2 to 0.")


def test_03_negative_edge():
    # 0->1 weight 3, 1->2 weight -2, 0->2 weight 5
    adj = _build_weighted_adj(3, [(0, 1, 3), (1, 2, -2), (0, 2, 5)], directed=True)
    D = floyd_warshall(3, adj)
    _assert_equal(D[0][2], 1, "0->1->2 = 3+(-2) = 1.")


def test_04_all_pairs():
    # Undirected triangle: 0-1 weight 1, 1-2 weight 2, 0-2 weight 4
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 2), (0, 2, 4)])
    D = floyd_warshall(3, adj)
    _assert_equal(D[0][1], 1, "Direct edge.")
    _assert_equal(D[0][2], 3, "0->1->2 = 3 beats direct 4.")
    _assert_equal(D[1][2], 2, "Direct 1-2.")
    _assert_equal(D[2][0], 3, "Symmetric in undirected.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single vertex", test_01_pedagogy_single_vertex),
        ("triangle directed", test_02_triangle),
        ("negative edge", test_03_negative_edge),
        ("all pairs undirected", test_04_all_pairs),
    ]
    _run_all_tests(TEST_CASES)
