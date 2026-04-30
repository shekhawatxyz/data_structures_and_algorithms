# Level 3c - Reverse Directed Graph
# Given a directed graph, return its reverse: every edge flipped.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 3c — `reverse_directed_graph`
# Given a directed graph, return its reverse: every edge flipped.

def reverse_directed_graph(adj):
    raise NotImplementedError('Implement reverse_directed_graph(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_simple_chain():
    # 0->1->2
    adj = _build_adj_list(3, [(0, 1), (1, 2)], directed=True)
    rev = reverse_directed_graph(adj)
    _assert_equal(sorted(rev[0]), [], "Vertex 0 has no incoming in original.")
    _assert_equal(sorted(rev[1]), [0], "Vertex 1 had edge from 0.")
    _assert_equal(sorted(rev[2]), [1], "Vertex 2 had edge from 1.")


def test_02_fan_out():
    # 0->1, 0->2, 0->3
    adj = _build_adj_list(4, [(0, 1), (0, 2), (0, 3)], directed=True)
    rev = reverse_directed_graph(adj)
    _assert_equal(sorted(rev[0]), [], "Vertex 0 has no predecessors.")
    _assert_equal(rev[1], [0], "Vertex 1 points to 0 in reverse.")
    _assert_equal(rev[2], [0], "Vertex 2 points to 0 in reverse.")
    _assert_equal(rev[3], [0], "Vertex 3 points to 0 in reverse.")


def test_03_cycle():
    # 0->1->2->0
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
    rev = reverse_directed_graph(adj)
    _assert_equal(sorted(rev[0]), [2], "Reverse of cycle: 0 gets edge from 2.")
    _assert_equal(sorted(rev[1]), [0], "Reverse of cycle: 1 gets edge from 0.")
    _assert_equal(sorted(rev[2]), [1], "Reverse of cycle: 2 gets edge from 1.")


def test_04_empty_graph():
    adj = [[], [], []]
    rev = reverse_directed_graph(adj)
    _assert_equal(rev, [[], [], []], "Reverse of empty graph is empty.")


def test_05_single_node():
    adj = [[]]
    rev = reverse_directed_graph(adj)
    _assert_equal(rev, [[]], "Reverse of single node.")


if __name__ == "__main__":
    TEST_CASES = [
        ("simple chain", test_01_simple_chain),
        ("fan out", test_02_fan_out),
        ("cycle", test_03_cycle),
        ("empty graph", test_04_empty_graph),
        ("single node", test_05_single_node),
    ]
    _run_all_tests(TEST_CASES)
