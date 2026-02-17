# Level 2.5 - insert_before_node(node, value)
# Write insert_before_node(node, value) that inserts immediately before
# the referenced node without needing the list head.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def insert_before_node(node, value):
    raise NotImplementedError('Implement insert_before_node(node, value).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_insert_before_middle_node():
    head = _make_doubly_linked_list([1, 2, 3])
    node2 = _find_first_node(head, 2)
    insert_before_node(node2, 99)
    result_head = _head_from_any(node2)
    _assert_equal(
        _to_list_forward(result_head),
        [1, 99, 2, 3],
        'insert_before_node should place the new value right before the given node.',
    )
    _assert_true(_verify_bidirectional_links(result_head), 'Links should remain valid after insert_before_node.')


def test_insert_before_head_node_creates_new_head():
    head = _make_doubly_linked_list([4, 5])
    insert_before_node(head, 3)
    result_head = _head_from_any(head)
    _assert_equal(_to_list_forward(result_head), [3, 4, 5], 'Inserting before head should create a new head.')
    _assert_true(result_head.prev is None, 'New head.prev should be None.')


def test_insert_before_node_none_raises_error():
    _assert_raises(
        lambda: insert_before_node(None, 1),
        'insert_before_node should raise an error for node=None.',
    )


def test_insert_before_node_preserves_neighbors():
    head = _make_doubly_linked_list([10, 20, 30])
    node20 = _find_first_node(head, 20)
    node10 = node20.prev
    insert_before_node(node20, 15)
    result_head = _head_from_any(node20)
    inserted = node20.prev
    _assert_true(inserted.data == 15, 'Inserted node should be right before the reference node.')
    _assert_true(inserted.prev is node10, 'Inserted node.prev should point to old predecessor.')
    _assert_true(inserted.next is node20, 'Inserted node.next should point to reference node.')
    _assert_true(_verify_bidirectional_links(result_head), 'All links should be consistent after insertion.')


if __name__ == '__main__':
    TEST_CASES = [
        ('insert before middle node', test_insert_before_middle_node),
        ('insert before head node', test_insert_before_head_node_creates_new_head),
        ('node=None raises error', test_insert_before_node_none_raises_error),
        ('neighbor pointers preserved', test_insert_before_node_preserves_neighbors),
    ]
    _run_all_tests(TEST_CASES)
