# Level 2.3 - insert_at(head, index, value)
# Write insert_at(head, index, value) for 0-indexed insertion positions
# and return the new head.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def insert_at(head, index, value):
    raise NotImplementedError('Implement insert_at(head, index, value).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

def _make_doubly_linked_list(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            node.prev = tail
            tail = node
    return head


def _head_from_any(node):
    current = node
    while current is not None and current.prev is not None:
        current = current.prev
    return current


def _tail_from_head(head):
    current = head
    while current is not None and current.next is not None:
        current = current.next
    return current


def _to_list_forward(head, max_nodes=2000):
    values = []
    current = head
    steps = 0

    while current is not None:
        values.append(current.data)
        current = current.next
        steps += 1
        if steps > max_nodes:
            raise AssertionError(
                'Forward traversal exceeded safety limit; possible cycle or broken links.'
            )

    return values


def _to_list_backward(head, max_nodes=2000):
    values = []
    current = _tail_from_head(head)
    steps = 0

    while current is not None:
        values.append(current.data)
        current = current.prev
        steps += 1
        if steps > max_nodes:
            raise AssertionError(
                'Backward traversal exceeded safety limit; possible cycle or broken links.'
            )

    return values


def _verify_bidirectional_links(head, max_nodes=2000):
    if head is None:
        return True

    if head.prev is not None:
        return False

    prev_node = None
    current = head
    steps = 0

    while current is not None:
        if current.prev is not prev_node:
            return False
        if prev_node is not None and prev_node.next is not current:
            return False

        prev_node = current
        current = current.next
        steps += 1

        if steps > max_nodes:
            return False

    return True


def _list_nodes(head, max_nodes=2000):
    nodes = []
    current = head
    steps = 0

    while current is not None:
        nodes.append(current)
        current = current.next
        steps += 1
        if steps > max_nodes:
            raise AssertionError('Node traversal exceeded safety limit; possible cycle.')

    return nodes


def _node_ids(head, max_nodes=2000):
    return [id(node) for node in _list_nodes(head, max_nodes=max_nodes)]


def _find_first_node(head, value):
    current = head
    while current is not None:
        if current.data == value:
            return current
        current = current.next
    return None


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

def test_insert_at_index_zero_prepends():
    head = _make_doubly_linked_list([2, 3])
    result = insert_at(head, 0, 1)
    _assert_equal(_to_list_forward(result), [1, 2, 3], 'insert_at(..., 0, value) should prepend.')
    _assert_true(result.prev is None, 'New head.prev should be None after prepending.')


def test_insert_at_middle_position():
    head = _make_doubly_linked_list([1, 3, 4])
    result = insert_at(head, 1, 2)
    _assert_equal(_to_list_forward(result), [1, 2, 3, 4], 'insert_at should insert correctly in the middle.')
    _assert_true(_verify_bidirectional_links(result), 'All links should remain valid after middle insertion.')


def test_insert_at_end_appends_at_tail():
    head = _make_doubly_linked_list([1, 2, 3])
    result = insert_at(head, 3, 4)
    _assert_equal(_to_list_forward(result), [1, 2, 3, 4], 'insert_at at index==length should append.')
    _assert_true(_tail_from_head(result).next is None, 'Tail.next should remain None after append.')


def test_insert_at_raises_for_invalid_indexes():
    head = _make_doubly_linked_list([1, 2, 3])
    _assert_raises(
        lambda: insert_at(head, -1, 5),
        'insert_at should raise an error for negative indexes.',
    )
    _assert_raises(
        lambda: insert_at(head, 10, 5),
        'insert_at should raise an error when index is out of range.',
    )


if __name__ == '__main__':
    TEST_CASES = [
        ('index 0 prepends', test_insert_at_index_zero_prepends),
        ('middle insertion', test_insert_at_middle_position),
        ('index==length appends', test_insert_at_end_appends_at_tail),
        ('invalid indexes raise', test_insert_at_raises_for_invalid_indexes),
    ]
    _run_all_tests(TEST_CASES)
