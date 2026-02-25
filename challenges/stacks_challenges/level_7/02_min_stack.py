# Level 7b - MinStack in O(1)
# Implement MinStack with push, pop, peek, get_min all in O(1).
# You may use one auxiliary stack and optimize its space usage.

class MinStack:
    def __init__(self):
        raise NotImplementedError('Implement MinStack.__init__.')

    def push(self, item):
        raise NotImplementedError('Implement MinStack.push(item).')

    def pop(self):
        raise NotImplementedError('Implement MinStack.pop().')

    def peek(self):
        raise NotImplementedError('Implement MinStack.peek().')

    def get_min(self):
        raise NotImplementedError('Implement MinStack.get_min().')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

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


def test_01_pedagogy_get_min_progression_while_pushing():
    stack = MinStack()
    sequence = [5, 2, 7, 1, 1]
    expected_mins = [5, 2, 2, 1, 1]

    for index, (value, expected_min) in enumerate(zip(sequence, expected_mins), start=1):
        stack.push(value)
        _assert_equal(
            stack.get_min(),
            expected_min,
            f'After push #{index} of value {value}, get_min() should be {expected_min}.',
        )


def test_02_pedagogy_lifo_and_min_update_while_popping():
    stack = MinStack()
    for value in [3, 2, 2, 4]:
        stack.push(value)

    _assert_equal(stack.pop(), 4, 'First pop should remove top value 4.')
    _assert_equal(stack.get_min(), 2, 'Min should remain 2 after popping non-min value 4.')
    _assert_equal(stack.pop(), 2, 'Second pop should remove top-most minimum 2.')
    _assert_equal(stack.get_min(), 2, 'Min should remain 2 due to duplicate minimum.')
    _assert_equal(stack.pop(), 2, 'Third pop removes second minimum.')
    _assert_equal(stack.get_min(), 3, 'Min should update to 3 after removing all minimum duplicates.')


def test_03_boundaries_empty_stack_operations_raise():
    stack = MinStack()
    _assert_raises(lambda: stack.pop(), 'pop() on empty MinStack should raise.')
    _assert_raises(lambda: stack.peek(), 'peek() on empty MinStack should raise.')
    _assert_raises(lambda: stack.get_min(), 'get_min() on empty MinStack should raise.')


def test_04_boundaries_duplicate_min_values_are_tracked_correctly():
    stack = MinStack()
    for value in [1, 1, 1]:
        stack.push(value)

    _assert_equal(stack.get_min(), 1, 'Min should be 1 after pushing duplicate minima.')
    stack.pop()
    _assert_equal(stack.get_min(), 1, 'Min should remain 1 after popping one minimum.')
    stack.pop()
    _assert_equal(stack.get_min(), 1, 'Min should remain 1 until all minimum duplicates are removed.')


def test_05_interactions_negative_and_positive_mix():
    stack = MinStack()
    for value in [10, -3, 5, -7, 0]:
        stack.push(value)

    _assert_equal(stack.get_min(), -7, 'Min should become -7 after pushing -7.')
    _assert_equal(stack.pop(), 0, 'Top should pop in LIFO order for mixed sign values.')
    _assert_equal(stack.get_min(), -7, 'Min should remain -7 after popping non-min value 0.')
    _assert_equal(stack.pop(), -7, 'Popping -7 should remove current minimum.')
    _assert_equal(stack.get_min(), -3, 'Min should update to next minimum -3 after removing -7.')


def test_06_interactions_interleaved_push_pop_peek_get_min():
    stack = MinStack()
    stack.push(4)
    _assert_equal(stack.peek(), 4, 'peek should show top 4 after first push.')
    _assert_equal(stack.get_min(), 4, 'min should be 4 after first push.')

    stack.push(6)
    _assert_equal(stack.peek(), 6, 'peek should update to 6 after pushing 6.')
    _assert_equal(stack.get_min(), 4, 'min should remain 4 after pushing larger value 6.')

    stack.push(1)
    _assert_equal(stack.get_min(), 1, 'min should update to 1 after pushing 1.')
    _assert_equal(stack.pop(), 1, 'pop should remove top 1 first.')
    _assert_equal(stack.peek(), 6, 'peek should revert to 6 after popping 1.')
    _assert_equal(stack.get_min(), 4, 'min should revert to 4 after popping 1.')


if __name__ == '__main__':
    TEST_CASES = [
        ('pedagogy: min progression on push', test_01_pedagogy_get_min_progression_while_pushing),
        ('pedagogy: lifo + min updates on pop', test_02_pedagogy_lifo_and_min_update_while_popping),
        ('boundaries: empty operations raise', test_03_boundaries_empty_stack_operations_raise),
        ('boundaries: duplicate minima', test_04_boundaries_duplicate_min_values_are_tracked_correctly),
        ('interactions: mixed sign values', test_05_interactions_negative_and_positive_mix),
        ('interactions: interleaved ops', test_06_interactions_interleaved_push_pop_peek_get_min),
    ]
    _run_all_tests(TEST_CASES)
