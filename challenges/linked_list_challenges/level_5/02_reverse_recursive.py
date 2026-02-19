# Level 5.2 - reverse_recursive(head)
# Write reverse_recursive(head) that reverses a linked list recursively
# and returns the new head.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_recursive(head):
    if head is None:
        return None
    elif head.next is None:
        return head
    else:
        new_head = reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
                "Linked list traversal exceeded a safety limit. "
                "Your list might contain an unexpected cycle."
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
                "Node-id traversal exceeded a safety limit. "
                "Your list might contain an unexpected cycle."
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


def test_reverse_recursive_empty_list_returns_none():
    result = reverse_recursive(None)
    _assert_true(result is None, "reverse_recursive(None) should return None.")


def test_reverse_recursive_single_node_list():
    head = _make_linked_list([11])
    result = reverse_recursive(head)
    _assert_equal(
        _linked_list_to_list(result),
        [11],
        "Single-node recursive reverse should stay [11].",
    )


def test_reverse_recursive_multiple_nodes():
    head = _make_linked_list([1, 2, 3, 4, 5])
    result = reverse_recursive(head)
    _assert_equal(
        _linked_list_to_list(result),
        [5, 4, 3, 2, 1],
        "reverse_recursive should invert all nodes in the list.",
    )


def test_reverse_recursive_with_duplicates():
    head = _make_linked_list([9, 9, 8])
    result = reverse_recursive(head)
    _assert_equal(
        _linked_list_to_list(result),
        [8, 9, 9],
        "reverse_recursive should handle repeated values correctly.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty recursive reverse", test_reverse_recursive_empty_list_returns_none),
        ("single-node recursive reverse", test_reverse_recursive_single_node_list),
        ("multi-node recursive reverse", test_reverse_recursive_multiple_nodes),
        ("duplicates recursive reverse", test_reverse_recursive_with_duplicates),
    ]
    _run_all_tests(TEST_CASES)
