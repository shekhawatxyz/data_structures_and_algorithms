# Level 3.2 - delete_all(head, value)
# Write delete_all(head, value) that removes every node with the
# given value and returns the new head.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def delete_all(head, value):
    if head is None:
        return None
    dummy = Node(1)
    dummy.next = head
    a = dummy
    while a is not None:
        if a.next is None:
            return dummy.next
        if a.next.data == value:
            a.next = a.next.next
        else:
            a = a.next


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_delete_all_removes_matches_anywhere():
    head = _make_linked_list([2, 1, 2, 3, 2, 4])
    result = delete_all(head, 2)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 3, 4],
        "delete_all should remove all matching values from head, middle, and tail.",
    )


def test_delete_all_when_no_matches():
    head = _make_linked_list([1, 3, 5])
    result = delete_all(head, 2)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 3, 5],
        "If no values match, delete_all should leave the list unchanged.",
    )


def test_delete_all_when_all_nodes_match():
    head = _make_linked_list([7, 7, 7])
    result = delete_all(head, 7)
    _assert_true(
        result is None, "If every node matches, delete_all should return None."
    )


def test_delete_all_on_empty_list_returns_none():
    result = delete_all(None, 1)
    _assert_true(result is None, "delete_all(None, value) should return None.")


if __name__ == "__main__":
    TEST_CASES = [
        ("remove matches from all positions", test_delete_all_removes_matches_anywhere),
        ("no matches keeps list", test_delete_all_when_no_matches),
        ("all nodes removed", test_delete_all_when_all_nodes_match),
        ("empty list returns None", test_delete_all_on_empty_list_returns_none),
    ]
    _run_all_tests(TEST_CASES)
