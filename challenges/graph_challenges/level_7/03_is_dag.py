# Level 7c - Is DAG
# Return True iff the directed graph is acyclic.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 7c — `is_dag`
# Return `True` iff the directed graph is acyclic. (Either approach above will do; or reuse `has_cycle_directed`.)

def is_dag(adj):
    raise NotImplementedError('Implement is_dag(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_dag():
    adj = _build_adj_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
    _assert_equal(is_dag(adj), True, "Diamond DAG is acyclic.")


def test_02_has_cycle():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    _assert_equal(is_dag(adj), False, "Cycle means not a DAG.")


def test_03_empty_graph():
    adj = [[], [], []]
    _assert_equal(is_dag(adj), True, "Empty graph is a DAG.")


def test_04_self_loop():
    adj = [[0]]
    _assert_equal(is_dag(adj), False, "Self-loop means not a DAG.")


def test_05_chain():
    adj = _build_adj_list(5, [(0, 1), (1, 2), (2, 3), (3, 4)], directed=True)
    _assert_equal(is_dag(adj), True, "Chain is a DAG.")


if __name__ == "__main__":
    TEST_CASES = [
        ("dag", test_01_dag),
        ("has cycle", test_02_has_cycle),
        ("empty graph", test_03_empty_graph),
        ("self loop", test_04_self_loop),
        ("chain", test_05_chain),
    ]
    _run_all_tests(TEST_CASES)
