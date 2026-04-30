# Level 5.3 - partition(head, x)
# Write partition(head, x) that stably places values < x before values
# >= x while preserving order within each partition.

# Complete Exact Problem Statement (from doubly-linked-list-challenges.md):
# **5.3** Write `partition(head, x)` — rearrange so all values less than `x` come before all values ≥ `x`, preserving relative order within each group. Return the new head.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


def partition(head, x):
    if head is None:
        return None
    current = head
    dummy1 = Node(0)
    dummy2 = Node(0)
    current1 = dummy1
    current2 = dummy2
    while current:
        cn = current.next
        if current.data < x:
            current1.next = current
            current.prev = current1
            current1 = current
            current.next = None
        else:
            current2.next = current
            current.prev = current2
            current2 = current
            current.next = None
        current = cn
    d1 = dummy1.next
    dummy1.next = None
    if not d1:
        if dummy2.next:
            dummy2.next.prev = None
            return dummy2.next
    d1.prev = None
    current1.next = dummy2.next
    if dummy2.next:
        dummy2.next.prev = current1
    return d1


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
                "Forward traversal exceeded safety limit; possible cycle or broken links."
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
                "Backward traversal exceeded safety limit; possible cycle or broken links."
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
            raise AssertionError(
                "Node traversal exceeded safety limit; possible cycle."
            )

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


def test_partition_mixed_values_preserves_stability():
    head = _make_doubly_linked_list([3, 5, 8, 5, 10, 2, 1])
    result = partition(head, 5)
    _assert_equal(
        _to_list_forward(result),
        [3, 2, 1, 5, 8, 5, 10],
        "partition should preserve relative order within <x and >=x groups.",
    )


def test_partition_all_values_less_than_x():
    head = _make_doubly_linked_list([1, 2, 3])
    result = partition(head, 10)
    _assert_equal(
        _to_list_forward(result),
        [1, 2, 3],
        "If all values are <x, list should remain unchanged.",
    )


def test_partition_all_values_greater_or_equal_x():
    head = _make_doubly_linked_list([7, 8, 9])
    result = partition(head, 5)
    _assert_equal(
        _to_list_forward(result),
        [7, 8, 9],
        "If all values are >=x, list should remain unchanged.",
    )


def test_partition_keeps_links_valid():
    head = _make_doubly_linked_list([4, 1, 3, 2])
    result = partition(head, 3)
    _assert_true(
        _verify_bidirectional_links(result),
        "All prev/next links should be valid after partition.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("stable mixed partition", test_partition_mixed_values_preserves_stability),
        ("all values < x", test_partition_all_values_less_than_x),
        ("all values >= x", test_partition_all_values_greater_or_equal_x),
        ("links valid after partition", test_partition_keeps_links_valid),
    ]
    _run_all_tests(TEST_CASES)
