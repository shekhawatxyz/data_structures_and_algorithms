# Level 8.4 - clone_with_random(head)
# Write clone_with_random(head) that deep-copies a doubly linked list with
# next/prev/random pointers so clone pointers only target cloned nodes.

class Node:
    def __init__(self, data, prev=None, next=None, random=None):
        self.data = data
        self.prev = prev
        self.next = next
        self.random = random

def clone_with_random(head):
    raise NotImplementedError('Implement clone_with_random(head).')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

def _make_doubly_linked_list(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            node.prev = tail
            tail = node
    return head


def _head_from_any(node):
    current = node
    while current is not None and current.prev is not None:
        current = current.prev
    return current


def _tail_from_head(head):
    current = head
    while current is not None and current.next is not None:
        current = current.next
    return current


def _to_list_forward(head, max_nodes=2000):
    values = []
    current = head
    steps = 0

    while current is not None:
        values.append(current.data)
        current = current.next
        steps += 1
        if steps > max_nodes:
            raise AssertionError(
                'Forward traversal exceeded safety limit; possible cycle or broken links.'
            )

    return values


def _to_list_backward(head, max_nodes=2000):
    values = []
    current = _tail_from_head(head)
    steps = 0

    while current is not None:
        values.append(current.data)
        current = current.prev
        steps += 1
        if steps > max_nodes:
            raise AssertionError(
                'Backward traversal exceeded safety limit; possible cycle or broken links.'
            )

    return values


def _verify_bidirectional_links(head, max_nodes=2000):
    if head is None:
        return True

    if head.prev is not None:
        return False

    prev_node = None
    current = head
    steps = 0

    while current is not None:
        if current.prev is not prev_node:
            return False
        if prev_node is not None and prev_node.next is not current:
            return False

        prev_node = current
        current = current.next
        steps += 1

        if steps > max_nodes:
            return False

    return True


def _list_nodes(head, max_nodes=2000):
    nodes = []
    current = head
    steps = 0

    while current is not None:
        nodes.append(current)
        current = current.next
        steps += 1
        if steps > max_nodes:
            raise AssertionError('Node traversal exceeded safety limit; possible cycle.')

    return nodes


def _node_ids(head, max_nodes=2000):
    return [id(node) for node in _list_nodes(head, max_nodes=max_nodes)]


def _find_first_node(head, value):
    current = head
    while current is not None:
        if current.data == value:
            return current
        current = current.next
    return None


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

def _build_random_list(values, random_targets):
    if not values:
        return None, []

    nodes = [Node(v) for v in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]

    for i, target_index in random_targets.items():
        nodes[i].random = None if target_index is None else nodes[target_index]

    return nodes[0], nodes


def test_clone_with_random_empty_input_returns_none():
    _assert_true(clone_with_random(None) is None, 'clone_with_random(None) should return None.')


def test_clone_with_random_copies_values_and_structure():
    head, original_nodes = _build_random_list(
        [1, 2, 3],
        {
            0: 2,   # 1.random -> 3
            1: 0,   # 2.random -> 1
            2: None,
        },
    )

    cloned_head = clone_with_random(head)
    cloned_nodes = _list_nodes(cloned_head)

    _assert_equal([n.data for n in cloned_nodes], [1, 2, 3], 'Cloned list values should match original values.')
    _assert_true(_verify_bidirectional_links(cloned_head), 'Cloned next/prev links should be consistent.')

    for original, cloned in zip(original_nodes, cloned_nodes):
        _assert_true(original is not cloned, 'Each cloned node must be a distinct object from original node.')

    original_index = {node: i for i, node in enumerate(original_nodes)}
    cloned_index = {node: i for i, node in enumerate(cloned_nodes)}

    for i, cloned_node in enumerate(cloned_nodes):
        original_target = original_nodes[i].random
        cloned_target = cloned_node.random

        if original_target is None:
            _assert_true(cloned_target is None, 'Cloned random pointer should be None when original random is None.')
        else:
            expected_index = original_index[original_target]
            _assert_true(
                cloned_target in cloned_index,
                'Cloned random pointers must point to cloned nodes, not original nodes.',
            )
            _assert_equal(
                cloned_index[cloned_target],
                expected_index,
                'Cloned random pointer should point to clone of the original random target.',
            )
            _assert_true(
                cloned_target is not original_target,
                'Cloned random target must not reference the original node.',
            )


def test_clone_with_random_is_deep_copy_independent_of_original_mutations():
    head, original_nodes = _build_random_list([5, 6], {0: 1, 1: 0})
    cloned_head = clone_with_random(head)
    cloned_nodes = _list_nodes(cloned_head)

    original_nodes[0].data = 999
    original_nodes[0].random = None
    original_nodes[0].next = None

    _assert_equal([n.data for n in cloned_nodes], [5, 6], 'Clone data should not change when original data mutates.')
    _assert_true(cloned_nodes[0].random is cloned_nodes[1], 'Clone random links should remain independent.')


def test_clone_with_random_single_node_self_random():
    head = Node(42)
    head.random = head

    cloned_head = clone_with_random(head)
    _assert_true(cloned_head is not head, 'Cloned single node should be a different object.')
    _assert_equal(cloned_head.data, 42, 'Cloned single node should copy data value.')
    _assert_true(cloned_head.random is cloned_head, 'Self-random should point to cloned self, not original.')


if __name__ == '__main__':
    TEST_CASES = [
        ('empty input returns None', test_clone_with_random_empty_input_returns_none),
        ('copies values/structure/random mapping', test_clone_with_random_copies_values_and_structure),
        ('deep copy independence', test_clone_with_random_is_deep_copy_independent_of_original_mutations),
        ('single-node self-random clone', test_clone_with_random_single_node_self_random),
    ]
    _run_all_tests(TEST_CASES)
