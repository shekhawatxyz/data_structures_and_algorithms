# Level 13c - Condensation
# Build the condensation DAG by collapsing each SCC into one super-vertex.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 13c — `condensation`
# Build the condensation: collapse each SCC into one super-vertex; super-edges are inherited from the original graph. The result is a DAG.

def condensation(adj):
    raise NotImplementedError('Implement condensation(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_already_dag():
    # 0->1->2 is already a DAG; condensation has 3 super-vertices
    adj = [[1], [2], []]
    cond_adj, scc_id = condensation(adj)
    _assert_equal(len(cond_adj), 3, "3 SCCs in a DAG.")
    # Each vertex is its own SCC
    _assert_true(scc_id[0] != scc_id[1] and scc_id[1] != scc_id[2],
                 "Each vertex has distinct SCC ID.")


def test_02_single_scc():
    # 0->1->2->0: one SCC -> one super-vertex, no edges
    adj = [[1], [2], [0]]
    cond_adj, scc_id = condensation(adj)
    _assert_equal(len(cond_adj), 1, "One super-vertex.")
    _assert_equal(cond_adj[0], [], "No self-edges in condensation.")
    _assert_true(scc_id[0] == scc_id[1] == scc_id[2], "All same SCC ID.")


def test_03_two_sccs_with_edge():
    # 0<->1, 1->2: SCC {0,1} -> SCC {2}
    adj = [[1], [0, 2], []]
    cond_adj, scc_id = condensation(adj)
    _assert_equal(len(cond_adj), 2, "Two super-vertices.")
    _assert_equal(scc_id[0], scc_id[1], "0 and 1 in same SCC.")
    _assert_true(scc_id[2] != scc_id[0], "2 in different SCC.")
    # There should be an edge from SCC of {0,1} to SCC of {2}
    src_scc = scc_id[0]
    _assert_true(scc_id[2] in cond_adj[src_scc],
                 "Edge from {0,1} SCC to {2} SCC in condensation.")


def test_04_no_edges_between_sccs():
    # Two isolated cycles: 0->1->0 and 2->3->2
    adj = [[1], [0], [3], [2]]
    cond_adj, scc_id = condensation(adj)
    _assert_equal(len(cond_adj), 2, "Two super-vertices.")
    _assert_equal(scc_id[0], scc_id[1], "0,1 same SCC.")
    _assert_equal(scc_id[2], scc_id[3], "2,3 same SCC.")
    for neighbors in cond_adj:
        _assert_equal(neighbors, [], "No edges between isolated SCCs.")


if __name__ == "__main__":
    TEST_CASES = [
        ("already a DAG", test_01_pedagogy_already_dag),
        ("single SCC", test_02_single_scc),
        ("two SCCs with edge", test_03_two_sccs_with_edge),
        ("no edges between SCCs", test_04_no_edges_between_sccs),
    ]
    _run_all_tests(TEST_CASES)
