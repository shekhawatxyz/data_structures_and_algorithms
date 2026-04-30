# Level 10c - Transitive Closure
# Boolean reachability matrix using Floyd-Warshall skeleton with logical OR.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 10c — `transitive_closure`
# For an unweighted directed graph, return the boolean matrix `R` where `R[i][j]` is `True` iff `j` is reachable from `i`. The Floyd-Warshall skeleton with logical OR for `min`.

def transitive_closure(n, adj):
    raise NotImplementedError('Implement transitive_closure(n, adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_chain():
    # 0->1->2, so 0 can reach 2 transitively
    adj = [[1], [2], []]
    R = transitive_closure(3, adj)
    _assert_true(R[0][0], "Self-reachable.")
    _assert_true(R[0][1], "Direct edge.")
    _assert_true(R[0][2], "Transitive: 0->1->2.")
    _assert_true(not R[2][0], "No path from 2 to 0.")


def test_02_cycle():
    # 0->1->2->0 (cycle)
    adj = [[1], [2], [0]]
    R = transitive_closure(3, adj)
    _assert_true(R[0][2], "0 reaches 2.")
    _assert_true(R[2][0], "2 reaches 0 via cycle.")
    _assert_true(R[1][0], "1 reaches 0 via cycle.")


def test_03_disconnected():
    # 0->1, vertex 2 isolated
    adj = [[1], [], []]
    R = transitive_closure(3, adj)
    _assert_true(R[0][1], "Direct edge.")
    _assert_true(not R[0][2], "2 is isolated.")
    _assert_true(not R[1][0], "No reverse edge.")
    _assert_true(R[2][2], "Self-reachable.")


def test_04_complete_reachability():
    # 0->1, 1->2, 2->3, 3->0 (full cycle)
    adj = [[1], [2], [3], [0]]
    R = transitive_closure(4, adj)
    for i in range(4):
        for j in range(4):
            _assert_true(R[i][j], f"{i} should reach {j} in full cycle.")


def test_05_single_vertex():
    adj = [[]]
    R = transitive_closure(1, adj)
    _assert_true(R[0][0], "Single vertex reaches itself.")


if __name__ == "__main__":
    TEST_CASES = [
        ("chain", test_01_pedagogy_chain),
        ("cycle", test_02_cycle),
        ("disconnected", test_03_disconnected),
        ("complete reachability", test_04_complete_reachability),
        ("single vertex", test_05_single_vertex),
    ]
    _run_all_tests(TEST_CASES)
