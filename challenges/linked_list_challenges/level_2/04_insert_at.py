# Level 2.4 - insert_at(head, index, value)
# Write insert_at(head, index, value) to insert at the 0-indexed position.
# Return the new head, and raise an error if index is out of range.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert_at(head, index, value):
    a = head
    count = 0
    v = Node(value)
    if index < 0:
        raise IndexError
    if index == 0:
        v.next = a
        a = v
        return a
    while a is not None:
        if count == index - 1:
            v.next = a.next
            a.next = v
            return head
        a = a.next
        count += 1
    if index > count:
        raise IndexError


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_insert_at_index_zero_prepends():
    head = _make_linked_list([2, 3])
    result = insert_at(head, 0, 1)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3],
        "insert_at(..., 0, value) should prepend at the head.",
    )


def test_insert_at_middle_position():
    head = _make_linked_list([1, 3, 4])
    result = insert_at(head, 1, 2)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3, 4],
        "insert_at should correctly insert into the middle of the list.",
    )


def test_insert_at_end_appends():
    head = _make_linked_list([1, 2, 3])
    result = insert_at(head, 3, 4)
    _assert_equal(
        _linked_list_to_list(result),
        [1, 2, 3, 4],
        "insert_at at index == length should append at the tail.",
    )


def test_insert_at_empty_list_with_zero_index():
    result = insert_at(None, 0, 99)
    _assert_equal(
        _linked_list_to_list(result),
        [99],
        "insert_at(None, 0, value) should create a one-node list.",
    )


def test_insert_at_raises_for_out_of_range_and_negative_indexes():
    head = _make_linked_list([1, 2, 3])
    _assert_raises(
        lambda: insert_at(head, 10, 5),
        "insert_at should raise an error when index is greater than list length.",
    )
    _assert_raises(
        lambda: insert_at(head, -1, 5),
        "insert_at should raise an error for negative indexes.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("index 0 prepends", test_insert_at_index_zero_prepends),
        ("middle insertion", test_insert_at_middle_position),
        ("end insertion appends", test_insert_at_end_appends),
        ("empty list with index 0", test_insert_at_empty_list_with_zero_index),
        (
            "out-of-range indexes raise",
            test_insert_at_raises_for_out_of_range_and_negative_indexes,
        ),
    ]
    _run_all_tests(TEST_CASES)
