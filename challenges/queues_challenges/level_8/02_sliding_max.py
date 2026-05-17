# Level 9b - Sliding window maximum
# Return the maximum value in each window of size k.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 8b — Sliding window maximum
#
# ```python
# def sliding_max(values: list[int], k: int) -> list[int]:
#     ...
# ```
#
# For each contiguous window of size `k`, return the maximum value in the window. The amortized cost per window should be O(1).
#
# ```
# sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3)
# # [3, 3, 5, 5, 6, 7]
# ```
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


# def first_negative_each_window(values, k):
#     if k < 1:
#         raise ValueError("Cannot slice if less than 1.")
#     if k > len(values):
#         raise ValueError("Cannot slice if bigger than the list")
#     result = [0] * (len(values) - k + 1)
#     deque = Deque(k)
#     for i in range(k):
#         if values[i] < 0:
#             deque.push_back((values[i], i))
#     if not deque.is_empty():
#         result[0] = deque.peek_front()[0]
#     for i in range(k, len(values)):
#         if values[i] < 0:
#             deque.push_back((values[i], i))
#         if not deque.is_empty():
#             if i - k == deque.peek_front()[1]:
#                 deque.pop_front()
#         if not deque.is_empty():
#             result[i - k + 1] = deque.peek_front()[0]
#     return result


def sliding_max(values, k):
    n = len(values)
    dq = Deque(k)
    if k < 1:
        raise ValueError("Cannot slice if less than 1.")
    if k > len(values):
        raise ValueError("Cannot slice if bigger than the list")
    result = [0] * (n - k + 1)
    for i in range(k):
        while not dq.is_empty() and dq.peek_back()[0] <= values[i]:
            dq.pop_back()
        dq.push_back((values[i], i))
    result[0] = dq.peek_front()[0]
    for i in range(k, n):
        if dq.peek_front()[1] == i - k:
            dq.pop_front()
        while not dq.is_empty() and dq.peek_back()[0] <= values[i]:
            dq.pop_back()
        dq.push_back((values[i], i))
        result[i - k + 1] = dq.peek_front()[0]
    return result


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


def test_sample():
    values = [1, 3, -1, -3, 5, 3, 6, 7]
    _assert_equal(
        sliding_max(values, 3),
        [3, 3, 5, 5, 6, 7],
        "sample windows should match expected maxima.",
    )


def test_duplicates_and_k_one():
    _assert_equal(
        sliding_max([4, 4, 4], 2),
        [4, 4],
        "duplicate maxima should be handled correctly.",
    )
    _assert_equal(
        sliding_max([2, -1, 5], 1), [2, -1, 5], "k=1 should return the original values."
    )


def test_invalid_k_raises():
    _assert_raises(
        ValueError, lambda: sliding_max([1, 2], 0), "k=0 should raise ValueError."
    )
    _assert_raises(
        ValueError,
        lambda: sliding_max([1, 2], 3),
        "k larger than values length should raise ValueError.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("sample", test_sample),
        ("duplicates and k one", test_duplicates_and_k_one),
        ("invalid k raises", test_invalid_k_raises),
    ]
    _run_all_tests(TEST_CASES)
