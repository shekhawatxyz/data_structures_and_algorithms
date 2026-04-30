# Level 5b - BFS Path
# Return the shortest (fewest-edges) path from s to t, or None.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 5b — `bfs_path`
# Return the shortest (fewest-edges) path from `s` to `t`, or `None`. Reconstruct using parent pointers.

def bfs_path(adj, s, t):
    raise NotImplementedError('Implement bfs_path(adj, s, t).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_shortest_path():
    # 0-1-2-3 and 0-3 shortcut
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3), (0, 3)])
    path = bfs_path(adj, 0, 3)
    _assert_true(path is not None, "Path should exist.")
    _assert_equal(path[0], 0, "Path starts at s.")
    _assert_equal(path[-1], 3, "Path ends at t.")
    _assert_equal(len(path), 2, "Shortest path 0->3 has length 2 (1 edge).")


def test_02_no_path():
    adj = _build_adj_list(4, [(0, 1), (2, 3)])
    path = bfs_path(adj, 0, 3)
    _assert_equal(path, None, "No path between disconnected components.")


def test_03_same_node():
    adj = _build_adj_list(3, [(0, 1), (1, 2)])
    path = bfs_path(adj, 1, 1)
    _assert_true(path is not None, "Path from node to itself exists.")
    _assert_equal(path, [1], "Path from node to itself is just the node.")


def test_04_path_graph():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)])
    path = bfs_path(adj, 0, 3)
    _assert_equal(path, [0, 1, 2, 3], "Unique shortest path in path graph.")


def test_05_directed_path():
    adj = _build_adj_list(3, [(0, 1), (1, 2)], directed=True)
    path = bfs_path(adj, 0, 2)
    _assert_equal(path, [0, 1, 2], "Directed shortest path.")
    path2 = bfs_path(adj, 2, 0)
    _assert_equal(path2, None, "No backward path in directed graph.")


if __name__ == "__main__":
    TEST_CASES = [
        ("shortest path", test_01_shortest_path),
        ("no path", test_02_no_path),
        ("same node", test_03_same_node),
        ("path graph", test_04_path_graph),
        ("directed path", test_05_directed_path),
    ]
    _run_all_tests(TEST_CASES)
