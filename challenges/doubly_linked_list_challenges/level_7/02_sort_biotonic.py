# Level 7.2 - sort_biotonic(head)
# Write sort_biotonic(head) for lists that increase then decrease,
# returning a fully sorted list in ascending order.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def sort_biotonic(head):
    raise NotImplementedError('Implement sort_biotonic(head).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def test_sort_biotonic_basic_peak_case():
    head = _make_doubly_linked_list([1, 3, 7, 5, 2])
    result = sort_biotonic(head)
    _assert_equal(_to_list_forward(result), [1, 2, 3, 5, 7], 'Bitonic sequence should be sorted ascending.')
    _assert_true(_verify_bidirectional_links(result), 'All links should remain valid after sort_biotonic.')


def test_sort_biotonic_already_increasing_list():
    head = _make_doubly_linked_list([1, 2, 3, 4])
    result = sort_biotonic(head)
    _assert_equal(_to_list_forward(result), [1, 2, 3, 4], 'Already-increasing input should remain sorted.')


def test_sort_biotonic_with_duplicates():
    head = _make_doubly_linked_list([1, 4, 6, 6, 5, 2])
    result = sort_biotonic(head)
    _assert_equal(_to_list_forward(result), [1, 2, 4, 5, 6, 6], 'sort_biotonic should handle duplicate values.')


def test_sort_biotonic_empty_and_single_node_inputs():
    _assert_true(sort_biotonic(None) is None, 'sort_biotonic(None) should return None.')
    single = _make_doubly_linked_list([9])
    result = sort_biotonic(single)
    _assert_equal(_to_list_forward(result), [9], 'Single-node input should remain unchanged.')


if __name__ == '__main__':
    TEST_CASES = [
        ('basic bitonic sort case', test_sort_biotonic_basic_peak_case),
        ('already increasing list', test_sort_biotonic_already_increasing_list),
        ('bitonic with duplicates', test_sort_biotonic_with_duplicates),
        ('empty/single input handling', test_sort_biotonic_empty_and_single_node_inputs),
    ]
    _run_all_tests(TEST_CASES)
