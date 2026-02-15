# Level 1.4 - length(head)
# Write a function length(head) that returns the number of nodes in the list.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_length_of_empty_list_is_zero():
    _assert_equal(length(None), 0, "length(None) should be 0.")


def test_length_of_single_node_list_is_one():
    head = _make_linked_list([10])
    _assert_equal(length(head), 1, "A single-node list should have length 1.")


def test_length_of_multiple_nodes():
    head = _make_linked_list([1, 2, 3, 4, 5])
    _assert_equal(length(head), 5, "List [1,2,3,4,5] should have length 5.")


def test_length_with_duplicate_values():
    head = _make_linked_list([2, 2, 2, 2])
    _assert_equal(length(head), 4, "Duplicate values still count as separate nodes.")


if __name__ == "__main__":
    TEST_CASES = [
        ("empty list length", test_length_of_empty_list_is_zero),
        ("single-node length", test_length_of_single_node_list_is_one),
        ("multi-node length", test_length_of_multiple_nodes),
        ("duplicate values still count", test_length_with_duplicate_values),
    ]
    _run_all_tests(TEST_CASES)
