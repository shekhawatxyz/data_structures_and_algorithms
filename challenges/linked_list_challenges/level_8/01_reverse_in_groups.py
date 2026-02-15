# Level 8.1 - reverse_in_groups(head, k)
# Write reverse_in_groups(head, k) that reverses the list in groups of k.
# If fewer than k nodes remain, reverse that final group as well.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_in_groups(head, k):
    raise NotImplementedError('Implement reverse_in_groups(head, k).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_reverse_in_groups_k_three():
    head = _make_linked_list([1, 2, 3, 4, 5])
    result = reverse_in_groups(head, 3)
    _assert_equal(
        _linked_list_to_list(result),
        [3, 2, 1, 5, 4],
        'With k=3, [1,2,3,4,5] should become [3,2,1,5,4].',
    )


def test_reverse_in_groups_k_one_keeps_list_unchanged():
    head = _make_linked_list([1, 2, 3])
    result = reverse_in_groups(head, 1)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3],
        'With k=1, reverse_in_groups should not change the list.',
    )


def test_reverse_in_groups_k_larger_than_length_reverses_all():
    head = _make_linked_list([1, 2, 3])
    result = reverse_in_groups(head, 5)
    _assert_equal(
        _linked_list_to_list(result),
        [3, 2, 1],
        'If k > length, the full list should be reversed as one final group.',
    )


def test_reverse_in_groups_raises_for_non_positive_k():
    head = _make_linked_list([1, 2, 3])
    _assert_raises(
        lambda: reverse_in_groups(head, 0),
        'reverse_in_groups should raise an error for k=0.',
    )
    _assert_raises(
        lambda: reverse_in_groups(head, -2),
        'reverse_in_groups should raise an error for negative k.',
    )


if __name__ == '__main__':
    TEST_CASES = [
        ('k=3 group reversal', test_reverse_in_groups_k_three),
        ('k=1 no change', test_reverse_in_groups_k_one_keeps_list_unchanged),
        ('k>length reverses all', test_reverse_in_groups_k_larger_than_length_reverses_all),
        ('invalid k raises errors', test_reverse_in_groups_raises_for_non_positive_k),
    ]
    _run_all_tests(TEST_CASES)
