# Level 1a - Queue with a list
# Implement ListQueue backed by a plain Python list.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 1a — Queue with a list
#
# Implement a `ListQueue` class backed by a plain Python list:
#
# - `enqueue(x)` — add `x` to the back
# - `dequeue()` — remove and return the front; raise on empty
# - `peek()` — return the front without removing; raise on empty
# - `is_empty() -> bool`
# - `__len__() -> int`
#
# You don't need to worry about the asymptotic cost of `dequeue`.
#
# ```
# q = ListQueue()
# q.enqueue(1); q.enqueue(2); q.enqueue(3)
# q.dequeue()    # 1
# q.peek()       # 2
# len(q)         # 2
# ```

class ListQueue:
    def __init__(self):
        raise NotImplementedError("Implement ListQueue.__init__().")

    def enqueue(self, x):
        raise NotImplementedError("Implement ListQueue.enqueue(x).")

    def dequeue(self):
        raise NotImplementedError("Implement ListQueue.dequeue().")

    def peek(self):
        raise NotImplementedError("Implement ListQueue.peek().")

    def is_empty(self):
        raise NotImplementedError("Implement ListQueue.is_empty().")

    def __len__(self):
        raise NotImplementedError("Implement ListQueue.__len__().")

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


def test_basic_fifo_and_peek():
    q = ListQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    _assert_equal(q.peek(), 1, "peek should return the front item.")
    _assert_equal(q.dequeue(), 1, "dequeue should remove the first item.")
    _assert_equal(q.dequeue(), 2, "dequeue should preserve FIFO order.")
    _assert_equal(len(q), 1, "len should track remaining items.")


def test_empty_state_transitions():
    q = ListQueue()
    _assert_true(q.is_empty(), "new queue should be empty.")
    q.enqueue("x")
    _assert_true(not q.is_empty(), "queue with one item should not be empty.")
    _assert_equal(q.dequeue(), "x", "single item should dequeue correctly.")
    _assert_true(q.is_empty(), "queue should be empty after removing all items.")


def test_empty_operations_raise():
    q = ListQueue()
    _assert_raises(IndexError, q.dequeue, "dequeue on empty queue should raise IndexError.")
    _assert_raises(IndexError, q.peek, "peek on empty queue should raise IndexError.")


if __name__ == "__main__":
    TEST_CASES = [
        ("basic FIFO and peek", test_basic_fifo_and_peek),
        ("empty state transitions", test_empty_state_transitions),
        ("empty operations raise", test_empty_operations_raise),
    ]
    _run_all_tests(TEST_CASES)
