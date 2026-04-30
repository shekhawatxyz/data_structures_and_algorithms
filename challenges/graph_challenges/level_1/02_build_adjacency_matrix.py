# Level 1b - Build Adjacency Matrix
# Build an adjacency matrix from a list of edges and a vertex count.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 1b — `build_adjacency_matrix`
# Same input, but output is an `n × n` matrix.
# ```python
# def build_adjacency_matrix(n: int, edges: list[tuple[int, int]], directed: bool) -> list[list[int]]
# ```

def build_adjacency_matrix(n, edges, directed):
    raise NotImplementedError('Implement build_adjacency_matrix(n, edges, directed).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_undirected_triangle():
    mat = build_adjacency_matrix(3, [(0, 1), (1, 2), (0, 2)], directed=False)
    expected = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]
    _assert_equal(mat, expected, "Undirected triangle matrix.")


def test_02_directed_graph():
    mat = build_adjacency_matrix(3, [(0, 1), (1, 2)], directed=True)
    expected = [
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0],
    ]
    _assert_equal(mat, expected, "Directed graph matrix.")


def test_03_empty_graph():
    mat = build_adjacency_matrix(3, [], directed=False)
    expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    _assert_equal(mat, expected, "Empty graph matrix.")


def test_04_single_node():
    mat = build_adjacency_matrix(1, [], directed=False)
    _assert_equal(mat, [[0]], "Single node matrix.")


def test_05_directed_star():
    mat = build_adjacency_matrix(4, [(0, 1), (0, 2), (0, 3)], directed=True)
    _assert_equal(mat[0], [0, 1, 1, 1], "Row 0 of directed star.")
    _assert_equal(mat[1], [0, 0, 0, 0], "Row 1 of directed star.")


if __name__ == "__main__":
    TEST_CASES = [
        ("undirected triangle", test_01_undirected_triangle),
        ("directed graph", test_02_directed_graph),
        ("empty graph", test_03_empty_graph),
        ("single node", test_04_single_node),
        ("directed star", test_05_directed_star),
    ]
    _run_all_tests(TEST_CASES)
