# Level 6c - Find Cycle (Directed)
# Return one cycle as a list of vertices, or None if the graph is acyclic.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 6c — `find_cycle_directed`
# Return one cycle as a list of vertices, or `None` if the graph is acyclic.

def find_cycle_directed(adj):
    raise NotImplementedError('Implement find_cycle_directed(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _is_valid_cycle(adj, cycle):
    """Verify that cycle is a valid directed cycle in the graph."""
    if not cycle or len(cycle) < 2:
        return False
    for i in range(len(cycle) - 1):
        if cycle[i + 1] not in adj[cycle[i]]:
            return False
    # Last vertex must connect back to first
    if cycle[0] not in adj[cycle[-1]]:
        return False
    return True


def test_01_simple_cycle():
    # 0->1->2->0
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    cycle = find_cycle_directed(adj)
    _assert_true(cycle is not None, "Cycle should be found.")
    _assert_true(_is_valid_cycle(adj, cycle), f"Cycle {cycle} is not valid.")


def test_02_dag_no_cycle():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (0, 2)], directed=True)
    cycle = find_cycle_directed(adj)
    _assert_equal(cycle, None, "DAG has no cycle.")


def test_03_self_loop():
    adj = [[0], []]
    cycle = find_cycle_directed(adj)
    _assert_true(cycle is not None, "Self-loop is a cycle.")
    _assert_equal(cycle, [0], "Self-loop cycle is [0].")


def test_04_larger_cycle():
    # 0->1->2->3->1 (cycle is 1->2->3->1)
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3), (3, 1)], directed=True)
    cycle = find_cycle_directed(adj)
    _assert_true(cycle is not None, "Cycle exists.")
    _assert_true(_is_valid_cycle(adj, cycle), f"Cycle {cycle} is not valid.")


def test_05_empty_graph():
    adj = [[], [], []]
    cycle = find_cycle_directed(adj)
    _assert_equal(cycle, None, "Empty graph has no cycle.")


if __name__ == "__main__":
    TEST_CASES = [
        ("simple cycle", test_01_simple_cycle),
        ("dag no cycle", test_02_dag_no_cycle),
        ("self loop", test_03_self_loop),
        ("larger cycle", test_04_larger_cycle),
        ("empty graph", test_05_empty_graph),
    ]
    _run_all_tests(TEST_CASES)
