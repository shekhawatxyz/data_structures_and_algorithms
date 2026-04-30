# Level 13b - SCC Tarjan
# Find all strongly connected components using Tarjan's algorithm.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 13b — `scc_tarjan`
# Same problem, single-pass, using lowlink and a stack of unfinished vertices.

def scc_tarjan(adj):
    raise NotImplementedError('Implement scc_tarjan(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_single_scc():
    # 0->1->2->0: one SCC
    adj = [[1], [2], [0]]
    sccs = scc_tarjan(adj)
    _assert_equal(len(sccs), 1, "One SCC for a cycle.")
    _assert_equal(sorted(sccs[0]), [0, 1, 2], "All vertices in one SCC.")


def test_02_dag():
    # 0->1->2 (no cycles)
    adj = [[1], [2], []]
    sccs = scc_tarjan(adj)
    _assert_equal(len(sccs), 3, "DAG: each vertex is its own SCC.")


def test_03_two_sccs():
    # 0<->1 and 1->2
    adj = [[1], [0, 2], []]
    sccs = scc_tarjan(adj)
    _assert_equal(len(sccs), 2, "Two SCCs.")
    scc_sets = sorted([sorted(s) for s in sccs])
    _assert_equal(scc_sets, [[0, 1], [2]], "SCC grouping.")


def test_04_self_loop():
    # Vertex with self-loop is its own SCC
    adj = [[0, 1], []]
    sccs = scc_tarjan(adj)
    scc_sets = sorted([sorted(s) for s in sccs])
    _assert_equal(scc_sets, [[0], [1]], "Self-loop vertex is its own SCC, as is isolated.")


def test_05_larger_graph():
    # 0->1->2->0 and 3->4->3, with 2->3
    adj = [[1], [2], [0, 3], [4], [3]]
    sccs = scc_tarjan(adj)
    scc_sets = sorted([sorted(s) for s in sccs])
    _assert_equal(scc_sets, [[0, 1, 2], [3, 4]], "Two cycle SCCs.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single SCC", test_01_pedagogy_single_scc),
        ("DAG", test_02_dag),
        ("two SCCs", test_03_two_sccs),
        ("self loop", test_04_self_loop),
        ("larger graph", test_05_larger_graph),
    ]
    _run_all_tests(TEST_CASES)
