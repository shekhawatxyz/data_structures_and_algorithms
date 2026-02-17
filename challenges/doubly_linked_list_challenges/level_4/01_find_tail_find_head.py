# Level 4.1 - find_tail(head), find_head(tail)
# Write find_tail(head) and find_head(tail) so either end of the list
# can recover access to the full structure.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def find_tail(head):
    raise NotImplementedError('Implement find_tail(head).')


def find_head(tail):
    raise NotImplementedError('Implement find_head(tail).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_find_tail_returns_last_node():
    head = _make_doubly_linked_list([1, 2, 3, 4])
    tail = find_tail(head)
    _assert_true(tail is not None and tail.data == 4, 'find_tail should return the node with value 4.')
    _assert_true(tail.next is None, 'Tail.next should be None.')


def test_find_head_from_tail_returns_original_head():
    head = _make_doubly_linked_list([5, 6, 7])
    tail = _tail_from_head(head)
    found_head = find_head(tail)
    _assert_true(found_head is head, 'find_head(tail) should recover the original head node.')


def test_find_tail_and_find_head_single_node_list():
    head = _make_doubly_linked_list([9])
    tail = find_tail(head)
    recovered = find_head(tail)
    _assert_true(tail is head, 'For single-node list, tail should be the head node.')
    _assert_true(recovered is head, 'find_head on single-node tail should return that same node.')


def test_find_tail_and_find_head_on_empty_input():
    _assert_true(find_tail(None) is None, 'find_tail(None) should return None.')
    _assert_true(find_head(None) is None, 'find_head(None) should return None.')


if __name__ == '__main__':
    TEST_CASES = [
        ('find_tail returns tail node', test_find_tail_returns_last_node),
        ('find_head recovers original head', test_find_head_from_tail_returns_original_head),
        ('single-node behavior', test_find_tail_and_find_head_single_node_list),
        ('empty-input behavior', test_find_tail_and_find_head_on_empty_input),
    ]
    _run_all_tests(TEST_CASES)
