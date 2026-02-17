# Level 1.3 - to_list_backward(head)
# Write to_list_backward(head) that finds the tail from head and then
# traverses backward to produce reversed values.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def to_list_backward(head):
    raise NotImplementedError('Implement to_list_backward(head).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_to_list_backward_none_returns_empty_list():
    _assert_equal(to_list_backward(None), [], 'to_list_backward(None) should return [].')


def test_to_list_backward_single_node():
    head = _make_doubly_linked_list([8])
    _assert_equal(to_list_backward(head), [8], 'Single-node backward traversal should return [8].')


def test_to_list_backward_multiple_nodes_returns_reverse_order():
    head = _make_doubly_linked_list([1, 2, 3, 4])
    _assert_equal(
        to_list_backward(head),
        [4, 3, 2, 1],
        'to_list_backward should return values from tail to head.',
    )


def test_to_list_backward_matches_forward_reverse_for_valid_list():
    head = _make_doubly_linked_list([10, 20, 30, 40, 50])
    forward = _to_list_forward(head)
    backward = to_list_backward(head)
    _assert_equal(
        backward,
        forward[::-1],
        'to_list_backward(head) should equal to_list(head)[::-1] for a valid list.',
    )


if __name__ == '__main__':
    TEST_CASES = [
        ('None returns []', test_to_list_backward_none_returns_empty_list),
        ('single-node backward traversal', test_to_list_backward_single_node),
        ('multi-node reverse order', test_to_list_backward_multiple_nodes_returns_reverse_order),
        ('matches forward reverse', test_to_list_backward_matches_forward_reverse_for_valid_list),
    ]
    _run_all_tests(TEST_CASES)
