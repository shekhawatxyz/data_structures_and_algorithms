# Level 1a - Stack Class Basics
# Implement a Stack class using a Python list internally.
# Support push(item), pop(), peek(), is_empty(), and size().
# Raise an appropriate error when popping or peeking an empty stack.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.items[-1]

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def size(self):
        return len(self.items)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _run_interleaved_sequence_and_capture(stack, operations):
    observations = []
    for op, value in operations:
        if op == "push":
            stack.push(value)
            observations.append((op, value, None, stack.size(), stack.peek()))
        elif op == "pop":
            popped = stack.pop()
            if stack.is_empty():
                top = None
            else:
                top = stack.peek()
            observations.append((op, value, popped, stack.size(), top))
        else:
            raise AssertionError(f"Unsupported operation {op!r} in test setup.")
    return observations


def test_01_pedagogy_starts_empty_then_single_push_behavior():
    stack = Stack()
    _assert_equal(stack.is_empty(), True, "New stack should start empty.")
    _assert_equal(stack.size(), 0, "New stack should start with size 0.")

    stack.push(10)
    _assert_equal(stack.is_empty(), False, "After one push, stack should not be empty.")
    _assert_equal(stack.size(), 1, "After one push, size should be 1.")
    _assert_equal(stack.peek(), 10, "After pushing 10, top should be 10.")


def test_02_pedagogy_lifo_progression_with_multiple_pushes():
    stack = Stack()
    for value in [1, 2, 3, 4]:
        stack.push(value)

    _assert_equal(stack.peek(), 4, "Top should be most recently pushed value (4).")
    _assert_equal(stack.pop(), 4, "First pop should return 4.")
    _assert_equal(stack.pop(), 3, "Second pop should return 3.")
    _assert_equal(stack.pop(), 2, "Third pop should return 2.")
    _assert_equal(stack.pop(), 1, "Fourth pop should return 1.")
    _assert_equal(
        stack.is_empty(), True, "Stack should be empty after popping all items."
    )


def test_03_boundaries_empty_pop_and_peek_raise_errors():
    stack = Stack()
    _assert_raises(lambda: stack.pop(), "pop() should raise on an empty stack.")
    _assert_raises(lambda: stack.peek(), "peek() should raise on an empty stack.")


def test_04_boundaries_size_off_by_one_transitions():
    stack = Stack()
    expected_sizes = [0, 1, 2, 1, 0]

    _assert_equal(stack.size(), expected_sizes[0], "Initial size should be 0.")
    stack.push("a")
    _assert_equal(stack.size(), expected_sizes[1], "Size should be 1 after first push.")
    stack.push("b")
    _assert_equal(
        stack.size(), expected_sizes[2], "Size should be 2 after second push."
    )
    stack.pop()
    _assert_equal(
        stack.size(), expected_sizes[3], "Size should return to 1 after one pop."
    )
    stack.pop()
    _assert_equal(
        stack.size(),
        expected_sizes[4],
        "Size should return to 0 after popping all items.",
    )


def test_05_interactions_interleaved_operations_keep_consistent_state():
    stack = Stack()
    operations = [
        ("push", 10),
        ("push", 20),
        ("pop", None),
        ("push", 30),
        ("push", 40),
        ("pop", None),
        ("pop", None),
        ("pop", None),
    ]

    observed = _run_interleaved_sequence_and_capture(stack, operations)
    expected = [
        ("push", 10, None, 1, 10),
        ("push", 20, None, 2, 20),
        ("pop", None, 20, 1, 10),
        ("push", 30, None, 2, 30),
        ("push", 40, None, 3, 40),
        ("pop", None, 40, 2, 30),
        ("pop", None, 30, 1, 10),
        ("pop", None, 10, 0, None),
    ]

    _assert_equal(
        observed,
        expected,
        "Interleaved operations should maintain correct pop values, sizes, and top values at each step.",
    )
    _assert_equal(
        stack.is_empty(), True, "Stack should be empty after full interleaved sequence."
    )


def test_06_interactions_duplicate_values_are_handled_independently():
    stack = Stack()
    for value in [5, 5, 5]:
        stack.push(value)

    _assert_equal(
        stack.size(),
        3,
        "Pushing three duplicate values should still create three stack entries.",
    )
    _assert_equal(stack.pop(), 5, "First pop should return top duplicate 5.")
    _assert_equal(stack.pop(), 5, "Second pop should return next duplicate 5.")
    _assert_equal(stack.pop(), 5, "Third pop should return final duplicate 5.")
    _assert_equal(
        stack.is_empty(), True, "Stack should be empty after popping all duplicates."
    )


if __name__ == "__main__":
    TEST_CASES = [
        (
            "pedagogy: empty -> single push",
            test_01_pedagogy_starts_empty_then_single_push_behavior,
        ),
        (
            "pedagogy: LIFO progression",
            test_02_pedagogy_lifo_progression_with_multiple_pushes,
        ),
        (
            "boundaries: empty pop/peek errors",
            test_03_boundaries_empty_pop_and_peek_raise_errors,
        ),
        (
            "boundaries: size transitions",
            test_04_boundaries_size_off_by_one_transitions,
        ),
        (
            "interactions: interleaved consistency",
            test_05_interactions_interleaved_operations_keep_consistent_state,
        ),
        (
            "interactions: duplicate values",
            test_06_interactions_duplicate_values_are_handled_independently,
        ),
    ]
    _run_all_tests(TEST_CASES)
