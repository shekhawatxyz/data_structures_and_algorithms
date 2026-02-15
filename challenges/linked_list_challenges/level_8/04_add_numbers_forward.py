# Level 8.4 - add_numbers_forward(head1, head2)
# Each list stores a non-negative integer in forward digit order.
# Write add_numbers_forward(head1, head2) and return the sum as a new list.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def add_numbers_forward(head1, head2):
    raise NotImplementedError('Implement add_numbers_forward(head1, head2).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_add_numbers_forward_basic_example():
    head1 = _make_linked_list([7, 2, 4, 3])  # 7243
    head2 = _make_linked_list([5, 6, 4])     # 564
    result = add_numbers_forward(head1, head2)  # 7807
    _assert_equal(
        _linked_list_to_list(result),
        [7, 8, 0, 7],
        '7243 + 564 should produce [7,8,0,7].',
    )


def test_add_numbers_forward_with_carry_creating_new_head():
    head1 = _make_linked_list([9, 9, 9])
    head2 = _make_linked_list([1])
    result = add_numbers_forward(head1, head2)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 0, 0, 0],
        '999 + 1 should produce [1,0,0,0] with a new leading carry node.',
    )


def test_add_numbers_forward_different_lengths():
    head1 = _make_linked_list([1, 2, 3])   # 123
    head2 = _make_linked_list([9, 9])      # 99
    result = add_numbers_forward(head1, head2)  # 222
    _assert_equal(
        _linked_list_to_list(result),
        [2, 2, 2],
        'add_numbers_forward should work when the input lengths differ.',
    )


def test_add_numbers_forward_zero_plus_zero():
    head1 = _make_linked_list([0])
    head2 = _make_linked_list([0])
    result = add_numbers_forward(head1, head2)
    _assert_equal(_linked_list_to_list(result), [0], '0 + 0 should produce [0].')


if __name__ == '__main__':
    TEST_CASES = [
        ('basic forward-order addition', test_add_numbers_forward_basic_example),
        ('carry creates new head', test_add_numbers_forward_with_carry_creating_new_head),
        ('different length forward lists', test_add_numbers_forward_different_lengths),
        ('zero plus zero', test_add_numbers_forward_zero_plus_zero),
    ]
    _run_all_tests(TEST_CASES)
