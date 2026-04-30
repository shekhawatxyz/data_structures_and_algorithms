# Level 4.1 - isomorphic_strings
# Determine if two strings are isomorphic (bijective character mapping).

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 11. `isomorphic_strings`
#
# ```python
# def isomorphic_strings(s: str, t: str) -> bool:
# ```
#
# Two strings are *isomorphic* if there is a bijection between the characters of `s` and the characters of `t` such that replacing each character of `s` according to the mapping yields `t`. Two different characters in `s` cannot map to the same character in `t`, and a single character in `s` cannot map to two different characters in `t`. The two strings have equal length.
#
# Examples:
# - `isomorphic_strings("egg", "add")` → `True`
# - `isomorphic_strings("foo", "bar")` → `False`
# - `isomorphic_strings("paper", "title")` → `True`
# - `isomorphic_strings("badc", "baba")` → `False`
# - `isomorphic_strings("ab", "aa")` → `False`

def isomorphic_strings(s, t):
    raise NotImplementedError('Implement isomorphic_strings(s, t).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_isomorphic():
    _assert_equal(isomorphic_strings("egg", "add"), True,
                  "'egg' -> 'add': e->a, g->d is a valid bijection.")


def test_02_pedagogy_not_isomorphic():
    _assert_equal(isomorphic_strings("foo", "bar"), False,
                  "'foo' -> 'bar': o maps to both a and r, invalid.")


def test_03_pedagogy_isomorphic_longer():
    _assert_equal(isomorphic_strings("paper", "title"), True,
                  "'paper' -> 'title': p->t, a->i, e->l, r->e is valid.")


def test_04_boundaries_reverse_mapping_conflict():
    _assert_equal(isomorphic_strings("badc", "baba"), False,
                  "Two different chars in s cannot map to same char in t.")


def test_05_boundaries_two_to_one_mapping():
    _assert_equal(isomorphic_strings("ab", "aa"), False,
                  "a->a and b->a violates bijection (two map to one).")


def test_06_interactions_single_char():
    _assert_equal(isomorphic_strings("a", "z"), True,
                  "Single char strings are always isomorphic.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: isomorphic egg/add", test_01_pedagogy_isomorphic),
        ("pedagogy: not isomorphic foo/bar", test_02_pedagogy_not_isomorphic),
        ("pedagogy: isomorphic paper/title", test_03_pedagogy_isomorphic_longer),
        ("boundaries: reverse mapping conflict", test_04_boundaries_reverse_mapping_conflict),
        ("boundaries: two-to-one mapping", test_05_boundaries_two_to_one_mapping),
        ("interactions: single char", test_06_interactions_single_char),
    ]
    _run_all_tests(TEST_CASES)
