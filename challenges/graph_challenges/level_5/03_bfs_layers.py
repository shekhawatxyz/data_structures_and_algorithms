# Level 5c - BFS Layers
# Return layers where layers[k] is the list of vertices exactly k edges from s.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 5c — `bfs_layers`
# Return `layers` where `layers[k]` is the list of all vertices exactly `k` edges away from `s`.

def bfs_layers(adj, s):
    raise NotImplementedError('Implement bfs_layers(adj, s).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_path_graph():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)])
    layers = bfs_layers(adj, 0)
    _assert_equal(layers[0], [0], "Layer 0 is source.")
    _assert_equal(layers[1], [1], "Layer 1.")
    _assert_equal(layers[2], [2], "Layer 2.")
    _assert_equal(layers[3], [3], "Layer 3.")


def test_02_star_graph():
    adj = _build_adj_list(4, [(0, 1), (0, 2), (0, 3)])
    layers = bfs_layers(adj, 0)
    _assert_equal(layers[0], [0], "Layer 0 is source.")
    _assert_equal(sorted(layers[1]), [1, 2, 3], "All leaves at layer 1.")
    _assert_equal(len(layers), 2, "Only 2 layers in star from center.")


def test_03_disconnected():
    adj = _build_adj_list(4, [(0, 1)])
    layers = bfs_layers(adj, 0)
    _assert_equal(layers[0], [0], "Layer 0.")
    _assert_equal(layers[1], [1], "Layer 1.")
    # Unreachable vertices should not appear in any layer
    all_vertices = []
    for layer in layers:
        all_vertices.extend(layer)
    _assert_true(2 not in all_vertices, "Unreachable vertex 2 not in layers.")
    _assert_true(3 not in all_vertices, "Unreachable vertex 3 not in layers.")


def test_04_single_node():
    adj = [[]]
    layers = bfs_layers(adj, 0)
    _assert_equal(layers, [[0]], "Single node: one layer with source.")


def test_05_triangle():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (0, 2)])
    layers = bfs_layers(adj, 0)
    _assert_equal(layers[0], [0], "Layer 0.")
    _assert_equal(sorted(layers[1]), [1, 2], "Both neighbours at layer 1.")


if __name__ == "__main__":
    TEST_CASES = [
        ("path graph", test_01_path_graph),
        ("star graph", test_02_star_graph),
        ("disconnected", test_03_disconnected),
        ("single node", test_04_single_node),
        ("triangle", test_05_triangle),
    ]
    _run_all_tests(TEST_CASES)
