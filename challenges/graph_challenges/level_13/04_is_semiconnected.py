# Level 13d - Is Semiconnected
# Check if a directed graph is semiconnected.

# Complete Exact Problem Statement (from graph-challenges.md):
# ### 13d — `is_semiconnected`
# A directed graph is semiconnected iff for every pair `(u, v)`, at least one of `u → v` or `v → u` is reachable. Hint: think about the condensation.

def is_semiconnected(adj):
    raise NotImplementedError('Implement is_semiconnected(adj).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_strongly_connected():
    # Strongly connected is also semiconnected
    adj = [[1], [2], [0]]
    _assert_true(is_semiconnected(adj), "Strongly connected -> semiconnected.")


def test_02_chain_is_semiconnected():
    # 0->1->2: for any pair, one can reach the other
    adj = [[1], [2], []]
    _assert_true(is_semiconnected(adj), "Chain is semiconnected.")


def test_03_fork_not_semiconnected():
    # 0->1, 0->2 but no path between 1 and 2
    adj = [[1, 2], [], []]
    _assert_true(not is_semiconnected(adj), "Fork: 1 and 2 cannot reach each other.")


def test_04_single_vertex():
    adj = [[]]
    _assert_true(is_semiconnected(adj), "Single vertex is trivially semiconnected.")


def test_05_two_sccs_in_chain():
    # 0<->1, 1->2<->3: semiconnected (chain of SCCs)
    adj = [[1], [0, 2], [3], [2]]
    _assert_true(is_semiconnected(adj), "Chain of SCCs is semiconnected.")


if __name__ == "__main__":
    TEST_CASES = [
        ("strongly connected", test_01_pedagogy_strongly_connected),
        ("chain", test_02_chain_is_semiconnected),
        ("fork not semiconnected", test_03_fork_not_semiconnected),
        ("single vertex", test_04_single_vertex),
        ("chain of SCCs", test_05_two_sccs_in_chain),
    ]
    _run_all_tests(TEST_CASES)
