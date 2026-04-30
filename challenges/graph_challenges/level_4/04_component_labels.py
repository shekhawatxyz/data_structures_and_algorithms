# Level 4d - Component Labels
# Return a list where label[i] is the component ID of vertex i.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 4d — `component_labels`
# Return a list where `label[i]` is the component ID of vertex `i`. Assign IDs `0, 1, 2, …` in order of discovery.

def component_labels(adj):
    raise NotImplementedError('Implement component_labels(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_single_component():
    adj = _build_adj_list(3, [(0, 1), (1, 2)])
    labels = component_labels(adj)
    # All should have same label (0)
    _assert_equal(labels, [0, 0, 0], "Connected graph: all vertices in component 0.")


def test_02_two_components():
    adj = _build_adj_list(4, [(0, 1), (2, 3)])
    labels = component_labels(adj)
    _assert_equal(labels[0], labels[1], "0 and 1 in same component.")
    _assert_equal(labels[2], labels[3], "2 and 3 in same component.")
    _assert_true(labels[0] != labels[2], "Different components get different IDs.")
    _assert_equal(labels[0], 0, "First discovered component has ID 0.")
    _assert_equal(labels[2], 1, "Second discovered component has ID 1.")


def test_03_all_isolated():
    adj = [[], [], []]
    labels = component_labels(adj)
    _assert_equal(labels, [0, 1, 2], "Each isolated vertex is its own component.")


def test_04_single_node():
    adj = [[]]
    labels = component_labels(adj)
    _assert_equal(labels, [0], "Single node in component 0.")


def test_05_three_components():
    # 0-1, 2 alone, 3-4
    adj = _build_adj_list(5, [(0, 1), (3, 4)])
    labels = component_labels(adj)
    _assert_equal(labels[0], labels[1], "0 and 1 together.")
    _assert_equal(labels[3], labels[4], "3 and 4 together.")
    _assert_equal(labels[0], 0, "First component is 0.")
    _assert_equal(labels[2], 1, "Isolated vertex 2 is component 1.")
    _assert_equal(labels[3], 2, "Third component is 2.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single component", test_01_single_component),
        ("two components", test_02_two_components),
        ("all isolated", test_03_all_isolated),
        ("single node", test_04_single_node),
        ("three components", test_05_three_components),
    ]
    _run_all_tests(TEST_CASES)
