# Level 9d - Shortest Path At Most K Edges
# Shortest distance from s to t using at most k edges.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 9d — `shortest_path_at_most_k_edges`
# Shortest distance from `s` to `t` using at most `k` edges. The Bellman-Ford skeleton with a generation counter is the right shape.

def shortest_path_at_most_k_edges(n, edges, s, t, k):
    raise NotImplementedError('Implement shortest_path_at_most_k_edges(n, edges, s, t, k).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    # 0->1 weight 5, k=1 is enough
    edges = [(0, 1, 5)]
    result = shortest_path_at_most_k_edges(2, edges, 0, 1, 1)
    _assert_equal(result, 5, "Direct edge with k=1.")


def test_02_k_limits_path():
    # 0->1 weight 10, 0->2 weight 1, 2->1 weight 1
    # With k=1, best 0->1 is 10. With k=2, best is 0->2->1 = 2
    edges = [(0, 1, 10), (0, 2, 1), (2, 1, 1)]
    result_k1 = shortest_path_at_most_k_edges(3, edges, 0, 1, 1)
    result_k2 = shortest_path_at_most_k_edges(3, edges, 0, 1, 2)
    _assert_equal(result_k1, 10, "With k=1 must use direct edge.")
    _assert_equal(result_k2, 2, "With k=2 can use cheaper 2-hop path.")


def test_03_unreachable_within_k():
    # 0->1->2->3, each weight 1, but k=2 cannot reach vertex 3
    edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1)]
    result = shortest_path_at_most_k_edges(4, edges, 0, 3, 2)
    _assert_true(result == float('inf'), "Cannot reach 3 in 2 edges.")


def test_04_same_source_target():
    edges = [(0, 1, 5), (1, 0, 3)]
    result = shortest_path_at_most_k_edges(2, edges, 0, 0, 0)
    _assert_equal(result, 0, "Distance from vertex to itself with k=0.")


def test_05_negative_weights():
    # 0->1 weight 4, 1->2 weight -2, 0->2 weight 3; k=2
    edges = [(0, 1, 4), (1, 2, -2), (0, 2, 3)]
    result = shortest_path_at_most_k_edges(3, edges, 0, 2, 2)
    _assert_equal(result, 2, "0->1->2 = 4+(-2)=2 is better than direct 3.")


if __name__ == "__main__":
    TEST_CASES = [
        ("direct edge", test_01_pedagogy_direct_edge),
        ("k limits path choice", test_02_k_limits_path),
        ("unreachable within k", test_03_unreachable_within_k),
        ("same source and target", test_04_same_source_target),
        ("negative weights", test_05_negative_weights),
    ]
    _run_all_tests(TEST_CASES)
