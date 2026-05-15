# Level 5a - Stack using a queue
# Implement a stack backed by exactly one queue.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 5a — Stack using a queue
#
# Implement a `QueueStack` class with the operations of a stack:
#
# - `push(x)`, `pop()`, `top()`, `is_empty()`, `__len__()`
#
# Internally use exactly one queue (with the operations from 1a/1b). One of `push` and `pop` will be O(n); choose which.
from typing import List


class ListQueue:
    def __init__(self):
        self.lst = []

    def enqueue(self, x):
        self.lst.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        return self.lst.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.lst[0]

    def is_empty(self):
        return self.__len__() == 0

    def __len__(self):
        return len(self.lst)


class QueueStack:
    def __init__(self):
        self._queue = ListQueue()

    def push(self, x):
        current_length = len(self._queue)
        self._queue.enqueue(x)
        counter = 0
        while counter < current_length:
            self._queue.enqueue(self._queue.dequeue())
            counter += 1

    def pop(self):
        return self._queue.dequeue()

    def top(self):
        return self._queue.peek()

    def is_empty(self):
        return len(self._queue) == 0

    def __len__(self):
        return len(self._queue)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _assert_raises(expected_exception, callable_obj, context):
    try:
        callable_obj()
    except expected_exception:
        return
    except Exception as exc:
        raise AssertionError(
            f"{context} Expected {expected_exception.__name__}, "
            f"got {type(exc).__name__}: {exc}."
        ) from exc
    raise AssertionError(
        f"{context} Expected {expected_exception.__name__}, but none was raised."
    )


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


def test_lifo_order_and_top():
    stack = QueueStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    _assert_equal(stack.top(), 3, "top should return most recent item.")
    _assert_equal(
        [stack.pop(), stack.pop(), stack.pop()],
        [3, 2, 1],
        "pop should return items in LIFO order.",
    )


def test_empty_state_and_len():
    stack = QueueStack()
    _assert_true(stack.is_empty(), "new stack should be empty.")
    stack.push("x")
    _assert_equal(len(stack), 1, "len should count pushed items.")
    _assert_true(not stack.is_empty(), "non-empty stack should report not empty.")
    _assert_equal(stack.pop(), "x", "single item should pop correctly.")
    _assert_true(stack.is_empty(), "stack should be empty after pop.")


def test_empty_operations_raise():
    stack = QueueStack()
    _assert_raises(IndexError, stack.pop, "pop on empty stack should raise IndexError.")
    _assert_raises(IndexError, stack.top, "top on empty stack should raise IndexError.")


if __name__ == "__main__":
    TEST_CASES = [
        ("LIFO order and top", test_lifo_order_and_top),
        ("empty state and len", test_empty_state_and_len),
        ("empty operations raise", test_empty_operations_raise),
    ]
    _run_all_tests(TEST_CASES)
