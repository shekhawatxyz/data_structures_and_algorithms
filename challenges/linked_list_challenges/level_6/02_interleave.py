# Level 6.2 - interleave(head1, head2)
# Write interleave(head1, head2) that weaves two lists together.
# If one list is longer, append the remaining nodes at the end.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def interleave(head1, head2):
    raise NotImplementedError('Implement interleave(head1, head2).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_interleave_equal_lengths():
    head1 = _make_linked_list([1, 2, 3])
    head2 = _make_linked_list(['a', 'b', 'c'])
    result = interleave(head1, head2)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 'a', 2, 'b', 3, 'c'],
        'interleave should alternate nodes when list lengths are equal.',
    )


def test_interleave_first_list_longer():
    head1 = _make_linked_list([1, 2, 3, 4, 5])
    head2 = _make_linked_list(['x', 'y'])
    result = interleave(head1, head2)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 'x', 2, 'y', 3, 4, 5],
        'Remaining nodes from first list should stay at the end.',
    )


def test_interleave_second_list_longer():
    head1 = _make_linked_list([1, 2])
    head2 = _make_linked_list(['x', 'y', 'z'])
    result = interleave(head1, head2)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 'x', 2, 'y', 'z'],
        'Remaining nodes from second list should stay at the end.',
    )


def test_interleave_with_empty_list_inputs():
    only_second = _make_linked_list([9, 8])
    result1 = interleave(None, only_second)
    _assert_equal(_linked_list_to_list(result1), [9, 8], 'interleave(None, B) should return B.')

    only_first = _make_linked_list([1, 2])
    result2 = interleave(only_first, None)
    _assert_equal(_linked_list_to_list(result2), [1, 2], 'interleave(A, None) should return A.')


if __name__ == '__main__':
    TEST_CASES = [
        ('equal length interleave', test_interleave_equal_lengths),
        ('first list longer', test_interleave_first_list_longer),
        ('second list longer', test_interleave_second_list_longer),
        ('handles empty inputs', test_interleave_with_empty_list_inputs),
    ]
    _run_all_tests(TEST_CASES)
