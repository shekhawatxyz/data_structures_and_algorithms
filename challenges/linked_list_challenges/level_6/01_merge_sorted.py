# Level 6.1 - merge_sorted(head1, head2)
# Write merge_sorted(head1, head2) to merge two sorted linked lists
# without creating new nodes, and return the merged head.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def merge_sorted(head1, head2):
    raise NotImplementedError('Implement merge_sorted(head1, head2).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_merge_sorted_basic_interleaving():
    head1 = _make_linked_list([1, 3, 5])
    head2 = _make_linked_list([2, 4, 6])
    result = merge_sorted(head1, head2)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3, 4, 5, 6],
        'merge_sorted should merge two sorted lists into sorted order.',
    )


def test_merge_sorted_with_one_empty_list():
    head1 = _make_linked_list([1, 2, 3])
    result = merge_sorted(head1, None)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3],
        'merge_sorted(list, None) should return the non-empty list.',
    )


def test_merge_sorted_with_duplicates():
    head1 = _make_linked_list([1, 2, 2])
    head2 = _make_linked_list([2, 2, 3])
    result = merge_sorted(head1, head2)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 2, 2, 2, 3],
        'merge_sorted should preserve duplicate values from both lists.',
    )


def test_merge_sorted_reuses_existing_nodes_only():
    head1 = _make_linked_list([1, 4])
    head2 = _make_linked_list([2, 3])
    expected_ids = set(_node_ids(head1) + _node_ids(head2))
    result = merge_sorted(head1, head2)
    result_ids = _node_ids(result)

    _assert_equal(
        set(result_ids),
        expected_ids,
        'merge_sorted should reuse original nodes instead of creating new ones.',
    )
    _assert_equal(
        len(result_ids),
        len(expected_ids),
        'Merged list should contain each original node exactly once.',
    )


if __name__ == '__main__':
    TEST_CASES = [
        ('basic merge interleaving', test_merge_sorted_basic_interleaving),
        ('one list empty', test_merge_sorted_with_one_empty_list),
        ('merge with duplicates', test_merge_sorted_with_duplicates),
        ('reuses existing nodes only', test_merge_sorted_reuses_existing_nodes_only),
    ]
    _run_all_tests(TEST_CASES)
