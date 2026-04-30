# Level 1d - Edges from Adjacency List
# Produce the canonical edge list from an adjacency list.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 1d — `edges_from_adjlist`
# Produce the canonical edge list back out of an adjacency list. For undirected graphs each edge appears exactly once in the result.

def edges_from_adjlist(adj, directed):
    raise NotImplementedError('Implement edges_from_adjlist(adj, directed).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_undirected_triangle():
    adj = [[1, 2], [0, 2], [0, 1]]
    edges = edges_from_adjlist(adj, directed=False)
    # Each edge once, canonically (u < v)
    _assert_equal(sorted(edges), sorted([(0, 1), (0, 2), (1, 2)]),
                  "Undirected triangle edges.")


def test_02_directed_graph():
    adj = [[1], [2], []]
    edges = edges_from_adjlist(adj, directed=True)
    _assert_equal(sorted(edges), [(0, 1), (1, 2)], "Directed edges.")


def test_03_empty_graph():
    adj = [[], [], []]
    edges = edges_from_adjlist(adj, directed=False)
    _assert_equal(edges, [], "Empty graph has no edges.")


def test_04_undirected_no_duplicates():
    # Ensure undirected edges appear exactly once
    adj = [[1, 2, 3], [0], [0], [0]]
    edges = edges_from_adjlist(adj, directed=False)
    _assert_equal(len(edges), 3, "Star graph should have 3 edges.")


def test_05_directed_all_edges():
    # Complete directed graph on 3 nodes
    adj = [[1, 2], [0, 2], [0, 1]]
    edges = edges_from_adjlist(adj, directed=True)
    _assert_equal(len(edges), 6, "Complete directed K3 has 6 directed edges.")


if __name__ == "__main__":
    TEST_CASES = [
        ("undirected triangle", test_01_undirected_triangle),
        ("directed graph", test_02_directed_graph),
        ("empty graph", test_03_empty_graph),
        ("undirected no duplicates", test_04_undirected_no_duplicates),
        ("directed all edges", test_05_directed_all_edges),
    ]
    _run_all_tests(TEST_CASES)
