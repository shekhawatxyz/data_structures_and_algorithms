# Level 7.1 - reverse_between(head, left, right)
# Write reverse_between(head, left, right) that reverses only the
# sublist from position left to right (1-indexed).

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_between(head, left, right):
    raise NotImplementedError('Implement reverse_between(head, left, right).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_reverse_between_middle_segment():
    head = _make_linked_list([1, 2, 3, 4, 5])
    result = reverse_between(head, 2, 4)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 4, 3, 2, 5],
        'reverse_between should reverse the requested middle segment only.',
    )


def test_reverse_between_entire_list():
    head = _make_linked_list([1, 2, 3])
    result = reverse_between(head, 1, 3)
    _assert_equal(
        _linked_list_to_list(result),
        [3, 2, 1],
        'Reversing from 1 to length should reverse the whole list.',
    )


def test_reverse_between_noop_when_left_equals_right():
    head = _make_linked_list([1, 2, 3])
    result = reverse_between(head, 2, 2)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3],
        'When left == right, the list should remain unchanged.',
    )


def test_reverse_between_including_head_or_tail():
    head1 = _make_linked_list([1, 2, 3, 4])
    result1 = reverse_between(head1, 1, 2)
    _assert_equal(_linked_list_to_list(result1), [2, 1, 3, 4], 'Should support reversing from the head.')

    head2 = _make_linked_list([1, 2, 3, 4])
    result2 = reverse_between(head2, 3, 4)
    _assert_equal(_linked_list_to_list(result2), [1, 2, 4, 3], 'Should support reversing through the tail.')


if __name__ == '__main__':
    TEST_CASES = [
        ('reverse middle segment', test_reverse_between_middle_segment),
        ('reverse entire list', test_reverse_between_entire_list),
        ('left==right no-op', test_reverse_between_noop_when_left_equals_right),
        ('handles head/tail ranges', test_reverse_between_including_head_or_tail),
    ]
    _run_all_tests(TEST_CASES)
