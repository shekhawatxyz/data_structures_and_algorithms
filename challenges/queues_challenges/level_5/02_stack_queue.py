# Level 5b - Queue using two stacks
# Implement a queue backed by exactly two stacks.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 5b — Queue using two stacks
#
# Implement a `StackQueue` class with the operations of `ListQueue` (1a), but internally backed by exactly two stacks. Each `enqueue`, `dequeue`, and `peek` should run in O(1) **amortized** time.

class StackQueue:
    def __init__(self):
        raise NotImplementedError("Implement StackQueue.__init__().")

    def enqueue(self, x):
        raise NotImplementedError("Implement StackQueue.enqueue(x).")

    def dequeue(self):
        raise NotImplementedError("Implement StackQueue.dequeue().")

    def peek(self):
        raise NotImplementedError("Implement StackQueue.peek().")

    def is_empty(self):
        raise NotImplementedError("Implement StackQueue.is_empty().")

    def __len__(self):
        raise NotImplementedError("Implement StackQueue.__len__().")

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


def test_fifo_order_across_transfers():
    q = StackQueue()
    q.enqueue(1)
    q.enqueue(2)
    _assert_equal(q.dequeue(), 1, "first item should leave first.")
    q.enqueue(3)
    q.enqueue(4)
    _assert_equal([q.dequeue(), q.dequeue(), q.dequeue()], [2, 3, 4],
                  "queue should stay FIFO across stack transfers.")


def test_peek_len_and_empty():
    q = StackQueue()
    _assert_true(q.is_empty(), "new queue should be empty.")
    q.enqueue("a")
    q.enqueue("b")
    _assert_equal(q.peek(), "a", "peek should return front without removing it.")
    _assert_equal(len(q), 2, "len should include both stacks.")
    _assert_equal(q.dequeue(), "a", "peek should not remove the front.")


def test_empty_operations_raise():
    q = StackQueue()
    _assert_raises(IndexError, q.dequeue, "dequeue on empty queue should raise IndexError.")
    _assert_raises(IndexError, q.peek, "peek on empty queue should raise IndexError.")


if __name__ == "__main__":
    TEST_CASES = [
        ("FIFO order across transfers", test_fifo_order_across_transfers),
        ("peek len and empty", test_peek_len_and_empty),
        ("empty operations raise", test_empty_operations_raise),
    ]
    _run_all_tests(TEST_CASES)
