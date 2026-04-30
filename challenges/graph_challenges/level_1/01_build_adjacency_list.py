# Level 1a - Build Adjacency List
# Build an adjacency list from a list of edges and a vertex count.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 1a — `build_adjacency_list`
# Build an adjacency list from a list of edges and a vertex count.
# ```python
# def build_adjacency_list(n: int, edges: list[tuple[int, int]], directed: bool) -> list[list[int]]
# ```

def build_adjacency_list(n, edges, directed):
    raise NotImplementedError('Implement build_adjacency_list(n, edges, directed).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    # 3 nodes, edges: 0-1, 1-2, 0-2 (triangle)
    adj = build_adjacency_list(3, [(0, 1), (1, 2), (0, 2)], directed=False)
    _assert_equal(len(adj), 3, "Should have 3 vertices.")
    _assert_equal(sorted(adj[0]), [1, 2], "Vertex 0 neighbours.")
    _assert_equal(sorted(adj[1]), [0, 2], "Vertex 1 neighbours.")
    _assert_equal(sorted(adj[2]), [0, 1], "Vertex 2 neighbours.")


def test_02_directed_graph():
    # 3 nodes, directed edges: 0->1, 1->2
    adj = build_adjacency_list(3, [(0, 1), (1, 2)], directed=True)
    _assert_equal(adj[0], [1], "Vertex 0 successors.")
    _assert_equal(adj[1], [2], "Vertex 1 successors.")
    _assert_equal(adj[2], [], "Vertex 2 successors.")


def test_03_empty_graph():
    # 4 nodes, no edges
    adj = build_adjacency_list(4, [], directed=False)
    _assert_equal(adj, [[], [], [], []], "Empty graph should have no neighbours.")


def test_04_single_node():
    adj = build_adjacency_list(1, [], directed=False)
    _assert_equal(adj, [[]], "Single node graph.")


def test_05_directed_self_contained():
    # Directed graph where one node has multiple successors
    adj = build_adjacency_list(4, [(0, 1), (0, 2), (0, 3)], directed=True)
    _assert_equal(sorted(adj[0]), [1, 2, 3], "Vertex 0 has three successors.")
    _assert_equal(adj[1], [], "Vertex 1 has no successors.")


if __name__ == "__main__":
    TEST_CASES = [
        ("undirected triangle", test_01_undirected_triangle),
        ("directed graph", test_02_directed_graph),
        ("empty graph", test_03_empty_graph),
        ("single node", test_04_single_node),
        ("directed multiple successors", test_05_directed_self_contained),
    ]
    _run_all_tests(TEST_CASES)
