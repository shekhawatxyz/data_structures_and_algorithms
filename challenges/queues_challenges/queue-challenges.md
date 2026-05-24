# Queue Challenges

_Problems: 18/18._

A graduated sequence of programming challenges for building deep fluency with queues and their variants.

**Language:** Python.

**Constraint:** every problem is solvable with queues alone (and, where explicitly allowed, stacks or recursion). No trees, graphs, hash tables, heaps, or other data structures unless noted.

**Spirit:** when a problem says "the intended technique uses a queue," it means: don't bypass the data structure with a one-liner. The point is to grapple with the queue as a tool, not to produce a correct answer by any means.

---

## [x] Level 1 — Build a queue

- [x] **1a — Queue with a list** — Status:

Implement a `ListQueue` class backed by a plain Python list:

- `enqueue(x)` — add `x` to the back
- `dequeue()` — remove and return the front; raise on empty
- `peek()` — return the front without removing; raise on empty
- `is_empty() -> bool`
- `__len__() -> int`

You don't need to worry about the asymptotic cost of `dequeue`.

```
q = ListQueue()
q.enqueue(1); q.enqueue(2); q.enqueue(3)
q.dequeue()    # 1
q.peek()       # 2
len(q)         # 2
```

- [x] **1b — Queue with a circular buffer** — Status:

Implement a `RingQueue` class with the same operations as `ListQueue`, but:

- Backed by a fixed-capacity Python list, allocated once and never resized.
- Every operation runs in O(1).
- `enqueue` raises if the queue is full.

```
q = RingQueue(capacity=3)
q.enqueue(1); q.enqueue(2); q.enqueue(3)
q.dequeue()        # 1
q.enqueue(4)       # OK — wraps
q.dequeue()        # 2
```

---

## [x] Level 2 — Drive a queue

- [x] **2a — Command stream** — Status:

```python
def simulate(commands: list[str]) -> list:
    ...
```

`commands` is a list, each element being one of:
- `"E x"` — enqueue the integer `x`
- `"D"` — dequeue
- `"P"` — peek

Simulate the commands on an initially empty queue. Return the list of results from each `D` and `P`, in order. You may assume the input never tries to dequeue or peek an empty queue.

```
simulate(["E 1", "E 2", "P", "D", "P"])  # [1, 1, 2]
```

- [x] **2b — Round-robin elimination** — Status:

```python
def eliminate(names: list[str], k: int) -> str:
    ...
```

People stand in a circle in the given order. Starting from the first, you skip `k - 1` people and eliminate the `k`-th. You then continue from the next person, skipping `k - 1` and eliminating the next `k`-th. Repeat until one person remains. Return that person.

```
eliminate(["A", "B", "C", "D", "E"], 3)  # "D"
eliminate(["A", "B", "C"], 1)            # "C"
```

---

## [x] Level 3 — Queue as a generator

- [x] **3a — First n binary numbers** — Status:

```python
def binary_numbers(n: int) -> list[str]:
    ...
```

Return the binary representations (as strings) of the integers `1, 2, ..., n`, in order.

```
binary_numbers(5)   # ["1", "10", "11", "100", "101"]
```

The intended technique uses a queue. Don't just call `bin(i)` in a loop.

- [x] **3b — First non-repeating character in a stream** — Status:

```python
def first_unique_stream(stream: str) -> list[str]:
    ...
```

After reading each character of `stream` in order, return the earliest character (among all characters seen so far) that has appeared exactly once. If no such character exists at that point, return `"#"` for that step.

The output list has one entry per character in `stream`. Assume the alphabet is fixed and small (lowercase ASCII), so a length-26 array of counts is fair game; no general hash maps.

```
first_unique_stream("aabc")    # ["a", "#", "b", "b"]
first_unique_stream("aabbcc")  # ["a", "#", "b", "#", "c", "#"]
```

---

## [x] Level 4 — Queue manipulations

For all of Level 4, assume access to a queue with the operations from 1a/1b. You may use the call stack (recursion) freely. Where stated, you may also use a single auxiliary stack or queue.

- [x] **4a — Reverse a queue** — Status:

```python
def reverse(q) -> None:
    ...
```

Reverse `q` in place using only queue operations and recursion.

```
q: front [1, 2, 3, 4] back
reverse(q)
q: front [4, 3, 2, 1] back
```

- [x] **4b — Reverse the first k elements** — Status:

```python
def reverse_first_k(q, k: int) -> None:
    ...
```

Reverse the first `k` elements of `q` in place, leaving the remaining elements in their original order. You may use one auxiliary stack. Assume `0 <= k <= len(q)`.

```
q: front [1, 2, 3, 4, 5, 6] back, k = 3
reverse_first_k(q, 3)
q: front [3, 2, 1, 4, 5, 6] back
```

