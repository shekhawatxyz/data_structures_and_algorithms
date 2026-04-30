# Level 14c - Find Eulerian Circuit
# Return one Eulerian circuit using Hierholzer's algorithm.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 14c — `find_eulerian_circuit`
# Return one Eulerian circuit using Hierholzer's algorithm: walk until stuck, then splice in sub-tours from vertices with unused edges.

def find_eulerian_circuit(adj, directed):
    raise NotImplementedError('Implement find_eulerian_circuit(adj, directed).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _build_undirected_adj(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def _edge_counts(adj, directed):
    counts = {}
    for u, neighbors in enumerate(adj):
        for v in neighbors:
            edge = (u, v) if directed else tuple(sorted((u, v)))
            counts[edge] = counts.get(edge, 0) + 1
    if directed:
        return counts
    return {edge: count // 2 for edge, count in counts.items()}


def _path_edge_counts(path, directed):
    counts = {}
    for u, v in zip(path, path[1:]):
        edge = (u, v) if directed else tuple(sorted((u, v)))
        counts[edge] = counts.get(edge, 0) + 1
    return counts


def _assert_eulerian_circuit(adj, directed, circuit):
    _assert_equal(circuit[0], circuit[-1], "Circuit starts and ends at same vertex.")
    _assert_equal(
        _path_edge_counts(circuit, directed),
        _edge_counts(adj, directed),
        "Circuit should use every graph edge exactly once.",
    )


def test_01_pedagogy_directed_triangle():
    # 0->1->2->0
    adj = [[1], [2], [0]]
    circuit = find_eulerian_circuit(adj, directed=True)
    _assert_eulerian_circuit(adj, True, circuit)


def test_02_undirected_triangle():
    adj = _build_undirected_adj(3, [(0, 1), (1, 2), (0, 2)])
    circuit = find_eulerian_circuit(adj, directed=False)
    _assert_eulerian_circuit(adj, False, circuit)


def test_03_directed_uses_all_edges():
    # 0->1->2->0, 0->2->1->0 (two triangles sharing vertices)
    adj = [[1, 2], [2, 0], [0, 1]]
    circuit = find_eulerian_circuit(adj, directed=True)
    _assert_eulerian_circuit(adj, True, circuit)


def test_04_undirected_square():
    # Square: 0-1-2-3-0
    adj = _build_undirected_adj(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    circuit = find_eulerian_circuit(adj, directed=False)
    _assert_eulerian_circuit(adj, False, circuit)


def test_05_validates_edges():
    # Verify each consecutive pair is a valid edge
    adj = [[1], [2], [0]]
    circuit = find_eulerian_circuit(adj, directed=True)
    _assert_eulerian_circuit(adj, True, circuit)


if __name__ == "__main__":
    TEST_CASES = [
        ("directed triangle", test_01_pedagogy_directed_triangle),
        ("undirected triangle", test_02_undirected_triangle),
        ("directed all edges", test_03_directed_uses_all_edges),
        ("undirected square", test_04_undirected_square),
        ("validates edges", test_05_validates_edges),
    ]
    _run_all_tests(TEST_CASES)
