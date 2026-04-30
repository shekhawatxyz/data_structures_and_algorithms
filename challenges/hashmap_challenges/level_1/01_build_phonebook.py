# Level 1.1 - build_phonebook
# Build a dictionary mapping names to phone numbers from a list of tuples.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 1. `build_phonebook`
#
# ```python
# def build_phonebook(entries: list[tuple[str, str]]) -> dict[str, str]:
# ```
#
# Given a list of `(name, number)` tuples, return a dictionary mapping each name to its number. If the same name appears more than once, the later number takes precedence.
#
# Examples:
# - `build_phonebook([("Alice", "555-1234"), ("Bob", "555-9876")])` → `{"Alice": "555-1234", "Bob": "555-9876"}`
# - `build_phonebook([("Alice", "555-1234"), ("Alice", "555-0000")])` → `{"Alice": "555-0000"}`
# - `build_phonebook([])` → `{}`

def build_phonebook(entries):
    raise NotImplementedError('Implement build_phonebook(entries).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_two_distinct_entries():
    result = build_phonebook([("Alice", "555-1234"), ("Bob", "555-9876")])
    _assert_equal(result, {"Alice": "555-1234", "Bob": "555-9876"},
                  "Two distinct entries should map each name to its number.")


def test_02_pedagogy_duplicate_name_takes_later():
    result = build_phonebook([("Alice", "555-1234"), ("Alice", "555-0000")])
    _assert_equal(result, {"Alice": "555-0000"},
                  "Duplicate name should keep the later number.")


def test_03_boundaries_empty_input():
    result = build_phonebook([])
    _assert_equal(result, {}, "Empty input should return empty dict.")


def test_04_boundaries_single_entry():
    result = build_phonebook([("Zara", "111-2222")])
    _assert_equal(result, {"Zara": "111-2222"},
                  "Single entry should produce a one-element dict.")


def test_05_interactions_multiple_duplicates():
    result = build_phonebook([
        ("A", "1"), ("B", "2"), ("A", "3"), ("B", "4"), ("A", "5")
    ])
    _assert_equal(result, {"A": "5", "B": "4"},
                  "Multiple duplicates should keep only the last occurrence.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: two distinct entries", test_01_pedagogy_two_distinct_entries),
        ("pedagogy: duplicate takes later", test_02_pedagogy_duplicate_name_takes_later),
        ("boundaries: empty input", test_03_boundaries_empty_input),
        ("boundaries: single entry", test_04_boundaries_single_entry),
        ("interactions: multiple duplicates", test_05_interactions_multiple_duplicates),
    ]
    _run_all_tests(TEST_CASES)
