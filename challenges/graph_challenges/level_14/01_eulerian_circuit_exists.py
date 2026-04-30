# Level 14a - Eulerian Circuit Exists
# Return True iff the connected graph admits an Eulerian circuit.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 14a — `eulerian_circuit_exists`
# Return `True` iff the (connected) graph admits an Eulerian circuit. Handle both undirected and directed cases — the degree conditions differ.

def eulerian_circuit_exists(adj, directed):
    raise NotImplementedError('Implement eulerian_circuit_exists(adj, directed).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_undirected_triangle():
    # Triangle: all degrees 2 (even) -> Eulerian circuit exists
    adj = [[1, 2], [0, 2], [0, 1]]
    _assert_true(eulerian_circuit_exists(adj, directed=False),
                 "Triangle has Eulerian circuit (all even degree).")


def test_02_undirected_path_no_circuit():
    # Path 0-1-2: degrees 1, 2, 1 -> odd degrees exist
    adj = [[1], [0, 2], [1]]
    _assert_true(not eulerian_circuit_exists(adj, directed=False),
                 "Path has odd-degree vertices, no Eulerian circuit.")


def test_03_directed_circuit():
    # Directed cycle 0->1->2->0: in-degree == out-degree for all
    adj = [[1], [2], [0]]
    _assert_true(eulerian_circuit_exists(adj, directed=True),
                 "Directed cycle has Eulerian circuit.")


def test_04_directed_no_circuit():
    # 0->1->2: vertex 0 has out=1, in=0; not balanced
    adj = [[1], [2], []]
    _assert_true(not eulerian_circuit_exists(adj, directed=True),
                 "Directed path has no Eulerian circuit.")


def test_05_undirected_square():
    # Square 0-1-2-3-0: all degrees 2 -> circuit exists
    adj = [[1, 3], [0, 2], [1, 3], [2, 0]]
    _assert_true(eulerian_circuit_exists(adj, directed=False),
                 "Square has Eulerian circuit.")


if __name__ == "__main__":
    TEST_CASES = [
        ("undirected triangle", test_01_pedagogy_undirected_triangle),
        ("undirected path no circuit", test_02_undirected_path_no_circuit),
        ("directed circuit", test_03_directed_circuit),
        ("directed no circuit", test_04_directed_no_circuit),
        ("undirected square", test_05_undirected_square),
    ]
    _run_all_tests(TEST_CASES)
