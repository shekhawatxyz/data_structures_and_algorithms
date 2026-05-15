# Level 4a - Reverse a queue
# Reverse a queue in place using queue operations and recursion.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 4a — Reverse a queue
#
# ```python
# def reverse(q) -> None:
#     ...
# ```
#
# Reverse `q` in place using only queue operations and recursion.
#
# ```
# q: front [1, 2, 3, 4] back
# reverse(q)
# q: front [4, 3, 2, 1] back
# ```
import importlib.util, os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "list_queue_1a",
    os.path.join(_here, "..", "level_1", "01_list_queue.py"),
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
ListQueue = _mod.ListQueue


def reverse(q: ListQueue) -> None:
    if len(q) <= 1:
        return
    first = q.dequeue()
    reverse(q)
    q.enqueue(first)


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

    def peek(self):
        if not self._items:
            raise IndexError("empty queue")
        return self._items[0]

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


def test_reverse_many_items():
    q = SimpleQueue([1, 2, 3, 4])
    reverse(q)
    _assert_equal(_to_list(q), [4, 3, 2, 1], "queue should be reversed in place.")


def test_reverse_single_and_empty():
    one = SimpleQueue(["x"])
    reverse(one)
    _assert_equal(_to_list(one), ["x"], "single item queue should remain unchanged.")
    empty = SimpleQueue()
    reverse(empty)
    _assert_equal(_to_list(empty), [], "empty queue should remain empty.")


if __name__ == "__main__":
    TEST_CASES = [
        ("reverse many items", test_reverse_many_items),
        ("reverse single and empty", test_reverse_single_and_empty),
    ]
    _run_all_tests(TEST_CASES)
