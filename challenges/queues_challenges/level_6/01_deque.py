# Level 6a - Build a deque
# Implement a fixed-capacity deque with a circular buffer.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 6a — Build a deque
#
# Implement a `Deque` class backed by a fixed-capacity circular buffer:
#
# - `push_front(x)`, `push_back(x)` — raise if full
# - `pop_front()`, `pop_back()` — raise if empty; return the removed value
# - `peek_front()`, `peek_back()` — raise if empty
# - `is_empty()`, `__len__()`
#
# All operations O(1).


class Deque:
    def __init__(self, capacity):
        self.lst = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def push_front(self, x):
        if self.count == self.capacity:
            raise OverflowError("Queue is full")
        self.head = (self.head - 1) % self.capacity
        self.lst[self.head] = x
        self.count += 1

    def push_back(self, x):
        if self.count == self.capacity:
            raise OverflowError("Queue is full")
        self.lst[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        front_value = self.lst[self.head]
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return front_value

    def pop_back(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.tail = (self.tail - 1) % self.capacity
        back_value = self.lst[self.tail]
        self.count -= 1
        return back_value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.lst[self.head]

    def peek_back(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        temp_tail = (self.tail - 1) % self.capacity
        return self.lst[temp_tail]

    def is_empty(self):
        return self.count == 0

    def __len__(self):
        return self.count


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


def test_push_pop_both_ends():
    dq = Deque(4)
    dq.push_back(2)
    dq.push_front(1)
    dq.push_back(3)
    _assert_equal(dq.peek_front(), 1, "front peek should return front item.")
    _assert_equal(dq.peek_back(), 3, "back peek should return back item.")
    _assert_equal(
        [dq.pop_front(), dq.pop_back(), dq.pop_front()],
        [1, 3, 2],
        "deque should remove from both ends correctly.",
    )


def test_wraparound_and_len():
    dq = Deque(3)
    dq.push_back("a")
    dq.push_back("b")
    _assert_equal(dq.pop_front(), "a", "first front pop should work.")
    dq.push_back("c")
    dq.push_front("z")
    _assert_equal(len(dq), 3, "len should track wraparound state.")
    _assert_equal(
        [dq.pop_front(), dq.pop_front(), dq.pop_front()],
        ["z", "b", "c"],
        "wrapped deque should preserve order.",
    )
    _assert_true(dq.is_empty(), "deque should be empty after all pops.")


def test_full_and_empty_raise():
    dq = Deque(2)
    _assert_raises(
        IndexError, dq.pop_front, "pop_front on empty deque should raise IndexError."
    )
    _assert_raises(
        IndexError, dq.pop_back, "pop_back on empty deque should raise IndexError."
    )
    _assert_raises(
        IndexError, dq.peek_front, "peek_front on empty deque should raise IndexError."
    )
    _assert_raises(
        IndexError, dq.peek_back, "peek_back on empty deque should raise IndexError."
    )
    dq.push_front(1)
    dq.push_back(2)
    _assert_raises(
        OverflowError,
        lambda: dq.push_back(3),
        "push_back on full deque should raise OverflowError.",
    )
    _assert_raises(
        OverflowError,
        lambda: dq.push_front(0),
        "push_front on full deque should raise OverflowError.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("push pop both ends", test_push_pop_both_ends),
        ("wraparound and len", test_wraparound_and_len),
        ("full and empty raise", test_full_and_empty_raise),
    ]
    _run_all_tests(TEST_CASES)
