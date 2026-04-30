# Level 15a - Max Flow Edmonds-Karp
# Maximum flow from source s to sink t using BFS augmenting paths.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 15a — `max_flow_edmonds_karp`
# Maximum flow from source `s` to sink `t`, using BFS to find augmenting paths in the residual graph. (This is Ford-Fulkerson with BFS — Edmonds-Karp.)

def max_flow_edmonds_karp(n, capacity, s, t):
    raise NotImplementedError('Implement max_flow_edmonds_karp(n, capacity, s, t).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    """Build n x n capacity matrix from edge list [(u, v, cap), ...]."""
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] = c
    return cap


def test_01_pedagogy_single_edge():
    cap = _make_capacity(2, [(0, 1, 10)])
    flow = max_flow_edmonds_karp(2, cap, 0, 1)
    _assert_equal(flow, 10, "Single edge: flow equals capacity.")


def test_02_two_paths():
    # 0->1->3 (cap 5) and 0->2->3 (cap 3): max flow = 8
    cap = _make_capacity(4, [(0, 1, 5), (1, 3, 5), (0, 2, 3), (2, 3, 3)])
    flow = max_flow_edmonds_karp(4, cap, 0, 3)
    _assert_equal(flow, 8, "Two parallel paths: 5 + 3 = 8.")


def test_03_bottleneck():
    # 0->1 cap 10, 1->2 cap 5, 2->3 cap 10: bottleneck at 1->2
    cap = _make_capacity(4, [(0, 1, 10), (1, 2, 5), (2, 3, 10)])
    flow = max_flow_edmonds_karp(4, cap, 0, 3)
    _assert_equal(flow, 5, "Bottleneck limits flow.")


def test_04_diamond():
    # Classic diamond: 0->1(3), 0->2(2), 1->2(1), 1->3(2), 2->3(3)
    # Max flow = 5
    cap = _make_capacity(4, [(0, 1, 3), (0, 2, 2), (1, 2, 1), (1, 3, 2), (2, 3, 3)])
    flow = max_flow_edmonds_karp(4, cap, 0, 3)
    _assert_equal(flow, 5, "Diamond graph max flow.")


def test_05_no_path():
    # No edge from source side to sink side
    cap = _make_capacity(3, [(0, 1, 5)])
    flow = max_flow_edmonds_karp(3, cap, 0, 2)
    _assert_equal(flow, 0, "No path to sink means zero flow.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single edge", test_01_pedagogy_single_edge),
        ("two parallel paths", test_02_two_paths),
        ("bottleneck", test_03_bottleneck),
        ("diamond", test_04_diamond),
        ("no path", test_05_no_path),
    ]
    _run_all_tests(TEST_CASES)
