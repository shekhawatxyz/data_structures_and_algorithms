# Level 4b - DFS Path
# Return any path from s to t using DFS, or None if none exists.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 4b — `dfs_path`
# Return *any* path from `s` to `t`, or `None` if none exists.

def dfs_path(adj, s, t):
    raise NotImplementedError('Implement dfs_path(adj, s, t).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _is_valid_path(adj, path, s, t):
    """Check that path is a valid walk from s to t in the graph."""
    if not path:
        return False
    if path[0] != s or path[-1] != t:
        return False
    for i in range(len(path) - 1):
        if path[i + 1] not in adj[path[i]]:
            return False
    return True


def test_01_path_exists():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)])
    path = dfs_path(adj, 0, 3)
    _assert_true(path is not None, "Path should exist from 0 to 3.")
    _assert_true(_is_valid_path(adj, path, 0, 3), f"Path {path} is not valid.")


def test_02_no_path():
    adj = _build_adj_list(4, [(0, 1), (2, 3)])
    path = dfs_path(adj, 0, 3)
    _assert_equal(path, None, "No path between disconnected components.")


def test_03_same_node():
    adj = _build_adj_list(3, [(0, 1), (1, 2)])
    path = dfs_path(adj, 1, 1)
    _assert_true(path is not None, "Path from node to itself should exist.")
    _assert_equal(path[0], 1, "Path starts at s.")
    _assert_equal(path[-1], 1, "Path ends at t.")


def test_04_directed_no_path():
    adj = _build_adj_list(3, [(0, 1), (1, 2)], directed=True)
    path = dfs_path(adj, 2, 0)
    _assert_equal(path, None, "No path backward in directed chain.")


def test_05_directed_path_exists():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)], directed=True)
    path = dfs_path(adj, 0, 3)
    _assert_true(path is not None, "Directed path 0->1->2->3 exists.")
    _assert_true(_is_valid_path(adj, path, 0, 3), f"Path {path} is not valid.")


if __name__ == "__main__":
    TEST_CASES = [
        ("path exists", test_01_path_exists),
        ("no path", test_02_no_path),
        ("same node", test_03_same_node),
        ("directed no path", test_04_directed_no_path),
        ("directed path exists", test_05_directed_path_exists),
    ]
    _run_all_tests(TEST_CASES)
