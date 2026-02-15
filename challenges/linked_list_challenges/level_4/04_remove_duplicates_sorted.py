# Level 4.4 - remove_duplicates_sorted(head)
# Write remove_duplicates_sorted(head) for a non-decreasing sorted list
# so that each distinct value appears only once.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def remove_duplicates_sorted(head):
    raise NotImplementedError('Implement remove_duplicates_sorted(head).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_remove_duplicates_sorted_handles_empty_list():
    result = remove_duplicates_sorted(None)
    _assert_true(result is None, 'remove_duplicates_sorted(None) should return None.')


def test_remove_duplicates_sorted_on_already_unique_values():
    head = _make_linked_list([1, 2, 3, 4])
    result = remove_duplicates_sorted(head)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3, 4],
        'A list with unique sorted values should remain unchanged.',
    )


def test_remove_duplicates_sorted_collapses_duplicate_runs():
    head = _make_linked_list([1, 1, 2, 3, 3, 3, 4, 4])
    result = remove_duplicates_sorted(head)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3, 4],
        'Duplicate runs in a sorted list should be collapsed to one node each.',
    )


def test_remove_duplicates_sorted_all_values_same():
    head = _make_linked_list([9, 9, 9, 9])
    result = remove_duplicates_sorted(head)
    _assert_equal(
        _linked_list_to_list(result),
        [9],
        'When all values are the same, one node should remain.',
    )


if __name__ == '__main__':
    TEST_CASES = [
        ('empty list stays empty', test_remove_duplicates_sorted_handles_empty_list),
        ('already unique list unchanged', test_remove_duplicates_sorted_on_already_unique_values),
        ('duplicate runs collapsed', test_remove_duplicates_sorted_collapses_duplicate_runs),
        ('all values identical', test_remove_duplicates_sorted_all_values_same),
    ]
    _run_all_tests(TEST_CASES)
