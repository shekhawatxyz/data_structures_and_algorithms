# Level 11d - Second Best MST
# The second-best MST: minimum weight spanning tree among those that are not the MST.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 11d — `second_best_mst`
# The second-best MST: a spanning tree of minimum weight among those that are *not* the MST. Classical approach: find the MST, then for each non-MST edge consider swapping it in.

def second_best_mst(adj):
    raise NotImplementedError('Implement second_best_mst(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_triangle():
    # Triangle: 0-1(1), 1-2(2), 0-2(3)
    # MST: {0-1, 1-2} weight 3. Second best: {0-1, 0-2} weight 4
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 2), (0, 2, 3)])
    w = second_best_mst(adj)
    _assert_equal(w, 4, "Second best MST of triangle.")


def test_02_four_vertices():
    # 0-1(1), 1-2(2), 2-3(3), 0-3(4), 1-3(5)
    # MST: 0-1(1), 1-2(2), 2-3(3) = 6
    # Second best: swap 2-3(3) for 0-3(4) -> 0-1(1), 1-2(2), 0-3(4) = 7
    adj = _build_weighted_adj(4, [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 4), (1, 3, 5)])
    w = second_best_mst(adj)
    _assert_equal(w, 7, "Second best MST of 4-vertex graph.")


def test_03_equal_weight_alternative():
    # 0-1(1), 1-2(2), 0-2(2): MST weight 3, second best also 3
    adj = _build_weighted_adj(3, [(0, 1, 1), (1, 2, 2), (0, 2, 2)])
    w = second_best_mst(adj)
    _assert_equal(w, 3, "Second best equals MST when alternative same-weight edge exists.")


def test_04_larger_example():
    # 0-1(1), 0-2(2), 1-2(3), 1-3(4), 2-3(5)
    # MST: 0-1(1), 0-2(2), 1-3(4) = 7
    # Second best: replace 0-2(2) with 1-2(3) -> 0-1(1), 1-2(3), 1-3(4) = 8
    adj = _build_weighted_adj(4, [(0, 1, 1), (0, 2, 2), (1, 2, 3), (1, 3, 4), (2, 3, 5)])
    w = second_best_mst(adj)
    _assert_equal(w, 8, "Second best MST of larger graph.")


if __name__ == "__main__":
    TEST_CASES = [
        ("triangle", test_01_pedagogy_triangle),
        ("four vertices", test_02_four_vertices),
        ("equal weight alternative", test_03_equal_weight_alternative),
        ("larger example", test_04_larger_example),
    ]
    _run_all_tests(TEST_CASES)
