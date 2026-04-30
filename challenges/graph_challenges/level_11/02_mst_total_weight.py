# Level 11b - MST Total Weight
# Just the total weight of the minimum spanning tree.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 11b — `mst_total_weight`
# Just the total weight of the MST.

def mst_total_weight(adj):
    raise NotImplementedError('Implement mst_total_weight(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _build_weighted_adj(n, edges, directed=False):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))
    return adj


def test_01_pedagogy_single_edge():
    adj = _build_weighted_adj(2, [(0, 1, 4)])
    w = mst_total_weight(adj)
    _assert_equal(w, 4, "Single edge weight.")


def test_02_triangle():
    # Triangle: weights 1, 2, 3; MST picks 1+2=3
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 2), (0, 2, 3)])
    w = mst_total_weight(adj)
    _assert_equal(w, 3, "MST of triangle picks two lightest edges.")


def test_03_four_vertices():
    # 0-1(1), 1-3(2), 0-2(3), 2-3(4), 1-2(5)
    # MST: 0-1(1), 1-3(2), 0-2(3) = 6
    adj = _build_weighted_adj(4, [(0, 1, 1), (1, 3, 2), (0, 2, 3), (2, 3, 4), (1, 2, 5)])
    w = mst_total_weight(adj)
    _assert_equal(w, 6, "MST total weight of 4-vertex graph.")


def test_04_already_a_tree():
    # Path: 0-1(10), 1-2(20), 2-3(30)
    adj = _build_weighted_adj(4, [(0, 1, 10), (1, 2, 20), (2, 3, 30)])
    w = mst_total_weight(adj)
    _assert_equal(w, 60, "Tree is its own MST.")


def test_05_single_vertex():
    adj = _build_weighted_adj(1, [])
    w = mst_total_weight(adj)
    _assert_equal(w, 0, "Single vertex has MST weight 0.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single edge", test_01_pedagogy_single_edge),
        ("triangle", test_02_triangle),
        ("four vertices", test_03_four_vertices),
        ("already a tree", test_04_already_a_tree),
        ("single vertex", test_05_single_vertex),
    ]
    _run_all_tests(TEST_CASES)
