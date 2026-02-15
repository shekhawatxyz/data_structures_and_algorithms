# Level 3.4 - delete_range(head, start, end)
# Write delete_range(head, start, end) that removes all nodes from
# index start to index end (inclusive), then returns the new head.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def delete_range(head, start, end):
    raise NotImplementedError('Implement delete_range(head, start, end).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_delete_middle_range():
    head = _make_linked_list([1, 2, 3, 4, 5])
    result = delete_range(head, 1, 3)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 5],
        'delete_range should remove the inclusive range in the middle.',
    )


def test_delete_range_from_head():
    head = _make_linked_list([1, 2, 3, 4])
    result = delete_range(head, 0, 1)
    _assert_equal(
        _linked_list_to_list(result),
        [3, 4],
        'delete_range with start=0 should correctly update the head.',
    )


def test_delete_range_to_tail():
    head = _make_linked_list([1, 2, 3, 4, 5])
    result = delete_range(head, 3, 4)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3],
        'delete_range should remove a suffix when end reaches the tail.',
    )


def test_delete_single_index_range():
    head = _make_linked_list([10, 20, 30])
    result = delete_range(head, 1, 1)
    _assert_equal(
        _linked_list_to_list(result),
        [10, 30],
        'delete_range with start=end should remove exactly one node.',
    )


def test_delete_entire_list_range_returns_none():
    head = _make_linked_list([7, 8, 9])
    result = delete_range(head, 0, 2)
    _assert_true(result is None, 'Deleting the full index range should return None.')


if __name__ == '__main__':
    TEST_CASES = [
        ('delete middle range', test_delete_middle_range),
        ('delete range from head', test_delete_range_from_head),
        ('delete range to tail', test_delete_range_to_tail),
        ('delete single-index range', test_delete_single_index_range),
        ('delete entire list range', test_delete_entire_list_range_returns_none),
    ]
    _run_all_tests(TEST_CASES)
