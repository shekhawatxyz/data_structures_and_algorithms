# Level 6.4 - concatenate(head1, head2)
# Write concatenate(head1, head2) that joins two doubly linked lists
# end-to-end and returns the combined head.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def concatenate(head1, head2):
    raise NotImplementedError('Implement concatenate(head1, head2).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_concatenate_two_non_empty_lists():
    head1 = _make_doubly_linked_list([1, 2])
    head2 = _make_doubly_linked_list([3, 4])
    result = concatenate(head1, head2)
    _assert_equal(_to_list_forward(result), [1, 2, 3, 4], 'concatenate should join both lists in order.')
    _assert_true(_verify_bidirectional_links(result), 'All links should remain valid after concatenation.')


def test_concatenate_first_empty_returns_second():
    head2 = _make_doubly_linked_list([8, 9])
    result = concatenate(None, head2)
    _assert_equal(_to_list_forward(result), [8, 9], 'concatenate(None, B) should return B.')


def test_concatenate_second_empty_returns_first():
    head1 = _make_doubly_linked_list([5, 6])
    result = concatenate(head1, None)
    _assert_equal(_to_list_forward(result), [5, 6], 'concatenate(A, None) should return A.')


def test_concatenate_preserves_join_pointer_relationship():
    head1 = _make_doubly_linked_list([10, 20])
    head2 = _make_doubly_linked_list([30])
    tail1 = _tail_from_head(head1)
    result = concatenate(head1, head2)
    _assert_true(tail1.next is head2, 'Old tail of first list should point to second head after join.')
    _assert_true(head2.prev is tail1, 'Second head.prev should point to first tail after join.')
    _assert_equal(_to_list_forward(result), [10, 20, 30], 'Joined values should appear in order.')


if __name__ == '__main__':
    TEST_CASES = [
        ('concatenate non-empty lists', test_concatenate_two_non_empty_lists),
        ('first list empty', test_concatenate_first_empty_returns_second),
        ('second list empty', test_concatenate_second_empty_returns_first),
        ('join pointers set correctly', test_concatenate_preserves_join_pointer_relationship),
    ]
    _run_all_tests(TEST_CASES)
