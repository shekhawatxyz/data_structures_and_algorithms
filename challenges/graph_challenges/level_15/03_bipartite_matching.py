# Level 15c - Bipartite Matching
# Maximum matching in a bipartite graph by reduction to max-flow.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 15c — `bipartite_matching`
# Maximum matching in a bipartite graph, by reduction to max-flow. Add a super-source, a super-sink, unit capacities everywhere.

def bipartite_matching(n_left, n_right, edges):
    raise NotImplementedError('Implement bipartite_matching(n_left, n_right, edges).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_single_edge():
    # 1 left, 1 right, one edge: matching size 1
    edges = [(0, 0)]
    result = bipartite_matching(1, 1, edges)
    _assert_equal(result, 1, "Single edge gives matching of size 1.")


def test_02_perfect_matching():
    # 3 left, 3 right: 0-0, 1-1, 2-2
    edges = [(0, 0), (1, 1), (2, 2)]
    result = bipartite_matching(3, 3, edges)
    _assert_equal(result, 3, "Perfect matching of size 3.")


def test_03_partial_matching():
    # 3 left, 2 right: 0-0, 1-0, 2-1 -> max matching 2
    edges = [(0, 0), (1, 0), (2, 1)]
    result = bipartite_matching(3, 2, edges)
    _assert_equal(result, 2, "At most 2 since only 2 right vertices.")


def test_04_no_edges():
    edges = []
    result = bipartite_matching(3, 3, edges)
    _assert_equal(result, 0, "No edges means no matching.")


def test_05_complex_matching():
    # 3 left, 3 right: 0-0, 0-1, 1-0, 1-1, 2-2
    # Max matching: 3 (e.g., 0-1, 1-0, 2-2)
    edges = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)]
    result = bipartite_matching(3, 3, edges)
    _assert_equal(result, 3, "Maximum matching is 3.")


if __name__ == "__main__":
    TEST_CASES = [
        ("single edge", test_01_pedagogy_single_edge),
        ("perfect matching", test_02_perfect_matching),
        ("partial matching", test_03_partial_matching),
        ("no edges", test_04_no_edges),
        ("complex matching", test_05_complex_matching),
    ]
    _run_all_tests(TEST_CASES)
