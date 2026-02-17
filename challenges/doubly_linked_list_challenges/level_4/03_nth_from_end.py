# Level 4.3 - nth_from_end(head, n)
# Write nth_from_end(head, n) that returns the value of the nth node
# from the end (1-indexed).

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
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

def test_nth_from_end_last_node_with_n_1():
    head = _make_doubly_linked_list([10, 20, 30, 40])
    _assert_equal(nth_from_end(head, 1), 40, 'n=1 should return the last node value.')


def test_nth_from_end_first_node_with_n_equals_length():
    head = _make_doubly_linked_list([10, 20, 30, 40])
    _assert_equal(nth_from_end(head, 4), 10, 'n==length should return the head node value.')


def test_nth_from_end_middle_node_value():
    head = _make_doubly_linked_list([5, 6, 7, 8, 9])
    _assert_equal(nth_from_end(head, 3), 7, 'n=3 should return the third node from the end.')


def test_nth_from_end_raises_for_invalid_n_values():
    head = _make_doubly_linked_list([1, 2, 3])
    _assert_raises(lambda: nth_from_end(head, 0), 'nth_from_end should raise for n=0.')
    _assert_raises(lambda: nth_from_end(head, 5), 'nth_from_end should raise when n > length.')


if __name__ == '__main__':
    TEST_CASES = [
        ('n=1 returns last value', test_nth_from_end_last_node_with_n_1),
        ('n=length returns first value', test_nth_from_end_first_node_with_n_equals_length),
        ('middle nth-from-end value', test_nth_from_end_middle_node_value),
        ('invalid n values raise', test_nth_from_end_raises_for_invalid_n_values),
    ]
    _run_all_tests(TEST_CASES)
