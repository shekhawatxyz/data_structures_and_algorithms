# Level 4.4 - reverse_traversal(head, start, end)
# Write reverse_traversal(head, start, end) that prints values from index
# end back to start without auxiliary data structures.

import io
from contextlib import redirect_stdout

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def reverse_traversal(head, start, end):
    raise NotImplementedError('Implement reverse_traversal(head, start, end).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def _extract_output_values(head, start, end):
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        result = reverse_traversal(head, start, end)

    if result is not None:
        if isinstance(result, (list, tuple)):
            values = []
            for item in result:
                values.append(item.data if hasattr(item, 'data') else item)
            return values
        return [result.data] if hasattr(result, 'data') else [result]

    raw = buffer.getvalue().strip()
    if not raw:
        return []

    tokens = []
    cleaned = raw.replace('->', ' ').replace(',', ' ')
    for token in cleaned.split():
        token = token.strip('[]()')
        if token == '' or token == 'None':
            continue
        try:
            tokens.append(int(token))
        except ValueError:
            tokens.append(token)

    return tokens


def test_reverse_traversal_middle_segment():
    head = _make_doubly_linked_list([10, 20, 30, 40, 50])
    values = _extract_output_values(head, 1, 3)
    _assert_equal(values, [40, 30, 20], 'reverse_traversal should output values from end to start indices.')


def test_reverse_traversal_single_index_range():
    head = _make_doubly_linked_list([1, 2, 3])
    values = _extract_output_values(head, 2, 2)
    _assert_equal(values, [3], 'When start==end, reverse_traversal should output exactly one value.')


def test_reverse_traversal_full_range():
    head = _make_doubly_linked_list([1, 2, 3, 4])
    values = _extract_output_values(head, 0, 3)
    _assert_equal(values, [4, 3, 2, 1], 'Full-range reverse_traversal should output the full reverse order.')


def test_reverse_traversal_raises_for_invalid_ranges():
    head = _make_doubly_linked_list([1, 2, 3])
    _assert_raises(lambda: reverse_traversal(head, -1, 2), 'reverse_traversal should raise for negative start index.')
    _assert_raises(lambda: reverse_traversal(head, 2, 1), 'reverse_traversal should raise when start > end.')


if __name__ == '__main__':
    TEST_CASES = [
        ('middle segment reverse traversal', test_reverse_traversal_middle_segment),
        ('single index range', test_reverse_traversal_single_index_range),
        ('full range reverse traversal', test_reverse_traversal_full_range),
        ('invalid ranges raise', test_reverse_traversal_raises_for_invalid_ranges),
    ]
    _run_all_tests(TEST_CASES)
