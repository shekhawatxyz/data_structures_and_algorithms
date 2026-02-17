# Level 3.4 - delete_range(head, start, end)
# Write delete_range(head, start, end) that removes all nodes from
# index start to index end (inclusive).

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def delete_range(head, start, end):
    raise NotImplementedError('Implement delete_range(head, start, end).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_delete_range_middle_segment():
    head = _make_doubly_linked_list([1, 2, 3, 4, 5])
    result = delete_range(head, 1, 3)
    _assert_equal(_to_list_forward(result), [1, 5], 'delete_range should remove the inclusive middle segment.')
    _assert_true(_verify_bidirectional_links(result), 'Links must remain valid after range deletion.')


def test_delete_range_from_head():
    head = _make_doubly_linked_list([1, 2, 3, 4])
    result = delete_range(head, 0, 1)
    _assert_equal(_to_list_forward(result), [3, 4], 'Deleting a prefix range should update head correctly.')
    _assert_true(result.prev is None, 'Head.prev should be None after deleting from index 0.')


def test_delete_range_to_tail():
    head = _make_doubly_linked_list([1, 2, 3, 4, 5])
    result = delete_range(head, 3, 4)
    _assert_equal(_to_list_forward(result), [1, 2, 3], 'Deleting a suffix range should remove tail elements.')
    _assert_true(_tail_from_head(result).next is None, 'Tail.next should be None after deleting suffix.')


def test_delete_range_whole_list_returns_none():
    head = _make_doubly_linked_list([7, 8, 9])
    result = delete_range(head, 0, 2)
    _assert_true(result is None, 'Deleting full range should return None.')


if __name__ == '__main__':
    TEST_CASES = [
        ('delete middle range', test_delete_range_middle_segment),
        ('delete prefix range', test_delete_range_from_head),
        ('delete suffix range', test_delete_range_to_tail),
        ('delete full range returns None', test_delete_range_whole_list_returns_none),
    ]
    _run_all_tests(TEST_CASES)
