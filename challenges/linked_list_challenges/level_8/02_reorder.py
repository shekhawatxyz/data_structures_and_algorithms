# Level 8.2 - reorder(head)
# Write reorder(head) to transform L0 -> L1 -> ... -> Ln into
# L0 -> Ln -> L1 -> Ln-1 -> L2 -> ... in-place.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reorder(head):
    raise NotImplementedError('Implement reorder(head).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def _resolved_reorder_head(original_head, result):
    # Allow either in-place (return None) or return-new-head styles.
    return original_head if result is None else result


def test_reorder_odd_length_list():
    head = _make_linked_list([1, 2, 3, 4, 5])
    result = reorder(head)
    final_head = _resolved_reorder_head(head, result)
    _assert_equal(
        _linked_list_to_list(final_head),
        [1, 5, 2, 4, 3],
        'reorder should produce L0, Ln, L1, Ln-1... for odd-length lists.',
    )


def test_reorder_even_length_list():
    head = _make_linked_list([1, 2, 3, 4])
    result = reorder(head)
    final_head = _resolved_reorder_head(head, result)
    _assert_equal(
        _linked_list_to_list(final_head),
        [1, 4, 2, 3],
        'reorder should produce L0, Ln, L1, Ln-1... for even-length lists.',
    )


def test_reorder_short_lists_stay_valid():
    one = _make_linked_list([7])
    result_one = reorder(one)
    final_one = _resolved_reorder_head(one, result_one)
    _assert_equal(_linked_list_to_list(final_one), [7], 'Single-node list should remain unchanged.')

    two = _make_linked_list([7, 8])
    result_two = reorder(two)
    final_two = _resolved_reorder_head(two, result_two)
    _assert_equal(_linked_list_to_list(final_two), [7, 8], 'Two-node list should remain unchanged.')


def test_reorder_empty_list_is_handled():
    result = reorder(None)
    final_head = _resolved_reorder_head(None, result)
    _assert_true(final_head is None, 'reorder(None) should return None or keep None unchanged.')


if __name__ == '__main__':
    TEST_CASES = [
        ('odd-length reorder', test_reorder_odd_length_list),
        ('even-length reorder', test_reorder_even_length_list),
        ('short lists remain valid', test_reorder_short_lists_stay_valid),
        ('empty list handling', test_reorder_empty_list_is_handled),
    ]
    _run_all_tests(TEST_CASES)
