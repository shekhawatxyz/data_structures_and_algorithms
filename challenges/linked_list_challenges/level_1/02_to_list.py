# Level 1.2 - to_list(head)
# Write a function to_list(head) that takes the head of a linked list
# and returns a Python list of its values.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def to_list(head):
    y = []
    while head is not None:
        y.append(head.data)
        head = head.next
    return list(y)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_none_head_returns_empty_list():
    result = to_list(None)
    _assert_equal(result, [], "to_list(None) should return an empty Python list.")


def test_single_node_to_list():
    head = _make_linked_list([9])
    result = to_list(head)
    _assert_equal(result, [9], "to_list() should return [9] for a single-node list.")


def test_multiple_nodes_to_list_preserves_order():
    head = _make_linked_list([1, 2, 3, 4])
    result = to_list(head)
    _assert_equal(
        result,
        [1, 2, 3, 4],
        "to_list() should preserve node order when converting to a Python list.",
    )


def test_duplicates_are_preserved():
    head = _make_linked_list([5, 5, 1, 5])
    result = to_list(head)
    _assert_equal(
        result, [5, 5, 1, 5], "to_list() should keep duplicate values intact."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("None head returns []", test_none_head_returns_empty_list),
        ("single node conversion", test_single_node_to_list),
        ("multiple nodes preserve order", test_multiple_nodes_to_list_preserves_order),
        ("duplicates are preserved", test_duplicates_are_preserved),
    ]
    _run_all_tests(TEST_CASES)
