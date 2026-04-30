# Level 15b - Min Cut
# Find a minimum s-t cut: set of vertices on the source side.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 15b — `min_cut`
# Find a minimum `s`–`t` cut. After max flow, the cut is implicit in the residual graph: it's the set of vertices reachable from `s` in the residual.

def min_cut(n, capacity, s, t):
    raise NotImplementedError('Implement min_cut(n, capacity, s, t).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _make_capacity(n, edges):
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] = c
    return cap


def test_01_pedagogy_single_edge():
    cap = _make_capacity(2, [(0, 1, 5)])
    cut = min_cut(2, cap, 0, 1)
    _assert_true(0 in cut, "Source must be in source-side cut.")
    _assert_true(1 not in cut, "Sink must not be in source-side cut.")


def test_02_bottleneck_cut():
    # 0->1(10), 1->2(3), 2->3(10): cut at edge 1->2
    cap = _make_capacity(4, [(0, 1, 10), (1, 2, 3), (2, 3, 10)])
    cut = min_cut(4, cap, 0, 3)
    _assert_true(0 in cut, "Source in cut.")
    _assert_true(3 not in cut, "Sink not in cut.")
    _assert_true(1 in cut, "Vertex 1 on source side of bottleneck.")
    _assert_true(2 not in cut, "Vertex 2 on sink side of bottleneck.")


def test_03_two_paths():
    # 0->1->3 (cap 5) and 0->2->3 (cap 3)
    cap = _make_capacity(4, [(0, 1, 5), (1, 3, 5), (0, 2, 3), (2, 3, 3)])
    cut = min_cut(4, cap, 0, 3)
    _assert_true(0 in cut, "Source in cut.")
    _assert_true(3 not in cut, "Sink not in cut.")


def test_04_source_isolated():
    # 0->1(2), 0->2(3): no path to vertex 3
    cap = _make_capacity(4, [(0, 1, 2), (0, 2, 3)])
    cut = min_cut(4, cap, 0, 3)
    # All vertices reachable from s in residual (since t is unreachable, all except t)
    _assert_true(0 in cut, "Source in cut.")
    _assert_true(3 not in cut, "Sink not in cut.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single edge", test_01_pedagogy_single_edge),
        ("bottleneck cut", test_02_bottleneck_cut),
        ("two paths", test_03_two_paths),
        ("source isolated from sink", test_04_source_isolated),
    ]
    _run_all_tests(TEST_CASES)
