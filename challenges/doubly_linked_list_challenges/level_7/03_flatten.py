# Level 7.3 - flatten(head)
# Write flatten(head) for a multilevel doubly linked list where each node
# may have a child list inserted immediately after the node.

class Node:
    def __init__(self, data, prev=None, next=None, child=None):
        self.data = data
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    raise NotImplementedError('Implement flatten(head).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def _assert_no_child_links(head):
    current = head
    steps = 0
    while current is not None:
        _assert_true(current.child is None, 'All child pointers should be None after flattening.')
        current = current.next
        steps += 1
        if steps > 2000:
            raise AssertionError('Traversal exceeded safety limit while checking child pointers.')


def _build_multilevel_example():
    # Main: 1 - 2 - 3
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next, n2.prev = n2, n1
    n2.next, n3.prev = n3, n2

    # Child of 2: 7 - 8
    n7 = Node(7)
    n8 = Node(8)
    n7.next, n8.prev = n8, n7
    n2.child = n7

    # Child of 8: 11 - 12
    n11 = Node(11)
    n12 = Node(12)
    n11.next, n12.prev = n12, n11
    n8.child = n11

    # Child of 3: 9 - 10
    n9 = Node(9)
    n10 = Node(10)
    n9.next, n10.prev = n10, n9
    n3.child = n9

    return n1


def test_flatten_multilevel_structure_depth_first_order():
    head = _build_multilevel_example()
    result = flatten(head)
    _assert_equal(
        _to_list_forward(result),
        [1, 2, 7, 8, 11, 12, 3, 9, 10],
        'flatten should splice child lists immediately after parent nodes in depth-first order.',
    )
    _assert_true(_verify_bidirectional_links(result), 'All prev/next links should remain consistent after flatten.')
    _assert_no_child_links(result)


def test_flatten_already_flat_list_unchanged():
    head = _make_doubly_linked_list([1, 2, 3])
    result = flatten(head)
    _assert_equal(_to_list_forward(result), [1, 2, 3], 'Flattening a flat list should keep order unchanged.')
    _assert_true(_verify_bidirectional_links(result), 'Flat list links should remain valid after flatten.')


def test_flatten_single_node_with_child():
    head = Node(1)
    child1 = Node(2)
    child2 = Node(3)
    child1.next, child2.prev = child2, child1
    head.child = child1

    result = flatten(head)
    _assert_equal(_to_list_forward(result), [1, 2, 3], 'Single parent with child chain should flatten directly after parent.')
    _assert_true(_verify_bidirectional_links(result), 'Links should remain valid for flattened single-parent case.')
    _assert_no_child_links(result)


def test_flatten_empty_input_returns_none():
    _assert_true(flatten(None) is None, 'flatten(None) should return None.')


if __name__ == '__main__':
    TEST_CASES = [
        ('multilevel depth-first flatten', test_flatten_multilevel_structure_depth_first_order),
        ('already-flat list unchanged', test_flatten_already_flat_list_unchanged),
        ('single parent with child chain', test_flatten_single_node_with_child),
        ('empty input returns None', test_flatten_empty_input_returns_none),
    ]
    _run_all_tests(TEST_CASES)
