# Level 4.2 - pairs_with_sum(head, target)
# Write pairs_with_sum(head, target) for a sorted list using a head/tail
# two-pointer approach and return all matching value pairs.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def pairs_with_sum(head, target):
    raise NotImplementedError('Implement pairs_with_sum(head, target).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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

def _normalize_pairs(result):
    if result is None:
        return []

    normalized = []
    for pair in result:
        items = list(pair)
        _assert_equal(len(items), 2, 'Each pair output should contain exactly two elements.')

        left = items[0].data if hasattr(items[0], 'data') else items[0]
        right = items[1].data if hasattr(items[1], 'data') else items[1]

        normalized.append((left, right))

    return sorted(normalized)


def test_pairs_with_sum_finds_all_expected_pairs():
    head = _make_doubly_linked_list([1, 2, 3, 4, 5, 6])
    result = _normalize_pairs(pairs_with_sum(head, 7))
    _assert_equal(
        result,
        [(1, 6), (2, 5), (3, 4)],
        'pairs_with_sum should find all valid head/tail inward pairs summing to target.',
    )


def test_pairs_with_sum_returns_empty_when_no_pairs_exist():
    head = _make_doubly_linked_list([1, 2, 3, 4])
    result = _normalize_pairs(pairs_with_sum(head, 100))
    _assert_equal(result, [], 'pairs_with_sum should return no pairs when target is impossible.')


def test_pairs_with_sum_handles_two_node_list():
    head = _make_doubly_linked_list([4, 9])
    _assert_equal(_normalize_pairs(pairs_with_sum(head, 13)), [(4, 9)], 'Two-node exact match should be found.')
    _assert_equal(_normalize_pairs(pairs_with_sum(head, 7)), [], 'Two-node non-match should return empty result.')


def test_pairs_with_sum_handles_empty_list():
    result = _normalize_pairs(pairs_with_sum(None, 5))
    _assert_equal(result, [], 'pairs_with_sum(None, target) should return empty output.')


if __name__ == '__main__':
    TEST_CASES = [
        ('finds all expected pairs', test_pairs_with_sum_finds_all_expected_pairs),
        ('no-pair target returns empty', test_pairs_with_sum_returns_empty_when_no_pairs_exist),
        ('two-node list behavior', test_pairs_with_sum_handles_two_node_list),
        ('empty list behavior', test_pairs_with_sum_handles_empty_list),
    ]
    _run_all_tests(TEST_CASES)
