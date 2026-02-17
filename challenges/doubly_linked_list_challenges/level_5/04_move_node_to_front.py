# Level 5.4 - move_node_to_front(head, node)
# Write move_node_to_front(head, node) that unlinks the given node and
# moves it to the front, returning the new head.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def move_node_to_front(head, node):
    raise NotImplementedError('Implement move_node_to_front(head, node).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_move_middle_node_to_front():
    head = _make_doubly_linked_list([1, 2, 3, 4])
    node3 = _find_first_node(head, 3)
    result = move_node_to_front(head, node3)
    _assert_equal(_to_list_forward(result), [3, 1, 2, 4], 'Middle node should move to the front.')
    _assert_true(result is node3, 'Returned head should be the moved node.')


def test_move_tail_node_to_front():
    head = _make_doubly_linked_list([5, 6, 7])
    tail = _tail_from_head(head)
    result = move_node_to_front(head, tail)
    _assert_equal(_to_list_forward(result), [7, 5, 6], 'Tail node should move to front correctly.')
    _assert_true(_verify_bidirectional_links(result), 'All links should stay valid after moving tail to front.')


def test_move_head_node_to_front_is_noop():
    head = _make_doubly_linked_list([9, 8, 7])
    result = move_node_to_front(head, head)
    _assert_equal(_to_list_forward(result), [9, 8, 7], 'Moving head to front should keep list unchanged.')


def test_move_node_to_front_on_single_node_list():
    head = _make_doubly_linked_list([42])
    result = move_node_to_front(head, head)
    _assert_equal(_to_list_forward(result), [42], 'Single-node list should remain unchanged.')
    _assert_true(result.prev is None and result.next is None, 'Single-node links should remain None/None.')


if __name__ == '__main__':
    TEST_CASES = [
        ('move middle node to front', test_move_middle_node_to_front),
        ('move tail node to front', test_move_tail_node_to_front),
        ('moving head is noop', test_move_head_node_to_front_is_noop),
        ('single-node move is stable', test_move_node_to_front_on_single_node_list),
    ]
    _run_all_tests(TEST_CASES)
