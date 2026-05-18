# Level 9a - Queue with getMax
# Implement a queue that can return its maximum in O(1) amortized time.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 9a — Queue with getMax in O(1) amortized
#
# Implement a `MaxQueue` class:
#
# - `enqueue(x)`
# - `dequeue()` — return the removed value; raise on empty
# - `get_max()` — return the maximum element currently in the queue; raise on empty
#
# All three operations should run in O(1) amortized time.
#
# ```
# q = MaxQueue()
# q.enqueue(3); q.enqueue(1); q.enqueue(5)
# q.get_max()        # 5
# q.dequeue()        # 3
# q.get_max()        # 5
# q.dequeue()        # 1
# q.get_max()        # 5
# ```
from collections import deque


class MaxQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.dq = deque()

    def enqueue(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
            self.dq.append(new_node.data)
        else:
            while self.dq and new_node.data > self.dq[-1]:
                self.dq.pop()
            self.dq.append(new_node.data)
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            raise IndexError("Empty queue")
        if self.head.data == self.dq[0]:
            self.dq.popleft()
        return_value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return return_value

    def get_max(self):
        if not self.dq:
            raise IndexError("Empty queue")
        return self.dq[0]


class Node:
    def __init__(self, x) -> None:
        self.next = None
        self.data = x


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


def test_sample_sequence():
    q = MaxQueue()
    q.enqueue(3)
    q.enqueue(1)
    q.enqueue(5)
    _assert_equal(q.get_max(), 5, "max should be 5 after enqueueing 3, 1, 5.")
    _assert_equal(q.dequeue(), 3, "dequeue should remove from the front.")
    _assert_equal(q.get_max(), 5, "max should remain 5.")
    _assert_equal(q.dequeue(), 1, "second dequeue should remove 1.")
    _assert_equal(q.get_max(), 5, "max should still be 5.")


def test_duplicate_max_values():
    q = MaxQueue()
    for value in [4, 4, 2]:
        q.enqueue(value)
    _assert_equal(q.get_max(), 4, "duplicate max should be reported.")
    _assert_equal(q.dequeue(), 4, "front duplicate max should dequeue.")
    _assert_equal(q.get_max(), 4, "second duplicate max should remain.")


def test_empty_operations_raise():
    q = MaxQueue()
    _assert_raises(
        IndexError, q.dequeue, "dequeue on empty queue should raise IndexError."
    )
    _assert_raises(
        IndexError, q.get_max, "get_max on empty queue should raise IndexError."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("sample sequence", test_sample_sequence),
        ("duplicate max values", test_duplicate_max_values),
        ("empty operations raise", test_empty_operations_raise),
    ]
    _run_all_tests(TEST_CASES)
