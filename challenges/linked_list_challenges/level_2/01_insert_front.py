# Level 2.1 - insert_front(head, value)
# Write insert_front(head, value) that inserts at the front of the list
# and returns the new head.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert_front(head, value):
    v = Node(value)
    v.next = head
    head = v
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


def test_insert_front_on_empty_list():
    new_head = insert_front(None, 5)
    _assert_equal(
        _linked_list_to_list(new_head),
        [5],
        "insert_front(None, 5) should create a one-node list [5].",
    )


def test_insert_front_on_non_empty_list():
    original = _make_linked_list([2, 3])
    new_head = insert_front(original, 1)
    _assert_equal(
        _linked_list_to_list(new_head),
        [1, 2, 3],
        "insert_front should prepend the new value before existing nodes.",
    )


def test_new_head_points_to_old_head():
    original = _make_linked_list([8, 9])
    new_head = insert_front(original, 7)
    _assert_true(
        new_head.next is original,
        "The inserted front node should point to the previous head.",
    )


def test_insert_front_keeps_tail_values():
    original = _make_linked_list([4, 5, 6])
    new_head = insert_front(original, 3)
    _assert_equal(
        _linked_list_to_list(new_head),
        [3, 4, 5, 6],
        "insert_front should keep all previous nodes after the new head.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("insert into empty list", test_insert_front_on_empty_list),
        ("insert into non-empty list", test_insert_front_on_non_empty_list),
        ("new head points to old head", test_new_head_points_to_old_head),
        ("tail values preserved", test_insert_front_keeps_tail_values),
    ]
    _run_all_tests(TEST_CASES)
