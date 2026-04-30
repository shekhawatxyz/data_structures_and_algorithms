# Level 8a - Is Bipartite
# Return True iff the undirected graph admits a 2-colouring.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 8a — `is_bipartite`
# Return `True` iff the undirected graph admits a 2-colouring (no edge connects same-coloured vertices). BFS or DFS — try both.

def is_bipartite(adj):
    raise NotImplementedError('Implement is_bipartite(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_even_cycle():
    # 0-1-2-3-0 (4-cycle is bipartite)
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    _assert_equal(is_bipartite(adj), True, "Even cycle is bipartite.")


def test_02_odd_cycle():
    # Triangle: 0-1-2-0
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)])
    _assert_equal(is_bipartite(adj), False, "Triangle (odd cycle) not bipartite.")


def test_03_tree():
    adj = _build_adj_list(4, [(0, 1), (0, 2), (0, 3)])
    _assert_equal(is_bipartite(adj), True, "Every tree is bipartite.")


def test_04_disconnected_bipartite():
    # Two paths: 0-1, 2-3 (both bipartite)
    adj = _build_adj_list(4, [(0, 1), (2, 3)])
    _assert_equal(is_bipartite(adj), True, "Disconnected bipartite components.")


def test_05_disconnected_with_odd_cycle():
    # Component 1: 0-1 (bipartite), Component 2: 2-3-4-2 (odd cycle)
    adj = _build_adj_list(5, [(0, 1), (2, 3), (3, 4), (4, 2)])
    _assert_equal(is_bipartite(adj), False, "One non-bipartite component makes whole graph non-bipartite.")


def test_06_single_node():
    adj = [[]]
    _assert_equal(is_bipartite(adj), True, "Single node is trivially bipartite.")


if __name__ == "__main__":
    TEST_CASES = [
        ("even cycle", test_01_even_cycle),
        ("odd cycle", test_02_odd_cycle),
        ("tree", test_03_tree),
        ("disconnected bipartite", test_04_disconnected_bipartite),
        ("disconnected with odd cycle", test_05_disconnected_with_odd_cycle),
        ("single node", test_06_single_node),
    ]
    _run_all_tests(TEST_CASES)
