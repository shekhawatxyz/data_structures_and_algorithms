# Level 14b - Eulerian Path Exists
# Return True iff the graph admits an Eulerian path (not necessarily a circuit).

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 14b — `eulerian_path_exists`
# Return `True` iff the graph admits an Eulerian path (not necessarily a circuit).

def eulerian_path_exists(adj, directed):
    raise NotImplementedError('Implement eulerian_path_exists(adj, directed).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_undirected_path():
    # Path 0-1-2: exactly 2 odd-degree vertices -> Eulerian path exists
    adj = [[1], [0, 2], [1]]
    _assert_true(eulerian_path_exists(adj, directed=False),
                 "Path with 2 odd-degree vertices has Eulerian path.")


def test_02_undirected_circuit_also_path():
    # Triangle: Eulerian circuit exists, so path also exists
    adj = [[1, 2], [0, 2], [0, 1]]
    _assert_true(eulerian_path_exists(adj, directed=False),
                 "Eulerian circuit implies Eulerian path.")


def test_03_undirected_no_path():
    # 4 vertices: 0-1, 0-2, 0-3, 1-2 -> degrees: 3,2,2,1 -> 2 odd -> yes actually
    # Use different example: 0-1, 0-2, 0-3, 1-3 -> degrees: 3,2,1,2 -> 2 odd vertices
    # Better: 4 odd-degree vertices -> no Eulerian path
    # K4 minus an edge: 0-1, 0-2, 0-3, 1-2, 1-3 -> degrees: 3,3,2,2 -> 2 odd -> path exists
    # Complete K4: degrees all 3 -> 4 odd vertices -> no path
    adj = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
    _assert_true(not eulerian_path_exists(adj, directed=False),
                 "K4 has 4 odd-degree vertices, no Eulerian path.")


def test_04_directed_path():
    # 0->1->2: vertex 0 has out-in=1, vertex 2 has in-out=1, vertex 1 balanced
    adj = [[1], [2], []]
    _assert_true(eulerian_path_exists(adj, directed=True),
                 "Directed path has Eulerian path.")


def test_05_directed_no_path():
    # 0->1, 0->2: vertex 0 out-in=2, not valid
    adj = [[1, 2], [], []]
    _assert_true(not eulerian_path_exists(adj, directed=True),
                 "Fork has no Eulerian path.")


if __name__ == "__main__":
    TEST_CASES = [
        ("undirected path", test_01_pedagogy_undirected_path),
        ("circuit implies path", test_02_undirected_circuit_also_path),
        ("undirected no path", test_03_undirected_no_path),
        ("directed path", test_04_directed_path),
        ("directed no path", test_05_directed_no_path),
    ]
    _run_all_tests(TEST_CASES)
