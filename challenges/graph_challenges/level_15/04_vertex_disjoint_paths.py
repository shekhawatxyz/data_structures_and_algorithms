# Level 15d - Vertex Disjoint Paths
# Maximum number of internally vertex-disjoint paths from s to t.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 15d — `vertex_disjoint_paths`
# Maximum number of internally vertex-disjoint paths from `s` to `t`, by reduction to max-flow. The trick is node-splitting: replace each non-source/sink vertex `v` with two vertices `v_in` and `v_out` connected by a unit-capacity edge.

def vertex_disjoint_paths(n, adj, s, t):
    raise NotImplementedError('Implement vertex_disjoint_paths(n, adj, s, t).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_direct_edge():
    # 0->1: one vertex-disjoint path
    adj = [[1], []]
    result = vertex_disjoint_paths(2, adj, 0, 1)
    _assert_equal(result, 1, "Direct edge gives 1 path.")


def test_02_two_disjoint_paths():
    # 0->1->3, 0->2->3: two vertex-disjoint paths
    adj = [[1, 2], [3], [3], []]
    result = vertex_disjoint_paths(4, adj, 0, 3)
    _assert_equal(result, 2, "Two internally vertex-disjoint paths.")


def test_03_bottleneck_vertex():
    # 0->1->2->3, 0->1->3: vertex 1 is shared, limits to 1
    # Actually: 0->1, 0->2, 1->3, 2->3: two paths 0->1->3 and 0->2->3 (disjoint)
    # For bottleneck: 0->1->2, 0->1->3 won't work. Let's use:
    # 0->1->3, 0->2->1->3: share vertex 1, so only 1 vertex-disjoint path? No.
    # Better: 0->1->2 and only path is through 1
    adj = [[1], [2], []]
    result = vertex_disjoint_paths(3, adj, 0, 2)
    _assert_equal(result, 1, "Single path through bottleneck vertex.")


def test_04_no_path():
    adj = [[1], [], []]
    result = vertex_disjoint_paths(3, adj, 0, 2)
    _assert_equal(result, 0, "No path from s to t.")


def test_05_three_disjoint():
    # 0->1->4, 0->2->4, 0->3->4: three vertex-disjoint paths
    adj = [[1, 2, 3], [4], [4], [4], []]
    result = vertex_disjoint_paths(5, adj, 0, 4)
    _assert_equal(result, 3, "Three internally vertex-disjoint paths.")


if __name__ == "__main__":
    TEST_CASES = [
        ("direct edge", test_01_pedagogy_direct_edge),
        ("two disjoint paths", test_02_two_disjoint_paths),
        ("bottleneck vertex", test_03_bottleneck_vertex),
        ("no path", test_04_no_path),
        ("three disjoint paths", test_05_three_disjoint),
    ]
    _run_all_tests(TEST_CASES)
