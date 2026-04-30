# Level 1.2 - char_count
# Return a dictionary mapping each character in a string to its frequency.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 2. `char_count`
#
# ```python
# def char_count(s: str) -> dict[str, int]:
# ```
#
# Return a dictionary mapping each character in `s` to the number of times it appears.
#
# Examples:
# - `char_count("hello")` → `{"h": 1, "e": 1, "l": 2, "o": 1}`
# - `char_count("")` → `{}`
# - `char_count("aaa")` → `{"a": 3}`

def char_count(s):
    raise NotImplementedError('Implement char_count(s).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_hello():
    result = char_count("hello")
    _assert_equal(result, {"h": 1, "e": 1, "l": 2, "o": 1},
                  "char_count('hello') should count each character.")


def test_02_pedagogy_all_same():
    result = char_count("aaa")
    _assert_equal(result, {"a": 3},
                  "char_count('aaa') should return {'a': 3}.")


def test_03_boundaries_empty_string():
    result = char_count("")
    _assert_equal(result, {}, "char_count('') should return empty dict.")


def test_04_boundaries_single_char():
    result = char_count("x")
    _assert_equal(result, {"x": 1},
                  "Single character string should produce one-element dict.")


def test_05_interactions_spaces_and_punctuation():
    result = char_count("a b!")
    _assert_equal(result, {"a": 1, " ": 1, "b": 1, "!": 1},
                  "Spaces and punctuation should be counted as characters.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: hello", test_01_pedagogy_hello),
        ("pedagogy: all same chars", test_02_pedagogy_all_same),
        ("boundaries: empty string", test_03_boundaries_empty_string),
        ("boundaries: single char", test_04_boundaries_single_char),
        ("interactions: spaces and punctuation", test_05_interactions_spaces_and_punctuation),
    ]
    _run_all_tests(TEST_CASES)
