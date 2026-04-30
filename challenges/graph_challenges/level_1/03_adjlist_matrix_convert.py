# Level 1c - Adjacency List / Matrix Conversion
# Convert between adjacency list and adjacency matrix representations.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 1c — `adjlist_to_matrix` and `matrix_to_adjlist`
# Convert between the two representations. Two functions.

def adjlist_to_matrix(adj):
    raise NotImplementedError('Implement adjlist_to_matrix(adj).')


def matrix_to_adjlist(matrix):
    raise NotImplementedError('Implement matrix_to_adjlist(matrix).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_adjlist_to_matrix_triangle():
    adj = [[1, 2], [0, 2], [0, 1]]
    expected = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    _assert_equal(adjlist_to_matrix(adj), expected, "Triangle adjlist to matrix.")


def test_02_matrix_to_adjlist_triangle():
    matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    adj = matrix_to_adjlist(matrix)
    _assert_equal(sorted(adj[0]), [1, 2], "Vertex 0 from matrix.")
    _assert_equal(sorted(adj[1]), [0, 2], "Vertex 1 from matrix.")
    _assert_equal(sorted(adj[2]), [0, 1], "Vertex 2 from matrix.")


def test_03_empty_graph():
    adj = [[], [], []]
    mat = adjlist_to_matrix(adj)
    _assert_equal(mat, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "Empty adjlist to matrix.")
    adj_back = matrix_to_adjlist(mat)
    _assert_equal(adj_back, [[], [], []], "Empty matrix to adjlist.")


def test_04_directed_conversion():
    # Directed: 0->1, 1->2
    adj = [[1], [2], []]
    mat = adjlist_to_matrix(adj)
    _assert_equal(mat, [[0, 1, 0], [0, 0, 1], [0, 0, 0]], "Directed adjlist to matrix.")
    adj_back = matrix_to_adjlist(mat)
    _assert_equal(adj_back, [[1], [2], []], "Directed matrix to adjlist.")


def test_05_single_node():
    adj = [[]]
    _assert_equal(adjlist_to_matrix(adj), [[0]], "Single node adjlist to matrix.")
    _assert_equal(matrix_to_adjlist([[0]]), [[]], "Single node matrix to adjlist.")


if __name__ == "__main__":
    TEST_CASES = [
        ("adjlist to matrix triangle", test_01_adjlist_to_matrix_triangle),
        ("matrix to adjlist triangle", test_02_matrix_to_adjlist_triangle),
        ("empty graph roundtrip", test_03_empty_graph),
        ("directed conversion", test_04_directed_conversion),
        ("single node", test_05_single_node),
    ]
    _run_all_tests(TEST_CASES)
