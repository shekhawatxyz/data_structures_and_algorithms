# Level 1b - Queue with a circular buffer
# Implement RingQueue with fixed capacity and O(1) operations.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 1b — Queue with a circular buffer
#
# Implement a `RingQueue` class with the same operations as `ListQueue`, but:
#
# - Backed by a fixed-capacity Python list, allocated once and never resized.
# - Every operation runs in O(1).
# - `enqueue` raises if the queue is full.
#
# ```
# q = RingQueue(capacity=3)
# q.enqueue(1); q.enqueue(2); q.enqueue(3)
# q.dequeue()        # 1
# q.enqueue(4)       # OK — wraps
# q.dequeue()        # 2
# ```


class RingQueue:
    def __init__(self, capacity):
        self.lst = [None] * capacity
        self.capacity = capacity
        self.count = 0
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if self.__len__() == self.capacity:
            raise OverflowError("queue is at capacity")
        self.lst[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return_val = self.lst[self.head]
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return return_val

    def peek(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.lst[self.head]

    def is_empty(self):
        return self.__len__() == 0

    def __len__(self):
        return self.count


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


def test_wraparound_preserves_fifo():
    q = RingQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    _assert_equal(q.dequeue(), 1, "first item should leave first.")
    q.enqueue(4)
    _assert_equal(
        [q.dequeue(), q.dequeue(), q.dequeue()],
        [2, 3, 4],
        "queue should preserve FIFO order across wraparound.",
    )


def test_full_and_empty_raise():
    q = RingQueue(2)
    q.enqueue("a")
    q.enqueue("b")
    _assert_raises(
        OverflowError,
        lambda: q.enqueue("c"),
        "enqueue on a full queue should raise OverflowError.",
    )
    _assert_equal(q.dequeue(), "a", "first item should still be present.")
    _assert_equal(q.dequeue(), "b", "second item should still be present.")
    _assert_raises(
        IndexError, q.dequeue, "dequeue on empty queue should raise IndexError."
    )
    _assert_raises(IndexError, q.peek, "peek on empty queue should raise IndexError.")


def test_len_and_peek():
    q = RingQueue(2)
    _assert_true(q.is_empty(), "new queue should be empty.")
    q.enqueue(10)
    _assert_equal(q.peek(), 10, "peek should not remove the front.")
    _assert_equal(len(q), 1, "len should count active items.")
    _assert_equal(q.dequeue(), 10, "front should remain after peek.")


if __name__ == "__main__":
    TEST_CASES = [
        ("wraparound preserves FIFO", test_wraparound_preserves_fifo),
        ("full and empty raise", test_full_and_empty_raise),
        ("len and peek", test_len_and_peek),
    ]
    _run_all_tests(TEST_CASES)
