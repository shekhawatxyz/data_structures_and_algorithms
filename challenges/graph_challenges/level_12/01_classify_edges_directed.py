# Level 12a - Classify Edges Directed
# During DFS of a directed graph, classify every edge as tree, back, forward, or cross.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 12a — `classify_edges_directed`
# During DFS of a directed graph, classify every edge as one of `tree`, `back`, `forward`, `cross`. Return a dict from edge to label.

def classify_edges_directed(adj):
    raise NotImplementedError('Implement classify_edges_directed(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_simple_tree():
    # 0->1->2 (chain), all edges are tree edges
    adj = [[1], [2], []]
    result = classify_edges_directed(adj)
    _assert_equal(result[(0, 1)], "tree", "0->1 is a tree edge.")
    _assert_equal(result[(1, 2)], "tree", "1->2 is a tree edge.")


def test_02_back_edge():
    # 0->1->2->0 (cycle): 2->0 is a back edge
    adj = [[1], [2], [0]]
    result = classify_edges_directed(adj)
    _assert_equal(result[(0, 1)], "tree", "0->1 is tree.")
    _assert_equal(result[(1, 2)], "tree", "1->2 is tree.")
    _assert_equal(result[(2, 0)], "back", "2->0 is back edge (creates cycle).")


def test_03_forward_edge():
    # 0->1, 1->2, 0->2: the edge 0->2 is a forward edge
    adj = [[1, 2], [2], []]
    result = classify_edges_directed(adj)
    _assert_equal(result[(0, 1)], "tree", "0->1 is tree.")
    _assert_equal(result[(1, 2)], "tree", "1->2 is tree.")
    _assert_equal(result[(0, 2)], "forward", "0->2 is forward edge.")


def test_04_cross_edge():
    # 0->1, 0->2, 2->1: DFS from 0 visits 1 first (or 2 first depending on order)
    # With adj = [[2, 1], [], [1]]: DFS visits 0->2->1, then 0->1 is cross? No.
    # Actually: 0->2 tree, 2->1 tree, then 0->1 is cross (1 already finished)
    adj = [[2, 1], [], [1]]
    result = classify_edges_directed(adj)
    _assert_equal(result[(0, 2)], "tree", "0->2 is tree.")
    _assert_equal(result[(2, 1)], "tree", "2->1 is tree.")
    _assert_equal(result[(0, 1)], "cross", "0->1 is cross (1 already finished).")


def test_05_self_loop_is_back():
    # 0->0 is a back edge (self-loop)
    adj = [[0]]
    result = classify_edges_directed(adj)
    _assert_equal(result[(0, 0)], "back", "Self-loop is a back edge.")


if __name__ == "__main__":
    TEST_CASES = [
        ("simple tree edges", test_01_pedagogy_simple_tree),
        ("back edge in cycle", test_02_back_edge),
        ("forward edge", test_03_forward_edge),
        ("cross edge", test_04_cross_edge),
        ("self loop is back", test_05_self_loop_is_back),
    ]
    _run_all_tests(TEST_CASES)
