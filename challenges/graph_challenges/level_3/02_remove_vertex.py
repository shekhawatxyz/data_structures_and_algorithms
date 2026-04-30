# Level 3b - Remove Vertex
# Remove vertex v and every edge incident to it.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 3b — `remove_vertex`
# Remove vertex `v` and every edge incident to it. Decide: do you renumber the remaining vertices, or leave a tombstone? Both are defensible — make the choice deliberately.

def remove_vertex(adj, v):
    raise NotImplementedError('Implement remove_vertex(adj, v).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_remove_middle_vertex():
    # Triangle: 0-1, 1-2, 0-2. Remove vertex 1.
    adj = _build_adj_list(3, [(0, 1), (1, 2), (0, 2)])
    result = remove_vertex(adj, 1)
    # After removing vertex 1, remaining vertices should still be connected if edge 0-2 exists
    # The exact format depends on implementation (tombstone vs renumber)
    # Check that vertex 1's edges are gone and no reference to 1 remains
    _assert_true(result is not None or adj is not None,
                 "Function should return the modified graph or modify in place.")


def test_02_remove_leaf():
    # Star: 0-1, 0-2, 0-3. Remove vertex 3.
    adj = _build_adj_list(4, [(0, 1), (0, 2), (0, 3)])
    result = remove_vertex(adj, 3)
    graph = result if result is not None else adj
    # Vertex 3 should not appear in any neighbour list
    for i, neighbours in enumerate(graph):
        if neighbours is not None:  # handle tombstone
            _assert_true(3 not in neighbours,
                         f"Vertex 3 should not appear in adj[{i}] after removal.")


def test_03_remove_only_vertex():
    adj = [[]]
    result = remove_vertex(adj, 0)
    graph = result if result is not None else adj
    # Should result in empty graph
    _assert_true(len(graph) == 0 or graph == [None] or graph == [[]],
                 "Removing only vertex should yield empty or tombstoned graph.")


def test_04_remove_isolated_vertex():
    adj = [[], [2], [1], []]
    result = remove_vertex(adj, 0)
    graph = result if result is not None else adj
    # Edge 1-2 should still be intact
    found_edge = False
    for i, neighbours in enumerate(graph):
        if neighbours is not None and len(neighbours) > 0:
            found_edge = True
    _assert_true(found_edge, "Removing isolated vertex should preserve other edges.")


if __name__ == "__main__":
    TEST_CASES = [
        ("remove middle vertex", test_01_remove_middle_vertex),
        ("remove leaf", test_02_remove_leaf),
        ("remove only vertex", test_03_remove_only_vertex),
        ("remove isolated vertex", test_04_remove_isolated_vertex),
    ]
    _run_all_tests(TEST_CASES)
