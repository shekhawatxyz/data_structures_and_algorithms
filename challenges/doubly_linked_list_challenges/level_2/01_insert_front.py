# Level 2.1 - insert_front(head, value)
# Write insert_front(head, value) that inserts a new node at the front
# and returns the new head.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def insert_front(head, value):
    raise NotImplementedError('Implement insert_front(head, value).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_insert_front_on_empty_list_creates_single_node():
    new_head = insert_front(None, 5)
    _assert_equal(_to_list_forward(new_head), [5], 'insert_front(None, 5) should create [5].')
    _assert_true(new_head.prev is None, 'New head.prev must be None.')


def test_insert_front_on_non_empty_list_updates_bidirectional_links():
    head = _make_doubly_linked_list([2, 3])
    new_head = insert_front(head, 1)
    _assert_equal(_to_list_forward(new_head), [1, 2, 3], 'insert_front should prepend the new value.')
    _assert_true(new_head.next is head, 'New head.next should point to old head.')
    _assert_true(head.prev is new_head, 'Old head.prev should point back to new head.')


def test_insert_front_preserves_existing_tail_chain():
    head = _make_doubly_linked_list([4, 5, 6])
    new_head = insert_front(head, 3)
    _assert_equal(_to_list_forward(new_head), [3, 4, 5, 6], 'Existing nodes should remain after new head.')
    _assert_true(_verify_bidirectional_links(new_head), 'All links should stay valid after insert_front.')


def test_insert_front_with_duplicate_values():
    head = _make_doubly_linked_list([7, 7])
    new_head = insert_front(head, 7)
    _assert_equal(_to_list_forward(new_head), [7, 7, 7], 'insert_front should handle duplicate values.')


if __name__ == '__main__':
    TEST_CASES = [
        ('empty list insert_front', test_insert_front_on_empty_list_creates_single_node),
        ('non-empty insert updates links', test_insert_front_on_non_empty_list_updates_bidirectional_links),
        ('tail chain preserved', test_insert_front_preserves_existing_tail_chain),
        ('duplicate values handled', test_insert_front_with_duplicate_values),
    ]
    _run_all_tests(TEST_CASES)
