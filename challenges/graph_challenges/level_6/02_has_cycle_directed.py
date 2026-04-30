# Level 6b - Has Cycle (Directed)
# Return True iff the directed graph contains a cycle.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 6b — `has_cycle_directed`
# Return `True` iff the directed graph contains a cycle. The technique is genuinely different from 6a — DFS with three states (unvisited, in-progress, finished); a back-edge is the witness.

def has_cycle_directed(adj):
    raise NotImplementedError('Implement has_cycle_directed(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_simple_cycle():
    # 0->1->2->0
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    _assert_equal(has_cycle_directed(adj), True, "Simple directed cycle.")


def test_02_dag():
    # 0->1->2, 0->2 (DAG)
    adj = _build_adj_list(3, [(0, 1), (1, 2), (0, 2)], directed=True)
    _assert_equal(has_cycle_directed(adj), False, "DAG has no cycle.")


def test_03_self_loop():
    adj = [[0], []]
    _assert_equal(has_cycle_directed(adj), True, "Self-loop is a cycle.")


def test_04_disconnected_with_cycle():
    # Component 1: 0->1 (no cycle), Component 2: 2->3->2 (cycle)
    adj = _build_adj_list(4, [(0, 1), (2, 3), (3, 2)], directed=True)
    _assert_equal(has_cycle_directed(adj), True, "Cycle in one component.")


def test_05_chain_no_cycle():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)], directed=True)
    _assert_equal(has_cycle_directed(adj), False, "Directed chain is acyclic.")


if __name__ == "__main__":
    TEST_CASES = [
        ("simple cycle", test_01_simple_cycle),
        ("dag", test_02_dag),
        ("self loop", test_03_self_loop),
        ("disconnected with cycle", test_04_disconnected_with_cycle),
        ("chain no cycle", test_05_chain_no_cycle),
    ]
    _run_all_tests(TEST_CASES)
