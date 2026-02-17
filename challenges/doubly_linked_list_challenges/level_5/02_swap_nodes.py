# Level 5.2 - swap_nodes(head, val1, val2)
# Write swap_nodes(head, val1, val2) to re-link actual nodes (not just
# their data values), handling adjacency and head/tail cases.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def swap_nodes(head, val1, val2):
    raise NotImplementedError('Implement swap_nodes(head, val1, val2).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_swap_nodes_non_adjacent_values():
    head = _make_doubly_linked_list([1, 2, 3, 4, 5])
    result = swap_nodes(head, 2, 4)
    _assert_equal(_to_list_forward(result), [1, 4, 3, 2, 5], 'Non-adjacent values should swap node positions.')
    _assert_true(_verify_bidirectional_links(result), 'All links should remain valid after non-adjacent swap.')


def test_swap_nodes_adjacent_values():
    head = _make_doubly_linked_list([1, 2, 3, 4])
    result = swap_nodes(head, 2, 3)
    _assert_equal(_to_list_forward(result), [1, 3, 2, 4], 'Adjacent nodes should swap correctly.')
    _assert_true(_verify_bidirectional_links(result), 'All links should remain valid after adjacent swap.')


def test_swap_nodes_head_and_tail():
    head = _make_doubly_linked_list([1, 2, 3])
    result = swap_nodes(head, 1, 3)
    _assert_equal(_to_list_forward(result), [3, 2, 1], 'Swapping head and tail should update head correctly.')
    _assert_true(result.prev is None, 'Returned head.prev should be None after swap.')


def test_swap_nodes_must_swap_nodes_not_only_data_fields():
    head = _make_doubly_linked_list([1, 2, 3, 4])
    n1, n2, n3, n4 = _list_nodes(head)
    result = swap_nodes(head, 2, 4)
    _assert_equal(_to_list_forward(result), [1, 4, 3, 2], 'swap_nodes output order should reflect a node swap.')
    _assert_true(
        n4.prev is n1 and n4.next is n3,
        'Node that originally held value 4 should move between original nodes 1 and 3.',
    )
    _assert_true(
        n2.prev is n3 and n2.next is None,
        'Node that originally held value 2 should move to the tail after swapping with 4.',
    )


if __name__ == '__main__':
    TEST_CASES = [
        ('non-adjacent node swap', test_swap_nodes_non_adjacent_values),
        ('adjacent node swap', test_swap_nodes_adjacent_values),
        ('head/tail node swap', test_swap_nodes_head_and_tail),
        ('verifies real node swap', test_swap_nodes_must_swap_nodes_not_only_data_fields),
    ]
    _run_all_tests(TEST_CASES)
