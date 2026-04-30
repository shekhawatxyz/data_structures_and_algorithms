# Level 6d - Count Back Edges
# During a DFS run on a directed graph, count the back edges.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 6d — `count_back_edges`
# During a DFS run on a directed graph, count the back edges. A primer for full edge classification later.

def count_back_edges(adj):
    raise NotImplementedError('Implement count_back_edges(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_single_cycle():
    # 0->1->2->0: one back edge (2->0)
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    _assert_equal(count_back_edges(adj), 1, "One cycle = one back edge.")


def test_02_dag_no_back_edges():
    adj = _build_adj_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
    _assert_equal(count_back_edges(adj), 0, "DAG has no back edges.")


def test_03_self_loop():
    adj = [[0], []]
    _assert_equal(count_back_edges(adj), 1, "Self-loop is a back edge.")


def test_04_two_cycles():
    # 0->1->0, 1->2->1: two back edges
    adj = _build_adj_list(3, [(0, 1), (1, 0), (1, 2), (2, 1)], directed=True)
    _assert_equal(count_back_edges(adj), 2, "Two separate cycles = two back edges.")


def test_05_empty_graph():
    adj = [[], [], []]
    _assert_equal(count_back_edges(adj), 0, "Empty graph has no back edges.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single cycle", test_01_single_cycle),
        ("dag no back edges", test_02_dag_no_back_edges),
        ("self loop", test_03_self_loop),
        ("two cycles", test_04_two_cycles),
        ("empty graph", test_05_empty_graph),
    ]
    _run_all_tests(TEST_CASES)
