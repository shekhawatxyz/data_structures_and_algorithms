# Level 3.2 - delete_first(head, value)
# Write delete_first(head, value) that removes the first matching value
# and returns the new head.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def delete_first(head, value):
    raise NotImplementedError('Implement delete_first(head, value).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_delete_first_removes_first_matching_occurrence_only():
    head = _make_doubly_linked_list([1, 2, 2, 3])
    result = delete_first(head, 2)
    _assert_equal(_to_list_forward(result), [1, 2, 3], 'delete_first should remove only the first matching node.')


def test_delete_first_removes_head_if_it_matches():
    head = _make_doubly_linked_list([5, 6, 7])
    result = delete_first(head, 5)
    _assert_equal(_to_list_forward(result), [6, 7], 'delete_first should remove the head when it matches.')
    _assert_true(result.prev is None, 'New head.prev should be None after deleting old head.')


def test_delete_first_no_match_leaves_list_unchanged():
    head = _make_doubly_linked_list([1, 2, 3])
    result = delete_first(head, 99)
    _assert_equal(_to_list_forward(result), [1, 2, 3], 'List should remain unchanged when value is absent.')
    _assert_true(_verify_bidirectional_links(result), 'Links should remain valid when no node is deleted.')


def test_delete_first_on_empty_list_returns_none():
    _assert_true(delete_first(None, 1) is None, 'delete_first(None, value) should return None.')


if __name__ == '__main__':
    TEST_CASES = [
        ('remove first matching occurrence', test_delete_first_removes_first_matching_occurrence_only),
        ('remove matching head', test_delete_first_removes_head_if_it_matches),
        ('no match keeps list unchanged', test_delete_first_no_match_leaves_list_unchanged),
        ('empty list returns None', test_delete_first_on_empty_list_returns_none),
    ]
    _run_all_tests(TEST_CASES)
