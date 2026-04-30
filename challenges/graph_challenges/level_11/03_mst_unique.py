# Level 11c - MST Unique
# Return True iff the minimum spanning tree is unique.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 11c — `mst_unique`
# Return `True` iff the MST is unique. Subtle — think about edges of equal weight that could substitute for each other.

def mst_unique(adj):
    raise NotImplementedError('Implement mst_unique(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_unique_triangle():
    # Triangle with distinct weights: MST is unique
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 2), (0, 2, 3)])
    _assert_true(mst_unique(adj), "Distinct weights -> unique MST.")


def test_02_not_unique():
    # Triangle with two equal-weight edges that could substitute
    # 0-1(1), 1-2(2), 0-2(2) -> two possible MSTs of weight 3
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 2), (0, 2, 2)])
    _assert_true(not mst_unique(adj), "Equal-weight alternatives -> non-unique MST.")


def test_03_single_edge():
    adj = _build_weighted_adj(2, [(0, 1, 5)])
    _assert_true(mst_unique(adj), "Single edge graph has unique MST.")


def test_04_four_vertices_unique():
    # 0-1(1), 1-2(2), 2-3(3), 0-3(10): MST is 0-1-2-3, unique
    adj = _build_weighted_adj(4, [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 10)])
    _assert_true(mst_unique(adj), "Clear MST with no alternatives.")


def test_05_four_vertices_not_unique():
    # Square: 0-1(1), 1-2(1), 2-3(1), 0-3(1) -> many MSTs
    adj = _build_weighted_adj(4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 1)])
    _assert_true(not mst_unique(adj), "All same weight in cycle -> non-unique MST.")


if __name__ == "__main__":
    TEST_CASES = [
        ("unique triangle", test_01_pedagogy_unique_triangle),
        ("not unique", test_02_not_unique),
        ("single edge", test_03_single_edge),
        ("four vertices unique", test_04_four_vertices_unique),
        ("four vertices not unique", test_05_four_vertices_not_unique),
    ]
    _run_all_tests(TEST_CASES)
