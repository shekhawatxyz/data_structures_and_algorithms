# Level 6.4 - split_alternating(head)
# Write split_alternating(head) that splits one list into two lists
# by alternating nodes, and returns both heads.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def split_alternating(head):
    raise NotImplementedError('Implement split_alternating(head).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

def _make_linked_list(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def _linked_list_to_list(head, max_nodes=2000):
    values = []
    current = head
    steps = 0

    while current is not None:
        values.append(current.data)
        current = current.next
        steps += 1
        if steps > max_nodes:
            raise AssertionError(
                'Linked list traversal exceeded a safety limit. '
                'Your list might contain an unexpected cycle.'
            )

    return values


def _node_ids(head, max_nodes=2000):
    ids = []
    current = head
    steps = 0

    while current is not None:
        ids.append(id(current))
        current = current.next
        steps += 1
        if steps > max_nodes:
            raise AssertionError(
                'Node-id traversal exceeded a safety limit. '
                'Your list might contain an unexpected cycle.'
            )

    return ids


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

def _as_two_heads(result):
    _assert_true(
        isinstance(result, (tuple, list)) and len(result) == 2,
        'split_alternating should return a pair (head_a, head_b).',
    )
    return result[0], result[1]


def test_split_alternating_odd_length_list():
    original = _make_linked_list([1, 2, 3, 4, 5])
    expected_ids = set(_node_ids(original))

    head_a, head_b = _as_two_heads(split_alternating(original))
    _assert_equal(
        _linked_list_to_list(head_a),
        [1, 3, 5],
        'Odd-length split should place indices 0,2,4 in first list.',
    )
    _assert_equal(
        _linked_list_to_list(head_b),
        [2, 4],
        'Odd-length split should place indices 1,3 in second list.',
    )

    result_ids = set(_node_ids(head_a) + _node_ids(head_b))
    _assert_equal(
        result_ids,
        expected_ids,
        'split_alternating should reuse all original nodes exactly once.',
    )


def test_split_alternating_even_length_list():
    head = _make_linked_list([10, 20, 30, 40])
    head_a, head_b = _as_two_heads(split_alternating(head))
    _assert_equal(_linked_list_to_list(head_a), [10, 30], 'First output should be indices 0 and 2.')
    _assert_equal(_linked_list_to_list(head_b), [20, 40], 'Second output should be indices 1 and 3.')


def test_split_alternating_single_node_list():
    head = _make_linked_list([99])
    head_a, head_b = _as_two_heads(split_alternating(head))
    _assert_equal(_linked_list_to_list(head_a), [99], 'Single node should go to first list.')
    _assert_true(head_b is None, 'Second list should be None for single-node input.')


def test_split_alternating_empty_list():
    head_a, head_b = _as_two_heads(split_alternating(None))
    _assert_true(head_a is None and head_b is None, 'Empty input should return (None, None).')


if __name__ == '__main__':
    TEST_CASES = [
        ('odd length alternating split', test_split_alternating_odd_length_list),
        ('even length alternating split', test_split_alternating_even_length_list),
        ('single-node alternating split', test_split_alternating_single_node_list),
        ('empty alternating split', test_split_alternating_empty_list),
    ]
    _run_all_tests(TEST_CASES)
