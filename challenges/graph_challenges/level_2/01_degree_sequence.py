# Level 2a - Degree Sequence
# Return degrees of each vertex; for directed graphs return (in_degree, out_degree) tuples.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 2a — `degree_sequence`
# Return a list where index `i` is the degree of vertex `i`. For directed graphs, return `(in_degree, out_degree)` tuples.

def degree_sequence(adj, directed):
    raise NotImplementedError('Implement degree_sequence(adj, directed).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_undirected_triangle():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (0, 2)])
    result = degree_sequence(adj, directed=False)
    _assert_equal(result, [2, 2, 2], "All vertices in a triangle have degree 2.")


def test_02_directed_chain():
    adj = _build_adj_list(3, [(0, 1), (1, 2)], directed=True)
    result = degree_sequence(adj, directed=True)
    # (in_degree, out_degree)
    _assert_equal(result, [(0, 1), (1, 1), (1, 0)], "Directed chain degrees.")


def test_03_undirected_star():
    adj = _build_adj_list(4, [(0, 1), (0, 2), (0, 3)])
    result = degree_sequence(adj, directed=False)
    _assert_equal(result, [3, 1, 1, 1], "Star graph: center has degree 3.")


def test_04_isolated_vertices():
    adj = [[], [], []]
    result = degree_sequence(adj, directed=False)
    _assert_equal(result, [0, 0, 0], "Isolated vertices have degree 0.")


def test_05_directed_with_fan_in():
    # 0->2, 1->2, 2->3
    adj = _build_adj_list(4, [(0, 2), (1, 2), (2, 3)], directed=True)
    result = degree_sequence(adj, directed=True)
    _assert_equal(result, [(0, 1), (0, 1), (2, 1), (1, 0)], "Fan-in at vertex 2.")


if __name__ == "__main__":
    TEST_CASES = [
        ("undirected triangle", test_01_undirected_triangle),
        ("directed chain", test_02_directed_chain),
        ("undirected star", test_03_undirected_star),
        ("isolated vertices", test_04_isolated_vertices),
        ("directed fan-in", test_05_directed_with_fan_in),
    ]
    _run_all_tests(TEST_CASES)
