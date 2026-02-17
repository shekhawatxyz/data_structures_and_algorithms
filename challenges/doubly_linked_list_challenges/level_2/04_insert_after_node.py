# Level 2.4 - insert_after_node(node, value)
# Write insert_after_node(node, value) that inserts immediately after
# the referenced node without needing the list head.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def insert_after_node(node, value):
    raise NotImplementedError('Implement insert_after_node(node, value).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_insert_after_middle_node():
    head = _make_doubly_linked_list([1, 2, 3])
    node = _find_first_node(head, 2)
    insert_after_node(node, 99)
    result_head = _head_from_any(node)
    _assert_equal(
        _to_list_forward(result_head),
        [1, 2, 99, 3],
        'insert_after_node should place the new value right after the given node.',
    )
    _assert_true(_verify_bidirectional_links(result_head), 'Links should remain valid after insert_after_node.')


def test_insert_after_tail_node_adds_new_tail():
    head = _make_doubly_linked_list([4, 5])
    tail = _tail_from_head(head)
    insert_after_node(tail, 6)
    result_head = _head_from_any(tail)
    _assert_equal(_to_list_forward(result_head), [4, 5, 6], 'Inserting after tail should append a new tail.')
    _assert_true(_tail_from_head(result_head).data == 6, 'The inserted node should become the new tail.')


def test_insert_after_node_none_raises_error():
    _assert_raises(
        lambda: insert_after_node(None, 1),
        'insert_after_node should raise an error for node=None.',
    )


def test_insert_after_node_preserves_neighbors():
    head = _make_doubly_linked_list([10, 20, 30])
    node20 = _find_first_node(head, 20)
    node30 = node20.next
    insert_after_node(node20, 25)
    result_head = _head_from_any(node20)
    inserted = node20.next
    _assert_true(inserted.data == 25, 'The new node should be inserted after the reference node.')
    _assert_true(inserted.prev is node20, 'Inserted node.prev should point to the reference node.')
    _assert_true(inserted.next is node30, 'Inserted node.next should point to the old successor.')


if __name__ == '__main__':
    TEST_CASES = [
        ('insert after middle node', test_insert_after_middle_node),
        ('insert after tail node', test_insert_after_tail_node_adds_new_tail),
        ('node=None raises error', test_insert_after_node_none_raises_error),
        ('neighbor pointers preserved', test_insert_after_node_preserves_neighbors),
    ]
    _run_all_tests(TEST_CASES)
