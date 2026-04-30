# Level 8c - Odd Cycle
# If the graph is not bipartite, return one odd-length cycle as the witness.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 8c — `odd_cycle`
# If the graph is not bipartite, return one odd-length cycle as the witness. Otherwise return `None`.

def odd_cycle(adj):
    raise NotImplementedError('Implement odd_cycle(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    """Check that cycle is a valid cycle in an undirected graph and is odd length."""
    if not cycle or len(cycle) < 3:
        return False
    # Check odd length (number of edges = number of vertices in cycle)
    if len(cycle) % 2 == 0:
        return False
    # Check edges exist
    for i in range(len(cycle)):
        u = cycle[i]
        v = cycle[(i + 1) % len(cycle)]
        if v not in adj[u]:
            return False
    return True


def test_01_triangle():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)])
    cycle = odd_cycle(adj)
    _assert_true(cycle is not None, "Triangle has odd cycle.")
    _assert_true(_is_valid_cycle(adj, cycle), f"Cycle {cycle} is not a valid odd cycle.")


def test_02_bipartite_returns_none():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    cycle = odd_cycle(adj)
    _assert_equal(cycle, None, "Even cycle graph is bipartite, no odd cycle.")


def test_03_pentagon():
    # 5-cycle is odd
    adj = _build_adj_list(5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
    cycle = odd_cycle(adj)
    _assert_true(cycle is not None, "Pentagon has odd cycle.")
    _assert_true(_is_valid_cycle(adj, cycle), f"Cycle {cycle} is not a valid odd cycle.")


def test_04_single_node():
    adj = [[]]
    cycle = odd_cycle(adj)
    _assert_equal(cycle, None, "Single node is bipartite.")


def test_05_k4():
    # Complete graph K4: has many odd cycles (triangles)
    adj = _build_adj_list(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    cycle = odd_cycle(adj)
    _assert_true(cycle is not None, "K4 has odd cycles.")
    _assert_true(_is_valid_cycle(adj, cycle), f"Cycle {cycle} is not a valid odd cycle.")


if __name__ == "__main__":
    TEST_CASES = [
        ("triangle", test_01_triangle),
        ("bipartite returns none", test_02_bipartite_returns_none),
        ("pentagon", test_03_pentagon),
        ("single node", test_04_single_node),
        ("k4", test_05_k4),
    ]
    _run_all_tests(TEST_CASES)
