# Level 7c - Queue Using Two Stacks
# Implement StackQueue with enqueue(item) and dequeue() using two stacks.
# Behavior must be FIFO and operations should be O(1) amortized.

class StackQueue:
    def __init__(self):
        raise NotImplementedError('Implement StackQueue.__init__.')

    def enqueue(self, item):
        raise NotImplementedError('Implement StackQueue.enqueue(item).')

    def dequeue(self):
        raise NotImplementedError('Implement StackQueue.dequeue().')

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


def _assert_raises(callable_obj, context):
    try:
        callable_obj()
    except Exception:
        return
    raise AssertionError(f"{context} Expected an exception, but none was raised.")


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
    total = len(test_cases)

    for name, fn in test_cases:
        if _run_test(name, fn):
            passed += 1

    print(f"\nPassed {passed}/{total} tests.")
    if passed != total:
        raise SystemExit(1)


def test_01_pedagogy_fifo_order_with_simple_sequence():
    queue = StackQueue()
    for value in [1, 2, 3]:
        queue.enqueue(value)

    _assert_equal(queue.dequeue(), 1, 'First dequeue should return first enqueued value 1.')
    _assert_equal(queue.dequeue(), 2, 'Second dequeue should return second enqueued value 2.')
    _assert_equal(queue.dequeue(), 3, 'Third dequeue should return third enqueued value 3.')


def test_02_pedagogy_interleaved_enqueue_and_dequeue():
    queue = StackQueue()
    queue.enqueue('a')
    queue.enqueue('b')
    _assert_equal(queue.dequeue(), 'a', 'First dequeue should return a after enqueue(a), enqueue(b).')
    queue.enqueue('c')
    _assert_equal(queue.dequeue(), 'b', 'Second dequeue should return b, preserving FIFO across transfer.')
    _assert_equal(queue.dequeue(), 'c', 'Third dequeue should return c.')


def test_03_boundaries_dequeue_on_empty_queue_raises():
    queue = StackQueue()
    _assert_raises(lambda: queue.dequeue(), 'dequeue() on empty queue should raise an error.')


def test_04_boundaries_off_by_one_after_full_drain_and_refill():
    queue = StackQueue()
    for value in [10, 11]:
        queue.enqueue(value)
    _assert_equal(queue.dequeue(), 10, 'Queue should return first item before draining.')
    _assert_equal(queue.dequeue(), 11, 'Queue should return second item before becoming empty.')
    _assert_raises(lambda: queue.dequeue(), 'Queue should raise immediately after becoming empty.')

    queue.enqueue(12)
    _assert_equal(queue.dequeue(), 12, 'Queue should work correctly after being emptied and reused.')


def test_05_interactions_long_sequence_preserves_fifo_across_transfer_phases():
    queue = StackQueue()
    for value in range(10):
        queue.enqueue(value)

    first_half = [queue.dequeue() for _ in range(5)]
    _assert_equal(first_half, [0, 1, 2, 3, 4], 'First dequeue phase should return earliest 5 elements in order.')

    for value in range(10, 15):
        queue.enqueue(value)

    second_phase = [queue.dequeue() for _ in range(10)]
    _assert_equal(
        second_phase,
        [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        'Second dequeue phase should preserve FIFO across old and newly enqueued values.',
    )


def test_06_interactions_mixed_data_types_remain_ordered():
    queue = StackQueue()
    values = [1, 'two', (3,), {'four': 4}]
    for value in values:
        queue.enqueue(value)

    observed = [queue.dequeue() for _ in range(len(values))]
    _assert_equal(observed, values, 'Queue should preserve insertion order for mixed data types.')


if __name__ == '__main__':
    TEST_CASES = [
        ('pedagogy: basic fifo', test_01_pedagogy_fifo_order_with_simple_sequence),
        ('pedagogy: interleaved enqueue/dequeue', test_02_pedagogy_interleaved_enqueue_and_dequeue),
        ('boundaries: empty dequeue raises', test_03_boundaries_dequeue_on_empty_queue_raises),
        ('boundaries: drain + refill off-by-one checks', test_04_boundaries_off_by_one_after_full_drain_and_refill),
        ('interactions: long transfer sequence', test_05_interactions_long_sequence_preserves_fifo_across_transfer_phases),
        ('interactions: mixed data types', test_06_interactions_mixed_data_types_remain_ordered),
    ]
    _run_all_tests(TEST_CASES)
