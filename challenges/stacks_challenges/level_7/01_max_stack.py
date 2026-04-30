# Level 7a - MaxStack in O(1)
# Implement MaxStack with push, pop, peek, get_max all in O(1).
# Use only stacks internally (no other data structures).

# Complete Exact Problem Statement (from stack-challenges.md):
# **7a.** Design a `MaxStack` class that supports `push`, `pop`, `peek`, and `get_max` (returns the current maximum element), all in O(1) time. You may use additional stacks but no other data structures. (Hint: think about what information you need to preserve when you push, and what you need to restore when you pop.)

class MaxStack:
    def __init__(self):
        raise NotImplementedError('Implement MaxStack.__init__().')

    def push(self, item):
        raise NotImplementedError('Implement MaxStack.push(item).')

    def pop(self):
        raise NotImplementedError('Implement MaxStack.pop().')

    def peek(self):
        raise NotImplementedError('Implement MaxStack.peek().')

    def get_max(self):
        raise NotImplementedError('Implement MaxStack.get_max().')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_get_max_progression_while_pushing():
    stack = MaxStack()
    sequence = [3, 1, 5, 2, 5]
    expected_maxes = [3, 3, 5, 5, 5]

    for index, (value, expected_max) in enumerate(
        zip(sequence, expected_maxes), start=1
    ):
        stack.push(value)
        _assert_equal(
            stack.get_max(),
            expected_max,
            f"After push #{index} of value {value}, get_max() should be {expected_max}.",
        )


def test_02_pedagogy_lifo_and_max_update_while_popping():
    stack = MaxStack()
    for value in [2, 7, 7, 3]:
        stack.push(value)

    _assert_equal(stack.pop(), 3, "First pop should return 3 (top of stack).")
    _assert_equal(
        stack.get_max(), 7, "Max should remain 7 after popping non-max value 3."
    )
    _assert_equal(stack.pop(), 7, "Next pop should return top-most 7.")
    _assert_equal(stack.get_max(), 7, "Duplicate 7 remains, so max should still be 7.")
    _assert_equal(stack.pop(), 7, "Second 7 should pop next.")
    _assert_equal(
        stack.get_max(), 2, "After all 7s are removed, max should update to 2."
    )


def test_03_boundaries_empty_stack_operations_raise():
    stack = MaxStack()
    _assert_raises(lambda: stack.pop(), "pop() on empty MaxStack should raise.")
    _assert_raises(lambda: stack.peek(), "peek() on empty MaxStack should raise.")
    _assert_raises(lambda: stack.get_max(), "get_max() on empty MaxStack should raise.")


def test_04_boundaries_duplicate_max_values_are_tracked_correctly():
    stack = MaxStack()
    for value in [5, 5, 5]:
        stack.push(value)

    _assert_equal(stack.get_max(), 5, "Max should be 5 after pushing duplicate maxima.")
    stack.pop()
    _assert_equal(
        stack.get_max(), 5, "Max should stay 5 after popping one duplicate max."
    )
    stack.pop()
    _assert_equal(
        stack.get_max(),
        5,
        "Max should still stay 5 until all max duplicates are removed.",
    )


def test_05_interactions_negative_and_positive_mix():
    stack = MaxStack()
    for value in [-10, -3, -20, 0, -1]:
        stack.push(value)

    _assert_equal(
        stack.get_max(), 0, "Max should become 0 when non-negative value is introduced."
    )
    _assert_equal(
        stack.pop(), -1, "Top should pop in LIFO order even with mixed signs."
    )
    _assert_equal(stack.get_max(), 0, "Max should remain 0 after popping -1.")
    _assert_equal(stack.pop(), 0, "Popping 0 should remove the current max.")
    _assert_equal(stack.get_max(), -3, "Max should fall back to -3 after removing 0.")


def test_06_interactions_interleaved_push_pop_peek_get_max():
    stack = MaxStack()
    stack.push(4)
    _assert_equal(stack.peek(), 4, "peek should show top 4 after first push.")
    _assert_equal(stack.get_max(), 4, "max should be 4 after first push.")

    stack.push(1)
    _assert_equal(stack.peek(), 1, "peek should update to 1 after pushing 1.")
    _assert_equal(
        stack.get_max(), 4, "max should remain 4 after pushing smaller value 1."
    )

    stack.push(6)
    _assert_equal(stack.get_max(), 6, "max should update to 6 after pushing 6.")
    _assert_equal(stack.pop(), 6, "pop should remove 6 first.")
    _assert_equal(stack.peek(), 1, "peek should revert to 1 after popping 6.")
    _assert_equal(stack.get_max(), 4, "max should revert to 4 after popping 6.")


if __name__ == "__main__":
    TEST_CASES = [
        (
            "pedagogy: max progression on push",
            test_01_pedagogy_get_max_progression_while_pushing,
        ),
        (
            "pedagogy: lifo + max updates on pop",
            test_02_pedagogy_lifo_and_max_update_while_popping,
        ),
        (
            "boundaries: empty operations raise",
            test_03_boundaries_empty_stack_operations_raise,
        ),
        (
            "boundaries: duplicate maxima",
            test_04_boundaries_duplicate_max_values_are_tracked_correctly,
        ),
        (
            "interactions: mixed sign values",
            test_05_interactions_negative_and_positive_mix,
        ),
        (
            "interactions: interleaved ops",
            test_06_interactions_interleaved_push_pop_peek_get_max,
        ),
    ]
    _run_all_tests(TEST_CASES)
