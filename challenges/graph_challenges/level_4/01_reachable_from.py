# Level 4a - Reachable From
# Return the set of vertices reachable from source s using DFS.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 4a — `reachable_from`
# Return the set of vertices reachable from source `s`. Implement once recursively, once iteratively (with an explicit stack). The two should agree.

def reachable_from(adj, s):
    raise NotImplementedError('Implement reachable_from(adj, s).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_connected_graph():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)])
    result = reachable_from(adj, 0)
    _assert_equal(result, {0, 1, 2, 3}, "All vertices reachable in connected path.")


def test_02_disconnected_graph():
    adj = _build_adj_list(4, [(0, 1), (2, 3)])
    result = reachable_from(adj, 0)
    _assert_equal(result, {0, 1}, "Only component containing 0.")


def test_03_directed_graph():
    adj = _build_adj_list(3, [(0, 1), (1, 2)], directed=True)
    result = reachable_from(adj, 0)
    _assert_equal(result, {0, 1, 2}, "All reachable following directed edges.")
    result2 = reachable_from(adj, 2)
    _assert_equal(result2, {2}, "Vertex 2 can only reach itself in directed chain.")


def test_04_single_node():
    adj = [[]]
    result = reachable_from(adj, 0)
    _assert_equal(result, {0}, "Single node reaches only itself.")


def test_05_cycle():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    result = reachable_from(adj, 0)
    _assert_equal(result, {0, 1, 2}, "All vertices reachable in directed cycle.")


if __name__ == "__main__":
    TEST_CASES = [
        ("connected graph", test_01_connected_graph),
        ("disconnected graph", test_02_disconnected_graph),
        ("directed graph", test_03_directed_graph),
        ("single node", test_04_single_node),
        ("cycle", test_05_cycle),
    ]
    _run_all_tests(TEST_CASES)
