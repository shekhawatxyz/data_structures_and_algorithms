# Level 6.1 - merge_sorted(head1, head2)
# Write merge_sorted(head1, head2) that merges two sorted doubly linked
# lists by re-linking existing nodes with correct prev pointers.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def merge_sorted(head1, head2):
    raise NotImplementedError('Implement merge_sorted(head1, head2).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_merge_sorted_basic_interleaving():
    head1 = _make_doubly_linked_list([1, 3, 5])
    head2 = _make_doubly_linked_list([2, 4, 6])
    expected_ids = set(_node_ids(head1) + _node_ids(head2))

    result = merge_sorted(head1, head2)
    _assert_equal(_to_list_forward(result), [1, 2, 3, 4, 5, 6], 'merge_sorted should merge into sorted order.')
    _assert_true(_verify_bidirectional_links(result), 'All prev/next links should be valid after merge.')
    _assert_equal(set(_node_ids(result)), expected_ids, 'merge_sorted should reuse existing nodes only.')


def test_merge_sorted_with_one_empty_input():
    head1 = _make_doubly_linked_list([1, 2, 3])
    result = merge_sorted(head1, None)
    _assert_equal(_to_list_forward(result), [1, 2, 3], 'Merging with empty list should return non-empty list.')


def test_merge_sorted_with_duplicates():
    head1 = _make_doubly_linked_list([1, 2, 2])
    head2 = _make_doubly_linked_list([2, 3])
    result = merge_sorted(head1, head2)
    _assert_equal(_to_list_forward(result), [1, 2, 2, 2, 3], 'merge_sorted should preserve duplicates correctly.')


def test_merge_sorted_with_both_empty_inputs():
    _assert_true(merge_sorted(None, None) is None, 'merge_sorted(None, None) should return None.')


if __name__ == '__main__':
    TEST_CASES = [
        ('basic sorted merge', test_merge_sorted_basic_interleaving),
        ('one empty input', test_merge_sorted_with_one_empty_input),
        ('merge with duplicates', test_merge_sorted_with_duplicates),
        ('both empty inputs', test_merge_sorted_with_both_empty_inputs),
    ]
    _run_all_tests(TEST_CASES)
