# Level 5.3 - partition(head, x)
# Write partition(head, x) that places all values < x before values >= x,
# while preserving relative order within each partition.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def partition(head, x):
    raise NotImplementedError('Implement partition(head, x).')

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

def _make_linked_list(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def _linked_list_to_list(head, max_nodes=2000):
    values = []
    current = head
    steps = 0

    while current is not None:
        values.append(current.data)
        current = current.next
        steps += 1
        if steps > max_nodes:
            raise AssertionError(
                'Linked list traversal exceeded a safety limit. '
                'Your list might contain an unexpected cycle.'
            )

    return values


def _node_ids(head, max_nodes=2000):
    ids = []
    current = head
    steps = 0

    while current is not None:
        ids.append(id(current))
        current = current.next
        steps += 1
        if steps > max_nodes:
            raise AssertionError(
                'Node-id traversal exceeded a safety limit. '
                'Your list might contain an unexpected cycle.'
            )

    return ids


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

def test_partition_mixed_values_with_stable_order():
    head = _make_linked_list([3, 5, 8, 5, 10, 2, 1])
    result = partition(head, 5)
    _assert_equal(
        _linked_list_to_list(result),
        [3, 2, 1, 5, 8, 5, 10],
        'partition should preserve relative order in both <x and >=x groups.',
    )


def test_partition_all_values_less_than_x():
    head = _make_linked_list([1, 2, 3])
    result = partition(head, 10)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3],
        'If all values are < x, partition should leave the list unchanged.',
    )


def test_partition_all_values_greater_or_equal_x():
    head = _make_linked_list([7, 8, 9])
    result = partition(head, 5)
    _assert_equal(
        _linked_list_to_list(result),
        [7, 8, 9],
        'If all values are >= x, partition should leave the list unchanged.',
    )


def test_partition_handles_empty_list():
    result = partition(None, 3)
    _assert_true(result is None, 'partition(None, x) should return None.')


if __name__ == '__main__':
    TEST_CASES = [
        ('mixed values stable partition', test_partition_mixed_values_with_stable_order),
        ('all values less than x', test_partition_all_values_less_than_x),
        ('all values >= x', test_partition_all_values_greater_or_equal_x),
        ('empty list partition', test_partition_handles_empty_list),
    ]
    _run_all_tests(TEST_CASES)
