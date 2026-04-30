# Level 3b - First non-repeating character in a stream
# Track the earliest character that has appeared exactly once.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 3b — First non-repeating character in a stream
#
# ```python
# def first_unique_stream(stream: str) -> list[str]:
#     ...
# ```
#
# After reading each character of `stream` in order, return the earliest character (among all characters seen so far) that has appeared exactly once. If no such character exists at that point, return `"#"` for that step.
#
# The output list has one entry per character in `stream`. Assume the alphabet is fixed and small (lowercase ASCII), so a length-26 array of counts is fair game; no general hash maps.
#
# ```
# first_unique_stream("aabc")    # ["a", "#", "b", "b"]
# first_unique_stream("aabbcc")  # ["a", "#", "b", "#", "c", "#"]
# ```

def first_unique_stream(stream):
    raise NotImplementedError("Implement first_unique_stream(stream).")

#
#
#
#
#


def _assert_equal(actual, expected, context):
    if actual != expected:
        raise AssertionError(f"{context} Expected {expected!r}, got {actual!r}.")


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
    for name, fn in test_cases:
        if _run_test(name, fn):
            passed += 1
    print(f"\nPassed {passed}/{len(test_cases)} tests.")
    if passed != len(test_cases):
        raise SystemExit(1)


def test_samples():
    _assert_equal(first_unique_stream("aabc"), ["a", "#", "b", "b"],
                  "sample stream aabc should match expected outputs.")
    _assert_equal(first_unique_stream("aabbcc"), ["a", "#", "b", "#", "c", "#"],
                  "sample stream aabbcc should match expected outputs.")


def test_empty_stream():
    _assert_equal(first_unique_stream(""), [], "empty stream should produce no outputs.")


def test_unique_can_return_to_later_character():
    _assert_equal(first_unique_stream("abac"), ["a", "a", "b", "b"],
                  "queue should discard repeated earlier characters.")


if __name__ == "__main__":
    TEST_CASES = [
        ("samples", test_samples),
        ("empty stream", test_empty_stream),
        ("unique can return to later character", test_unique_can_return_to_later_character),
    ]
    _run_all_tests(TEST_CASES)