- [x] **4c — Interleave the halves** — Status:

```python
def interleave(q) -> None:
    ...
```

Given a queue with an even number of elements, interleave its first half with its second half. You may use one auxiliary queue or stack.

```
q: front [1, 2, 3, 4, 5, 6] back
interleave(q)
q: front [1, 4, 2, 5, 3, 6] back
```

---

## [x] Level 5 — Cross-structure implementation

You may treat a stack as a black box with `push`, `pop`, `top`, `is_empty`, `__len__`.

- [x] **5a — Stack using a queue** — Status:

Implement a `QueueStack` class with the operations of a stack:

- `push(x)`, `pop()`, `top()`, `is_empty()`, `__len__()`

Internally use exactly one queue (with the operations from 1a/1b). One of `push` and `pop` will be O(n); choose which.

- [x] **5b — Queue using two stacks** — Status:

Implement a `StackQueue` class with the operations of `ListQueue` (1a), but internally backed by exactly two stacks. Each `enqueue`, `dequeue`, and `peek` should run in O(1) **amortized** time.

---

## [x] Level 6 — Deque

- [x] **6a — Build a deque** — Status:

Implement a `Deque` class backed by a fixed-capacity circular buffer:

- `push_front(x)`, `push_back(x)` — raise if full
- `pop_front()`, `pop_back()` — raise if empty; return the removed value
- `peek_front()`, `peek_back()` — raise if empty
- `is_empty()`, `__len__()`

All operations O(1).

---

## [x] Level 7 — Sliding window primer

- [x] **7a — Moving average** — Status:

Implement a `MovingAverage` class:

- `MovingAverage(k: int)` — fixed window size `k >= 1`
- `next(x: float) -> float` — admit `x` into the window and return the average of the values currently in the window

Until `k` values have been seen, the window contains all values seen so far.

```
ma = MovingAverage(3)
ma.next(1)    # 1.0
ma.next(10)   # 5.5
ma.next(3)    # 4.666...
ma.next(5)    # 6.0     (window is now [10, 3, 5])
```

---

## [x] Level 8 — Monotonic deque

- [x] **8a — First negative in each window** — Status:

```python
def first_negative_each_window(values: list[int], k: int) -> list[int]:
    ...
```

For each contiguous window of size `k` in `values`, return the first negative value in that window — that is, the negative value with the smallest index inside the window. If the window contains no negative value, output `0` for that window.

```
first_negative_each_window([12, -1, -7, 8, -15, 30, 16, 28], 3)
# [-1, -1, -7, -15, -15, 0]
```

- [x] **8b — Sliding window maximum** — Status:

```python
def sliding_max(values: list[int], k: int) -> list[int]:
    ...
```

For each contiguous window of size `k`, return the maximum value in the window. The amortized cost per window should be O(1).

```
sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3)
# [3, 3, 5, 5, 6, 7]
```

---

## [x] Level 9 — Hairy applications

- [x] **9a — Queue with getMax in O(1) amortized** — Status:

Implement a `MaxQueue` class:

- `enqueue(x)`
- `dequeue()` — return the removed value; raise on empty
- `get_max()` — return the maximum element currently in the queue; raise on empty

All three operations should run in O(1) amortized time.

```
q = MaxQueue()
q.enqueue(3); q.enqueue(1); q.enqueue(5)
q.get_max()        # 5
q.dequeue()        # 3
q.get_max()        # 5
q.dequeue()        # 1
q.get_max()        # 5
```

- [x] **9b — Max sum subarray of length at most k** — Status:

```python
def max_subarray_at_most_k(values: list[int], k: int) -> int:
    ...
```

Return the maximum sum over all non-empty contiguous subarrays of `values` whose length is at most `k`. Values may be negative. Total runtime should be O(n).

```
max_subarray_at_most_k([1, -2, 3, -1, 2], 2)   # 3      (the subarray [3])
max_subarray_at_most_k([1, -2, 3, -1, 2], 3)   # 4      ([3, -1, 2])
max_subarray_at_most_k([-3, -1, -4, -1], 2)    # -1     ([-1])
```

- [x] **9c — Shortest subarray with sum at least K** — Status:

```python
def shortest_subarray(values: list[int], k: int) -> int:
    ...
```

Return the length of the shortest contiguous subarray of `values` whose sum is at least `k`. If no such subarray exists, return `-1`. Values may be negative. Total runtime should be O(n).

```
shortest_subarray([1], 1)                       # 1
shortest_subarray([1, 2], 4)                    # -1
shortest_subarray([2, -1, 2], 3)                # 3
shortest_subarray([84, -37, 32, 40, 95], 167)   # 3
```
