# Level 2d - Two-Hop Neighbours
# Return the set of vertices reachable in exactly two hops from v (excluding v itself).

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 2d — `two_hop_neighbours`
# Return the set of vertices `u ≠ v` such that there exists some `w` with `v–w` and `w–u` both edges. The bridge between query and traversal — neighbours-of-neighbours, no visited state needed yet.

def two_hop_neighbours(adj, v):
    raise NotImplementedError('Implement two_hop_neighbours(adj, v).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_path_graph():
    # 0 - 1 - 2 - 3
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)])
    result = two_hop_neighbours(adj, 0)
    _assert_equal(result, {2}, "Two hops from 0 in path reaches 2.")


def test_02_triangle():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (0, 2)])
    result = two_hop_neighbours(adj, 0)
    # From 0: hop to 1 then 2, hop to 2 then 1. Exclude 0 itself.
    _assert_equal(result, {1, 2}, "Two hops from 0 in triangle.")


def test_03_isolated_vertex():
    adj = _build_adj_list(3, [(1, 2)])
    result = two_hop_neighbours(adj, 0)
    _assert_equal(result, set(), "Isolated vertex has no two-hop neighbours.")


def test_04_star_center():
    # Star: 0 connected to 1, 2, 3
    adj = _build_adj_list(4, [(0, 1), (0, 2), (0, 3)])
    result = two_hop_neighbours(adj, 1)
    # From 1: hop to 0, then to 2 or 3 (not back to 1)
    _assert_equal(result, {2, 3}, "Two hops from leaf in star.")


def test_05_exclude_self():
    # 0 - 1 - 0 would be a two-hop path back to self; must exclude v
    adj = _build_adj_list(2, [(0, 1)])
    result = two_hop_neighbours(adj, 0)
    # From 0: hop to 1, hop back to 0 -- but exclude self
    _assert_equal(result, set(), "Must exclude self from two-hop neighbours.")


if __name__ == "__main__":
    TEST_CASES = [
        ("path graph", test_01_path_graph),
        ("triangle", test_02_triangle),
        ("isolated vertex", test_03_isolated_vertex),
        ("star center", test_04_star_center),
        ("exclude self", test_05_exclude_self),
    ]
    _run_all_tests(TEST_CASES)
