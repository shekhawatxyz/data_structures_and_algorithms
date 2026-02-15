# Level 5.4 - is_palindrome(head)
# Write is_palindrome(head) that returns True if the linked list
# reads the same forwards and backwards, else False.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def is_palindrome(head):
    raise NotImplementedError('Implement is_palindrome(head).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
                'Linked list traversal exceeded a safety limit. '
                'Your list might contain an unexpected cycle.'
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
                'Node-id traversal exceeded a safety limit. '
                'Your list might contain an unexpected cycle.'
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

def test_is_palindrome_true_for_even_length_palindrome():
    head = _make_linked_list([1, 2, 2, 1])
    _assert_equal(is_palindrome(head), True, 'Even-length palindrome should return True.')


def test_is_palindrome_true_for_odd_length_palindrome():
    head = _make_linked_list([1, 2, 3, 2, 1])
    _assert_equal(is_palindrome(head), True, 'Odd-length palindrome should return True.')


def test_is_palindrome_false_for_non_palindrome():
    head = _make_linked_list([1, 2, 3])
    _assert_equal(is_palindrome(head), False, 'Non-palindrome list should return False.')


def test_is_palindrome_handles_empty_and_single_node_lists():
    _assert_equal(is_palindrome(None), True, 'Empty list should be considered a palindrome.')
    single = _make_linked_list([9])
    _assert_equal(is_palindrome(single), True, 'Single-node list should be a palindrome.')


if __name__ == '__main__':
    TEST_CASES = [
        ('even palindrome is True', test_is_palindrome_true_for_even_length_palindrome),
        ('odd palindrome is True', test_is_palindrome_true_for_odd_length_palindrome),
        ('non-palindrome is False', test_is_palindrome_false_for_non_palindrome),
        ('empty and single are palindromes', test_is_palindrome_handles_empty_and_single_node_lists),
    ]
    _run_all_tests(TEST_CASES)
