# Level 7.2 - rotate(head, k)
# Write rotate(head, k) that rotates the list to the right by k places.
# Handle k values larger than the list length.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def rotate(head, k):
    raise NotImplementedError('Implement rotate(head, k).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_rotate_by_zero_keeps_list_unchanged():
    head = _make_linked_list([1, 2, 3, 4])
    result = rotate(head, 0)
    _assert_equal(_linked_list_to_list(result), [1, 2, 3, 4], 'rotate(..., 0) should not change the list.')


def test_rotate_by_value_less_than_length():
    head = _make_linked_list([1, 2, 3, 4, 5])
    result = rotate(head, 2)
    _assert_equal(
        _linked_list_to_list(result),
        [4, 5, 1, 2, 3],
        'Right rotate by 2 should move the last two nodes to the front.',
    )


def test_rotate_by_value_greater_than_length():
    head = _make_linked_list([1, 2, 3, 4, 5])
    result = rotate(head, 7)  # equivalent to rotate by 2
    _assert_equal(
        _linked_list_to_list(result),
        [4, 5, 1, 2, 3],
        'rotate should apply k modulo list length for large k.',
    )


def test_rotate_empty_and_single_node_lists():
    _assert_true(rotate(None, 3) is None, 'Rotating an empty list should return None.')

    single = _make_linked_list([9])
    result = rotate(single, 100)
    _assert_equal(_linked_list_to_list(result), [9], 'Single-node list should remain unchanged for any k.')


if __name__ == '__main__':
    TEST_CASES = [
        ('rotate by zero', test_rotate_by_zero_keeps_list_unchanged),
        ('rotate by k < length', test_rotate_by_value_less_than_length),
        ('rotate by k > length', test_rotate_by_value_greater_than_length),
        ('rotate empty/single lists', test_rotate_empty_and_single_node_lists),
    ]
    _run_all_tests(TEST_CASES)
