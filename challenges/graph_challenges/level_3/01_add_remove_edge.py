# Level 3a - Add and Remove Edge
# Maintain adjacency-list representation under edge mutations.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 3a — `add_edge` and `remove_edge`
# Maintain adjacency-list representation under edge mutations. For undirected, both endpoints' lists update.

def add_edge(adj, u, v, directed):
    raise NotImplementedError('Implement add_edge(adj, u, v, directed).')


def remove_edge(adj, u, v, directed):
    raise NotImplementedError('Implement remove_edge(adj, u, v, directed).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_add_undirected():
    adj = [[], [], []]
    add_edge(adj, 0, 1, directed=False)
    _assert_true(1 in adj[0], "After add_edge(0,1), 1 should be in adj[0].")
    _assert_true(0 in adj[1], "After add_edge(0,1), 0 should be in adj[1].")


def test_02_add_directed():
    adj = [[], [], []]
    add_edge(adj, 0, 1, directed=True)
    _assert_true(1 in adj[0], "After directed add_edge(0,1), 1 in adj[0].")
    _assert_true(0 not in adj[1], "After directed add_edge(0,1), 0 NOT in adj[1].")


def test_03_remove_undirected():
    adj = [[1, 2], [0, 2], [0, 1]]
    remove_edge(adj, 0, 1, directed=False)
    _assert_true(1 not in adj[0], "After remove, 1 not in adj[0].")
    _assert_true(0 not in adj[1], "After remove, 0 not in adj[1].")
    _assert_true(2 in adj[0], "Edge 0-2 still present.")


def test_04_remove_directed():
    adj = [[1, 2], [2], []]
    remove_edge(adj, 0, 1, directed=True)
    _assert_true(1 not in adj[0], "After directed remove, 1 not in adj[0].")
    _assert_true(2 in adj[0], "Edge 0->2 still present.")


def test_05_add_then_remove():
    adj = [[], []]
    add_edge(adj, 0, 1, directed=False)
    _assert_true(1 in adj[0], "Edge added.")
    remove_edge(adj, 0, 1, directed=False)
    _assert_true(1 not in adj[0], "Edge removed.")
    _assert_true(0 not in adj[1], "Edge removed from other end.")


if __name__ == "__main__":
    TEST_CASES = [
        ("add undirected", test_01_add_undirected),
        ("add directed", test_02_add_directed),
        ("remove undirected", test_03_remove_undirected),
        ("remove directed", test_04_remove_directed),
        ("add then remove", test_05_add_then_remove),
    ]
    _run_all_tests(TEST_CASES)
