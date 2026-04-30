# Level 7b - Topological Sort (Kahn's Algorithm)
# Return a topological order using Kahn's algorithm (in-degree zero processing).

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 7b — `topological_sort_kahn`
# Same problem, computed via Kahn's algorithm: start from in-degree-zero vertices, process and remove, repeat.

def topological_sort_kahn(adj):
    raise NotImplementedError('Implement topological_sort_kahn(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _assert_raises(expected_exception, callable_obj, context):
    try:
        callable_obj()
    except expected_exception:
        return
    except Exception as exc:
        raise AssertionError(
            f"{context} Expected {expected_exception.__name__}, "
            f"got {type(exc).__name__}: {exc}."
        ) from exc
    raise AssertionError(
        f"{context} Expected {expected_exception.__name__}, but none was raised."
    )


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


def _is_valid_topo_order(adj, order):
    """Check that order is a valid topological ordering."""
    if sorted(order) != list(range(len(adj))):
        return False
    pos = {v: i for i, v in enumerate(order)}
    for u in range(len(adj)):
        for v in adj[u]:
            if pos[u] >= pos[v]:
                return False
    return True


def test_01_simple_chain():
    adj = _build_adj_list(3, [(0, 1), (1, 2)], directed=True)
    order = topological_sort_kahn(adj)
    _assert_true(_is_valid_topo_order(adj, order),
                 f"Order {order} is not valid topological sort.")


def test_02_diamond():
    adj = _build_adj_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
    order = topological_sort_kahn(adj)
    _assert_true(_is_valid_topo_order(adj, order),
                 f"Order {order} is not valid topological sort.")


def test_03_cycle_raises():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    _assert_raises(ValueError, lambda: topological_sort_kahn(adj),
                   "Should raise ValueError for cyclic graph.")


def test_04_isolated_nodes():
    adj = [[], [], []]
    order = topological_sort_kahn(adj)
    _assert_true(_is_valid_topo_order(adj, order),
                 f"Order {order} is not valid topological sort.")


def test_05_complex_dag():
    # 0->2, 1->2, 2->3, 1->3
    adj = _build_adj_list(4, [(0, 2), (1, 2), (2, 3), (1, 3)], directed=True)
    order = topological_sort_kahn(adj)
    _assert_true(_is_valid_topo_order(adj, order),
                 f"Order {order} is not valid topological sort.")


if __name__ == "__main__":
    TEST_CASES = [
        ("simple chain", test_01_simple_chain),
        ("diamond", test_02_diamond),
        ("cycle raises", test_03_cycle_raises),
        ("isolated nodes", test_04_isolated_nodes),
        ("complex dag", test_05_complex_dag),
    ]
    _run_all_tests(TEST_CASES)
