# Level 9c - Bellman-Ford
# Single-source shortest distances tolerating negative edges, detecting negative cycles.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 9c — `bellman_ford`
# Single-source shortest distances tolerating negative edges. Detect a reachable negative cycle and signal it.

def bellman_ford(n, edges, s):
    raise NotImplementedError('Implement bellman_ford(n, edges, s).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_simple_positive():
    # 3 vertices: 0->1 weight 3, 1->2 weight 4
    edges = [(0, 1, 3), (1, 2, 4)]
    dist = bellman_ford(3, edges, 0)
    _assert_equal(dist[0], 0, "Source distance.")
    _assert_equal(dist[1], 3, "Direct edge.")
    _assert_equal(dist[2], 7, "Path 0->1->2.")


def test_02_negative_edge():
    # 3 vertices: 0->1 weight 5, 0->2 weight 2, 2->1 weight -4
    edges = [(0, 1, 5), (0, 2, 2), (2, 1, -4)]
    dist = bellman_ford(3, edges, 0)
    _assert_equal(dist[0], 0, "Source.")
    _assert_equal(dist[1], -2, "Shortest via negative edge: 0->2->1 = -2.")
    _assert_equal(dist[2], 2, "Direct 0->2.")


def test_03_negative_cycle_detected():
    # 3 vertices forming a negative cycle: 0->1 weight 1, 1->2 weight -1, 2->0 weight -1
    edges = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]
    try:
        result = bellman_ford(3, edges, 0)
    except ValueError:
        return
    # Should signal negative cycle: either return None, raise ValueError, or return special value
    _assert_true(result is None or result == "NEGATIVE_CYCLE",
                 "Should detect negative cycle (return None or 'NEGATIVE_CYCLE').")


def test_04_unreachable_vertex():
    # 4 vertices, only 0->1
    edges = [(0, 1, 2)]
    dist = bellman_ford(4, edges, 0)
    _assert_equal(dist[0], 0, "Source.")
    _assert_equal(dist[1], 2, "Direct edge.")
    _assert_true(dist[2] == float('inf'), "Unreachable vertex 2.")
    _assert_true(dist[3] == float('inf'), "Unreachable vertex 3.")


def test_05_single_vertex():
    dist = bellman_ford(1, [], 0)
    _assert_equal(dist[0], 0, "Single vertex distance to self.")


if __name__ == "__main__":
    TEST_CASES = [
        ("simple positive weights", test_01_pedagogy_simple_positive),
        ("negative edge", test_02_negative_edge),
        ("negative cycle detected", test_03_negative_cycle_detected),
        ("unreachable vertex", test_04_unreachable_vertex),
        ("single vertex", test_05_single_vertex),
    ]
    _run_all_tests(TEST_CASES)
