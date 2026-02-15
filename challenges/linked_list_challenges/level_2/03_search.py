# Level 2.3 - search(head, value)
# Write search(head, value) that returns True if value is present,
# and False otherwise.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def search(head, value):
    # a = head
    while head is not None:
        if head.data == value:
            return True
        head = head.next
    return False


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_search_empty_list_returns_false():
    _assert_equal(search(None, 1), False, "search(None, 1) should be False.")


def test_search_finds_head_value():
    head = _make_linked_list([5, 6, 7])
    _assert_equal(search(head, 5), True, "search should find a value at the head.")


def test_search_finds_middle_and_tail_values():
    head = _make_linked_list([5, 6, 7, 8])
    _assert_equal(search(head, 7), True, "search should find values in the middle.")
    _assert_equal(search(head, 8), True, "search should find values at the tail.")


def test_search_returns_false_for_missing_value():
    head = _make_linked_list([1, 2, 3])
    _assert_equal(
        search(head, 9), False, "search should return False when value is absent."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty list is always false", test_search_empty_list_returns_false),
        ("finds head value", test_search_finds_head_value),
        ("finds middle and tail values", test_search_finds_middle_and_tail_values),
        ("missing value returns false", test_search_returns_false_for_missing_value),
    ]
    _run_all_tests(TEST_CASES)
