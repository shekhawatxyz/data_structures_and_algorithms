# Level 4b - Reverse the first k elements
# Reverse the first k queue elements in place.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 4b — Reverse the first k elements
#
# ```python
# def reverse_first_k(q, k: int) -> None:
#     ...
# ```
#
# Reverse the first `k` elements of `q` in place, leaving the remaining elements in their original order. You may use one auxiliary stack. Assume `0 <= k <= len(q)`.
#
# ```
# q: front [1, 2, 3, 4, 5, 6] back, k = 3
# reverse_first_k(q, 3)
# q: front [3, 2, 1, 4, 5, 6] back
# ```

def reverse_first_k(q, k):
    raise NotImplementedError("Implement reverse_first_k(q, k).")

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


class SimpleQueue:
    def __init__(self, values=()):
        self._items = list(values)

    def enqueue(self, x):
        self._items.append(x)

    def dequeue(self):
        if not self._items:
            raise IndexError("empty queue")
        return self._items.pop(0)

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


def _to_list(q):
    result = []
    for _ in range(len(q)):
        value = q.dequeue()
        result.append(value)
        q.enqueue(value)
    return result


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
    q = SimpleQueue([1, 2, 3, 4, 5, 6])
    reverse_first_k(q, 3)
    _assert_equal(_to_list(q), [3, 2, 1, 4, 5, 6],
                  "first k elements should be reversed only.")


def test_zero_and_full_length():
    q = SimpleQueue([1, 2, 3])
    reverse_first_k(q, 0)
    _assert_equal(_to_list(q), [1, 2, 3], "k=0 should leave queue unchanged.")
    reverse_first_k(q, 3)
    _assert_equal(_to_list(q), [3, 2, 1], "k=len(q) should reverse the whole queue.")


def test_invalid_k_raises():
    _assert_raises(ValueError, lambda: reverse_first_k(SimpleQueue([1, 2]), -1),
                   "negative k should raise ValueError.")
    _assert_raises(ValueError, lambda: reverse_first_k(SimpleQueue([1, 2]), 3),
                   "k greater than len(q) should raise ValueError.")


if __name__ == "__main__":
    TEST_CASES = [
        ("sample", test_sample),
        ("zero and full length", test_zero_and_full_length),
        ("invalid k raises", test_invalid_k_raises),
    ]
    _run_all_tests(TEST_CASES)
