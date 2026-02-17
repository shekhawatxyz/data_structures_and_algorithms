# Level 7.1 - reverse_between(head, left, right)
# Write reverse_between(head, left, right) for 1-indexed boundaries,
# keeping all prev/next links valid across the full list.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def reverse_between(head, left, right):
    raise NotImplementedError('Implement reverse_between(head, left, right).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_reverse_between_middle_segment():
    head = _make_doubly_linked_list([1, 2, 3, 4, 5])
    result = reverse_between(head, 2, 4)
    _assert_equal(_to_list_forward(result), [1, 4, 3, 2, 5], 'Middle segment should reverse in place.')
    _assert_true(_verify_bidirectional_links(result), 'All links should stay valid after middle reversal.')


def test_reverse_between_entire_list():
    head = _make_doubly_linked_list([1, 2, 3])
    result = reverse_between(head, 1, 3)
    _assert_equal(_to_list_forward(result), [3, 2, 1], 'Full-range reverse_between should reverse the whole list.')


def test_reverse_between_left_equals_right_noop():
    head = _make_doubly_linked_list([1, 2, 3])
    result = reverse_between(head, 2, 2)
    _assert_equal(_to_list_forward(result), [1, 2, 3], 'If left == right, list should remain unchanged.')


def test_reverse_between_handles_head_or_tail_boundaries():
    head1 = _make_doubly_linked_list([1, 2, 3, 4])
    result1 = reverse_between(head1, 1, 2)
    _assert_equal(_to_list_forward(result1), [2, 1, 3, 4], 'Range starting at head should reverse correctly.')

    head2 = _make_doubly_linked_list([1, 2, 3, 4])
    result2 = reverse_between(head2, 3, 4)
    _assert_equal(_to_list_forward(result2), [1, 2, 4, 3], 'Range ending at tail should reverse correctly.')


if __name__ == '__main__':
    TEST_CASES = [
        ('reverse middle segment', test_reverse_between_middle_segment),
        ('reverse entire list', test_reverse_between_entire_list),
        ('left==right no-op', test_reverse_between_left_equals_right_noop),
        ('head/tail boundary ranges', test_reverse_between_handles_head_or_tail_boundaries),
    ]
    _run_all_tests(TEST_CASES)
