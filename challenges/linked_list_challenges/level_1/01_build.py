# Level 1.1 - build(values)
# Write a function build(values) that takes a Python list and returns
# the head of a singly linked list containing those values in order.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def build(values):
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


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_empty_input_returns_none():
    result = build([])
    _assert_true(
        result is None, "build([]) should return None for an empty input list."
    )


def test_single_value_builds_single_node():
    result = build([42])
    _assert_equal(
        _linked_list_to_list(result),
        [42],
        "build([42]) should create one node with value 42.",
    )


def test_multiple_values_preserve_order():
    values = [3, 7, 2, 7]
    result = build(values)
    _assert_equal(
        _linked_list_to_list(result),
        values,
        "build(values) should preserve the original order of values.",
    )


def test_repeated_values_create_distinct_nodes():
    result = build([1, 1, 1])
    ids = _node_ids(result)
    _assert_equal(len(ids), 3, "build([1,1,1]) should create exactly 3 nodes.")
    _assert_equal(
        len(set(ids)),
        3,
        "Each node in the built list should be a distinct object, even for repeated values.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("empty input returns None", test_empty_input_returns_none),
        ("single value builds one node", test_single_value_builds_single_node),
        ("multiple values preserve order", test_multiple_values_preserve_order),
        (
            "repeated values create distinct nodes",
            test_repeated_values_create_distinct_nodes,
        ),
    ]
    _run_all_tests(TEST_CASES)
