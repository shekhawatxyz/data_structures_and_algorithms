# Level 6.3 - split_at(head, index)
# Write split_at(head, index) that splits one doubly linked list into
# two independent lists and returns both heads.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def split_at(head, index):
    raise NotImplementedError('Implement split_at(head, index).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def _as_two_heads(result):
    _assert_true(
        isinstance(result, (tuple, list)) and len(result) == 2,
        'split_at should return a pair: (head1, head2).',
    )
    return result[0], result[1]


def test_split_at_middle_index():
    head = _make_doubly_linked_list([1, 2, 3, 4, 5])
    left, right = _as_two_heads(split_at(head, 2))
    _assert_equal(_to_list_forward(left), [1, 2], 'Left side should contain nodes before split index.')
    _assert_equal(_to_list_forward(right), [3, 4, 5], 'Right side should start at the split index.')
    _assert_true(_tail_from_head(left).next is None, 'Left tail.next should be None after split.')
    _assert_true(right.prev is None, 'Right head.prev should be None after split.')


def test_split_at_zero_index_returns_empty_left():
    head = _make_doubly_linked_list([7, 8, 9])
    left, right = _as_two_heads(split_at(head, 0))
    _assert_true(left is None, 'split_at(..., 0) should return None as first head.')
    _assert_equal(_to_list_forward(right), [7, 8, 9], 'Right list should contain all original nodes.')
    _assert_true(right.prev is None, 'Right head.prev must be None after split at 0.')


def test_split_at_length_returns_empty_right():
    head = _make_doubly_linked_list([1, 2, 3])
    left, right = _as_two_heads(split_at(head, 3))
    _assert_equal(_to_list_forward(left), [1, 2, 3], 'Left should contain all nodes when index == length.')
    _assert_true(right is None, 'Right should be None when index == length.')


def test_split_at_invalid_indexes_raise_errors():
    head = _make_doubly_linked_list([1, 2, 3])
    _assert_raises(lambda: split_at(head, -1), 'split_at should raise for negative indexes.')
    _assert_raises(lambda: split_at(head, 10), 'split_at should raise for indexes larger than list length.')


if __name__ == '__main__':
    TEST_CASES = [
        ('split at middle index', test_split_at_middle_index),
        ('split at zero index', test_split_at_zero_index_returns_empty_left),
        ('split at length index', test_split_at_length_returns_empty_right),
        ('invalid indexes raise', test_split_at_invalid_indexes_raise_errors),
    ]
    _run_all_tests(TEST_CASES)
