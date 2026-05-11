# Level 8.3 - LRUCache(capacity)
# Write an LRUCache class with O(1) get/put using a dictionary plus
# a doubly linked list. get misses return -1.

# Complete Exact Problem Statement (from doubly-linked-list-challenges.md):
# **8.3** Write a simple **LRU Cache** backed by a doubly linked list and a Python dictionary:
# ```python
# class LRUCache:
#     def __init__(self, capacity): ...
#     def get(self, key): ...
#     def put(self, key, value): ...
# ```
# - `get` returns the value if present (and marks it as recently used), or -1 if not.
# - `put` inserts or updates. If the cache is at capacity, evict the least recently used item.
# - Both operations must be O(1).
#
# This is the classic application of doubly linked lists: the dict gives O(1) lookup, and the doubly linked list gives O(1) insertion, deletion, and move-to-front — together they give you an O(1) LRU cache.
class Node:
    def __init__(self, key=None, value=None, prev=None, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self, node):
        recent = self.head.next
        self.head.next = node
        node.next = recent
        node.prev = self.head
        recent.prev = node

    def _remove(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before

    def _move_to_front(self, node):
        self._remove(node)
        self._add_to_front(node)

    def get(self, key):
        if key not in self.cache:
            return -1
        current = self.cache[key]
        self._move_to_front(current)
        return current.value

    def put(self, key, value):
        if key not in self.cache:
            current = Node(key, value)
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                del self.cache[lru.key]
                self._remove(lru)
            self.cache[key] = current
            self._add_to_front(current)
        else:
            current = self.cache[key]
            current.value = value
            self._move_to_front(current)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_lru_cache_basic_get_put_behavior():
    cache = LRUCache(2)
    cache.put(1, 10)
    _assert_equal(cache.get(1), 10, "get(1) should return value after put(1, 10).")
    _assert_equal(cache.get(2), -1, "Missing key should return -1.")


def test_lru_cache_evicts_least_recently_used_item():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    _assert_equal(cache.get(1), 1, "get(1) should mark key 1 as recently used.")
    cache.put(3, 3)  # should evict key 2

    _assert_equal(cache.get(2), -1, "Key 2 should be evicted as least recently used.")
    _assert_equal(cache.get(1), 1, "Key 1 should still exist after eviction of key 2.")
    _assert_equal(cache.get(3), 3, "Key 3 should exist after insertion.")


def test_lru_cache_put_updates_existing_key_without_growing_capacity():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)  # update existing and make key 1 most recent
    cache.put(3, 3)  # should evict key 2

    _assert_equal(
        cache.get(1), 10, "Updated key should keep latest value and stay in cache."
    )
    _assert_equal(
        cache.get(2),
        -1,
        "Least recently used key should be evicted after capacity overflow.",
    )
    _assert_equal(cache.get(3), 3, "Newest key should be present.")


def test_lru_cache_capacity_one_behavior():
    cache = LRUCache(1)
    cache.put(1, 100)
    _assert_equal(
        cache.get(1), 100, "Single-capacity cache should return stored value."
    )

    cache.put(2, 200)
    _assert_equal(
        cache.get(1), -1, "In capacity-1 cache, inserting new key should evict old key."
    )
    _assert_equal(cache.get(2), 200, "Newest key should remain in capacity-1 cache.")


if __name__ == "__main__":
    TEST_CASES = [
        ("basic get/put behavior", test_lru_cache_basic_get_put_behavior),
        (
            "evicts least recently used key",
            test_lru_cache_evicts_least_recently_used_item,
        ),
        (
            "put updates existing key",
            test_lru_cache_put_updates_existing_key_without_growing_capacity,
        ),
        ("capacity=1 behavior", test_lru_cache_capacity_one_behavior),
    ]
    _run_all_tests(TEST_CASES)
