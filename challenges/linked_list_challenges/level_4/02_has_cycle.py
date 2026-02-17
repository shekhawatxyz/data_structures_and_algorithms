# Level 4.2 - has_cycle(head)
# Write has_cycle(head) that returns True if the linked list contains
# a cycle, and False otherwise.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def has_cycle(head):
    a = head
    seen = set()
    if a is None:
        return False
    while a is not None:
        if a in seen:
            return True
        seen.add(a)
        a = a.next
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


def _make_cyclic_list(values, cycle_index):
    head = _make_linked_list(values)
    if head is None:
        return None

    tail = None
    cycle_target = None
    current = head
    index = 0
    while current is not None:
        if index == cycle_index:
            cycle_target = current
        tail = current
        current = current.next
        index += 1

    if tail is not None and cycle_target is not None:
        tail.next = cycle_target

    return head


def test_has_cycle_false_for_acyclic_list():
    head = _make_linked_list([1, 2, 3, 4])
    _assert_equal(
        has_cycle(head), False, "A normal list without loops should return False."
    )


def test_has_cycle_true_for_tail_link_to_middle():
    head = _make_cyclic_list([1, 2, 3, 4, 5], 2)
    _assert_equal(
        has_cycle(head), True, "A tail-to-middle link should be detected as a cycle."
    )


def test_has_cycle_true_for_single_node_self_cycle():
    node = Node(99)
    node.next = node
    _assert_equal(has_cycle(node), True, "A single node pointing to itself is a cycle.")


def test_has_cycle_false_for_empty_list():
    _assert_equal(
        has_cycle(None), False, "An empty list should not be considered cyclic."
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("acyclic list returns False", test_has_cycle_false_for_acyclic_list),
        ("tail-to-middle cycle detected", test_has_cycle_true_for_tail_link_to_middle),
        ("self-cycle detected", test_has_cycle_true_for_single_node_self_cycle),
        ("empty list returns False", test_has_cycle_false_for_empty_list),
    ]
    _run_all_tests(TEST_CASES)
