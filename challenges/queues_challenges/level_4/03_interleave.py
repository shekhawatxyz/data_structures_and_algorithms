# Level 4c - Interleave the halves
# Interleave first and second halves of an even-length queue.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 4c — Interleave the halves
#
# ```python
# def interleave(q) -> None:
#     ...
# ```
#
# Given a queue with an even number of elements, interleave its first half with its second half. You may use one auxiliary queue or stack.
#
# ```
# q: front [1, 2, 3, 4, 5, 6] back
# interleave(q)
# q: front [1, 4, 2, 5, 3, 6] back
# ```

def interleave(q):
    raise NotImplementedError("Implement interleave(q).")

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
    interleave(q)
    _assert_equal(_to_list(q), [1, 4, 2, 5, 3, 6],
                  "halves should interleave in alternating order.")


def test_two_and_empty():
    q = SimpleQueue([1, 2])
    interleave(q)
    _assert_equal(_to_list(q), [1, 2], "two-item queue is already interleaved.")
    empty = SimpleQueue()
    interleave(empty)
    _assert_equal(_to_list(empty), [], "empty queue should remain empty.")


def test_odd_length_raises():
    _assert_raises(ValueError, lambda: interleave(SimpleQueue([1, 2, 3])),
                   "odd-length queue should raise ValueError.")


if __name__ == "__main__":
    TEST_CASES = [
        ("sample", test_sample),
        ("two and empty", test_two_and_empty),
        ("odd length raises", test_odd_length_raises),
    ]
    _run_all_tests(TEST_CASES)
