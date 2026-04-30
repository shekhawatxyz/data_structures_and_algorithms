# Level 8b - Bipartition
# Return the two colour classes as a pair of lists, or None if not bipartite.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 8b — `bipartition`
# Return the two colour classes as a pair of lists, or `None` if not bipartite.

def bipartition(adj):
    raise NotImplementedError('Implement bipartition(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _is_valid_bipartition(adj, parts):
    """Check that parts is a valid 2-colouring."""
    if parts is None:
        return False
    part_a, part_b = parts
    all_vertices = sorted(part_a + part_b)
    if all_vertices != list(range(len(adj))):
        return False
    color = {}
    for v in part_a:
        color[v] = 0
    for v in part_b:
        color[v] = 1
    for u in range(len(adj)):
        for v in adj[u]:
            if color[u] == color[v]:
                return False
    return True


def test_01_even_cycle():
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    result = bipartition(adj)
    _assert_true(_is_valid_bipartition(adj, result),
                 f"Result {result} is not a valid bipartition.")


def test_02_not_bipartite():
    adj = _build_adj_list(3, [(0, 1), (1, 2), (2, 0)])
    result = bipartition(adj)
    _assert_equal(result, None, "Triangle is not bipartite.")


def test_03_path():
    adj = _build_adj_list(3, [(0, 1), (1, 2)])
    result = bipartition(adj)
    _assert_true(_is_valid_bipartition(adj, result),
                 f"Result {result} is not a valid bipartition.")


def test_04_single_node():
    adj = [[]]
    result = bipartition(adj)
    _assert_true(result is not None, "Single node is bipartite.")
    part_a, part_b = result
    _assert_equal(sorted(part_a + part_b), [0], "Must include vertex 0.")


def test_05_disconnected():
    adj = _build_adj_list(4, [(0, 1), (2, 3)])
    result = bipartition(adj)
    _assert_true(_is_valid_bipartition(adj, result),
                 f"Result {result} is not a valid bipartition.")


if __name__ == "__main__":
    TEST_CASES = [
        ("even cycle", test_01_even_cycle),
        ("not bipartite", test_02_not_bipartite),
        ("path", test_03_path),
        ("single node", test_04_single_node),
        ("disconnected", test_05_disconnected),
    ]
    _run_all_tests(TEST_CASES)
