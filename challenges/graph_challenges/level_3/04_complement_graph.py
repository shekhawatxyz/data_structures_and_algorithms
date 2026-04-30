# Level 3d - Complement Graph
# For a simple undirected graph, return its complement.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 3d — `complement_graph`
# For a simple undirected graph, return its complement: an edge in the result iff there is no edge in the input (excluding self-loops).

def complement_graph(adj):
    raise NotImplementedError('Implement complement_graph(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_complement_of_empty():
    # Empty graph on 3 vertices -> complete graph K3
    adj = [[], [], []]
    comp = complement_graph(adj)
    _assert_equal(sorted(comp[0]), [1, 2], "Complement of empty: 0 connects to all.")
    _assert_equal(sorted(comp[1]), [0, 2], "Complement of empty: 1 connects to all.")
    _assert_equal(sorted(comp[2]), [0, 1], "Complement of empty: 2 connects to all.")


def test_02_complement_of_complete():
    # K3 -> empty graph
    adj = _build_adj_list(3, [(0, 1), (1, 2), (0, 2)])
    comp = complement_graph(adj)
    _assert_equal(comp, [[], [], []], "Complement of K3 is empty.")


def test_03_complement_of_path():
    # Path 0-1-2-3: complement has edges where path doesn't
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)])
    comp = complement_graph(adj)
    _assert_equal(sorted(comp[0]), [2, 3], "Complement: 0 connects to 2,3.")
    _assert_equal(sorted(comp[1]), [3], "Complement: 1 connects to 3.")
    _assert_equal(sorted(comp[3]), [0, 1], "Complement: 3 connects to 0,1.")


def test_04_single_node():
    adj = [[]]
    comp = complement_graph(adj)
    _assert_equal(comp, [[]], "Single node complement is still single node.")


def test_05_double_complement():
    # Complement of complement should give back original
    adj = _build_adj_list(4, [(0, 1), (2, 3)])
    comp = complement_graph(adj)
    double_comp = complement_graph(comp)
    for i in range(4):
        _assert_equal(sorted(double_comp[i]), sorted(adj[i]),
                      f"Double complement should restore vertex {i}.")


if __name__ == "__main__":
    TEST_CASES = [
        ("complement of empty", test_01_complement_of_empty),
        ("complement of complete", test_02_complement_of_complete),
        ("complement of path", test_03_complement_of_path),
        ("single node", test_04_single_node),
        ("double complement", test_05_double_complement),
    ]
    _run_all_tests(TEST_CASES)
