# Level 2.2 - insert_back(head, value)
# Write insert_back(head, value) that appends at the end of the list
# and returns the head. Handle the empty-list case.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert_back(head, value):
    v = Node(value)
    a = head
    if a is None:
        a = v
        return a
    while a.next is not None:
        a = a.next
    a.next = v
    return head


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_insert_back_on_empty_list():
    result = insert_back(None, 10)
    _assert_equal(
        _linked_list_to_list(result),
        [10],
        "insert_back(None, 10) should return a one-node list [10].",
    )


def test_insert_back_appends_to_existing_list():
    head = _make_linked_list([1, 2])
    result = insert_back(head, 3)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3],
        "insert_back should append the new value at the tail.",
    )


def test_insert_back_keeps_original_head_identity():
    head = _make_linked_list([7, 8])
    result = insert_back(head, 9)
    _assert_true(
        result is head,
        "For a non-empty list, insert_back should return the original head object.",
    )


def test_insert_back_preserves_existing_node_order():
    head = _make_linked_list([4, 5, 6])
    existing_ids = _node_ids(head)
    result = insert_back(head, 99)
    resulting_ids = _node_ids(result)
    _assert_equal(
        resulting_ids[:3],
        existing_ids,
        "insert_back should preserve the order and identity of existing nodes.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty list insert_back", test_insert_back_on_empty_list),
        ("append to existing list", test_insert_back_appends_to_existing_list),
        ("head identity preserved", test_insert_back_keeps_original_head_identity),
        (
            "existing node order preserved",
            test_insert_back_preserves_existing_node_order,
        ),
    ]
    _run_all_tests(TEST_CASES)
