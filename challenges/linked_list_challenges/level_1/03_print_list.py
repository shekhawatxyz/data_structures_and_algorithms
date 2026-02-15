# Level 1.3 - print_list(head)
# Write a function print_list(head) that prints each element on one line,
# or in the format "3 -> 7 -> 2 -> None".

import io
from contextlib import redirect_stdout


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_list(head):
    y = []
    while head is not None:
        y.append(str(head.data))
        head = head.next
    for a in y:
        print(f"{a} ->")
    print(f"{None}")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _capture_print_output(head):
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        print_list(head)
    return buffer.getvalue().strip()


def _extract_printed_values(output):
    if output == "":
        return []

    if "->" in output:
        parts = [part.strip() for part in output.split("->") if part.strip()]
        if parts and parts[-1] == "None":
            parts = parts[:-1]
        return parts

    lines = [line.strip() for line in output.splitlines() if line.strip()]
    if lines and lines[-1] == "None":
        lines = lines[:-1]
    return lines


def test_print_non_empty_list_in_order():
    head = _make_linked_list([3, 7, 2])
    output = _capture_print_output(head)
    values = _extract_printed_values(output)
    _assert_equal(
        values,
        ["3", "7", "2"],
        "print_list(head) should print values in order for a non-empty list.",
    )


def test_print_preserves_duplicates_in_output():
    head = _make_linked_list([4, 4, 1])
    output = _capture_print_output(head)
    values = _extract_printed_values(output)
    _assert_equal(
        values,
        ["4", "4", "1"],
        "print_list(head) should include duplicate values in the output.",
    )


def test_print_empty_list_outputs_nothing_or_none():
    output = _capture_print_output(None)
    values = _extract_printed_values(output)
    _assert_equal(
        values,
        [],
        "print_list(None) should print either nothing or a None-only representation.",
    )


if __name__ == "__main__":
    TEST_CASES = [
        ("prints non-empty list in order", test_print_non_empty_list_in_order),
        ("prints duplicates correctly", test_print_preserves_duplicates_in_output),
        (
            "empty list output is acceptable",
            test_print_empty_list_outputs_nothing_or_none,
        ),
    ]
    _run_all_tests(TEST_CASES)
