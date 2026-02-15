# Level 4.1 - nth_from_end(head, n)
# Write nth_from_end(head, n) that returns the value of the nth node
# from the end (1-indexed; n=1 means the last node).

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def nth_from_end(head, n):
    raise NotImplementedError('Implement nth_from_end(head, n).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_nth_from_end_last_node():
    head = _make_linked_list([10, 20, 30, 40])
    _assert_equal(
        nth_from_end(head, 1),
        40,
        'nth_from_end(..., 1) should return the last node value.',
    )


def test_nth_from_end_first_node_when_n_equals_length():
    head = _make_linked_list([10, 20, 30, 40])
    _assert_equal(
        nth_from_end(head, 4),
        10,
        'nth_from_end(..., length) should return the first node value.',
    )


def test_nth_from_end_middle_node():
    head = _make_linked_list([5, 6, 7, 8, 9])
    _assert_equal(
        nth_from_end(head, 3),
        7,
        'nth_from_end(..., 3) should return the third node from the end.',
    )


def test_nth_from_end_raises_for_invalid_n():
    head = _make_linked_list([1, 2, 3])
    _assert_raises(
        lambda: nth_from_end(head, 0),
        'nth_from_end should raise an error for n=0.',
    )
    _assert_raises(
        lambda: nth_from_end(head, 5),
        'nth_from_end should raise an error when n is larger than list length.',
    )
    _assert_raises(
        lambda: nth_from_end(None, 1),
        'nth_from_end should raise an error for an empty list.',
    )


if __name__ == '__main__':
    TEST_CASES = [
        ('last node with n=1', test_nth_from_end_last_node),
        ('first node with n=length', test_nth_from_end_first_node_when_n_equals_length),
        ('middle nth-from-end', test_nth_from_end_middle_node),
        ('invalid n values raise', test_nth_from_end_raises_for_invalid_n),
    ]
    _run_all_tests(TEST_CASES)
