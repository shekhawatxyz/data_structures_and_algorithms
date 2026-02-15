# Level 7.3 - remove_duplicates_unsorted(head)
# Write remove_duplicates_unsorted(head) that removes duplicates from
# an unsorted list while preserving first occurrences.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def remove_duplicates_unsorted(head):
    raise NotImplementedError('Implement remove_duplicates_unsorted(head).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_remove_duplicates_unsorted_preserves_first_occurrences():
    head = _make_linked_list([3, 1, 3, 2, 1, 4, 2])
    result = remove_duplicates_unsorted(head)
    _assert_equal(
        _linked_list_to_list(result),
        [3, 1, 2, 4],
        'remove_duplicates_unsorted should keep first occurrences in original order.',
    )


def test_remove_duplicates_unsorted_no_duplicates_case():
    head = _make_linked_list([1, 2, 3])
    result = remove_duplicates_unsorted(head)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3],
        'List with no duplicates should remain unchanged.',
    )


def test_remove_duplicates_unsorted_all_duplicates_case():
    head = _make_linked_list([5, 5, 5, 5])
    result = remove_duplicates_unsorted(head)
    _assert_equal(
        _linked_list_to_list(result),
        [5],
        'All-duplicate list should reduce to a single node.',
    )


def test_remove_duplicates_unsorted_empty_list():
    result = remove_duplicates_unsorted(None)
    _assert_true(result is None, 'remove_duplicates_unsorted(None) should return None.')


if __name__ == '__main__':
    TEST_CASES = [
        ('preserves first occurrences', test_remove_duplicates_unsorted_preserves_first_occurrences),
        ('no duplicates unchanged', test_remove_duplicates_unsorted_no_duplicates_case),
        ('all duplicates collapse', test_remove_duplicates_unsorted_all_duplicates_case),
        ('empty list returns None', test_remove_duplicates_unsorted_empty_list),
    ]
    _run_all_tests(TEST_CASES)
