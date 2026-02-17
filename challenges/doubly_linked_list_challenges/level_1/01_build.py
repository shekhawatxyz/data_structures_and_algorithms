# Level 1.1 - build(values)
# Write build(values) that takes a Python list and returns the head
# of a doubly linked list with correct prev and next pointers.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def build(values):
    raise NotImplementedError('Implement build(values).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_build_empty_returns_none():
    result = build([])
    _assert_true(result is None, 'build([]) should return None for an empty input list.')


def test_build_single_value_has_no_neighbors():
    head = build([42])
    _assert_equal(_to_list_forward(head), [42], 'build([42]) should produce a one-node list [42].')
    _assert_true(head.prev is None, 'Head.prev should be None for a single-node list.')
    _assert_true(head.next is None, 'Head.next should be None for a single-node list.')


def test_build_multiple_values_sets_prev_and_next_correctly():
    head = build([1, 2, 3, 4])
    _assert_equal(_to_list_forward(head), [1, 2, 3, 4], 'build should preserve forward order.')
    _assert_equal(_to_list_backward(head), [4, 3, 2, 1], 'Backward traversal should match reverse order.')
    _assert_true(
        _verify_bidirectional_links(head),
        'All prev/next links should be consistent after build(values).',
    )


def test_build_creates_distinct_node_objects_for_duplicates():
    head = build([7, 7, 7])
    ids = _node_ids(head)
    _assert_equal(len(ids), 3, 'build should create one node per input element.')
    _assert_equal(len(set(ids)), 3, 'Duplicate values must still produce distinct node objects.')


if __name__ == '__main__':
    TEST_CASES = [
        ('empty input returns None', test_build_empty_returns_none),
        ('single value has no neighbors', test_build_single_value_has_no_neighbors),
        ('multiple values set bidirectional links', test_build_multiple_values_sets_prev_and_next_correctly),
        ('duplicate values still create distinct nodes', test_build_creates_distinct_node_objects_for_duplicates),
    ]
    _run_all_tests(TEST_CASES)
