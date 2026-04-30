# Level 7d - Longest Path in DAG
# Find the length of the longest path in a DAG.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 7d — `longest_path_in_dag`
# Length of the longest path in a DAG. The whole graph is the search space — but processed in the right order, the DP is one pass.

def longest_path_in_dag(adj):
    raise NotImplementedError('Implement longest_path_in_dag(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _build_adj_list(n, edges, directed=False):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj


def test_01_chain():
    # 0->1->2->3: longest path = 3 edges
    adj = _build_adj_list(4, [(0, 1), (1, 2), (2, 3)], directed=True)
    _assert_equal(longest_path_in_dag(adj), 3, "Chain of 4 nodes: longest path 3 edges.")


def test_02_diamond():
    # 0->1, 0->2, 1->3, 2->3: longest path = 2 (e.g., 0->1->3)
    adj = _build_adj_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
    _assert_equal(longest_path_in_dag(adj), 2, "Diamond: longest path 2 edges.")


def test_03_single_node():
    adj = [[]]
    _assert_equal(longest_path_in_dag(adj), 0, "Single node: longest path 0.")


def test_04_disconnected():
    # 0->1, 2->3->4: longest paths are 1 and 2, overall 2
    adj = _build_adj_list(5, [(0, 1), (2, 3), (3, 4)], directed=True)
    _assert_equal(longest_path_in_dag(adj), 2, "Disconnected: longest path is 2.")


def test_05_wide_dag():
    # 0->1, 0->2, 0->3, 1->4, 2->4, 3->4: longest = 2
    adj = _build_adj_list(5, [(0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 4)],
                          directed=True)
    _assert_equal(longest_path_in_dag(adj), 2, "Wide DAG: longest path 2 edges.")


if __name__ == "__main__":
    TEST_CASES = [
        ("chain", test_01_chain),
        ("diamond", test_02_diamond),
        ("single node", test_03_single_node),
        ("disconnected", test_04_disconnected),
        ("wide dag", test_05_wide_dag),
    ]
    _run_all_tests(TEST_CASES)
