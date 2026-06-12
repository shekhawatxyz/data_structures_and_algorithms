# Doubly Linked Lists: Graduated Programming Challenges

_Problems: 33._

Assume throughout that you are working with this node definition (or your own equivalent):

```python
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
```

The key difference from singly linked lists: every node now points both forward and backward. This means *every* insertion and deletion must update pointers in both directions, which is more bookkeeping — but it also means you can traverse backwards and delete a node given only a reference to it, which you couldn't before.

---

## Level 1: Getting Comfortable with the Structure

Same spirit as the singly linked list Level 1, but now you must keep `prev` pointers consistent from the start.

- [x] **1.1** — Status:

Write `build(values)` — takes a Python list and returns the head of a doubly linked list. Make sure every node's `prev` pointer is correctly set.

- [x] **1.2** — Status:

Write `to_list(head)` — returns a Python list of values by traversing forward.

- [x] **1.3** — Status:

Write `to_list_backward(head)` — given the *head*, first find the tail, then traverse backward to produce the list in reverse. (This verifies your `prev` pointers are correct: `to_list_backward(head)` should equal `to_list(head)[::-1]`.)

- [x] **1.4** — Status:

Write `verify(head)` — traverses the entire list and checks that for every node `n`, if `n.next` is not `None` then `n.next.prev is n`, and if `n.prev` is not `None` then `n.prev.next is n`. Returns `True` if all links are consistent, `False` otherwise. Use this to test everything you write from here on.

---

## Level 2: Insertion

Each of these requires updating two pointers per affected node instead of one. Get in the habit of thinking: "which pointers need to change, and in what order?"

- [x] **2.1** — Status:

Write `insert_front(head, value)` — returns the new head.

- [x] **2.2** — Status:

Write `insert_back(head, value)` — returns the head. (You'll need to find the tail first, or think about whether to maintain one.)

- [x] **2.3** — Status:

Write `insert_at(head, index, value)` — inserts at position `index` (0-indexed). Returns the new head.

- [x] **2.4** — Status:

Write `insert_after_node(node, value)` — given a direct reference to a node (not the head, not an index), insert a new node immediately after it. Notice that you don't need the head at all. This is something you *couldn't* do as cleanly with singly linked lists.

- [x] **2.5** — Status:

Write `insert_before_node(node, value)` — same, but insert before the given node. Again, no head needed. Think about why this is trivial with a doubly linked list and awkward with a singly linked one.

---

## Level 3: Deletion

Deletion is where the doubly linked list really shines: given a reference to a node, you can remove it in O(1) without needing to find its predecessor.

- [x] **3.1** — Status:

Write `delete_node(head, node)` — given a reference to a node, remove it. Returns the (possibly new) head.

- [x] **3.2** — Status:

Write `delete_first(head, value)` — removes the first node with the given value. Returns the new head.

- [x] **3.3** — Status:

Write `delete_all(head, value)` — removes every node with the given value.

- [x] **3.4** — Status:

Write `delete_range(head, start, end)` — removes all nodes from index `start` to index `end` (inclusive). Think about how many pointer updates you actually need, regardless of how many nodes you're removing.

---

## Level 4: Exploiting Bidirectionality

These problems are either easier or only possible because you can go backwards.

- [x] **4.1** — Status:

Write `find_tail(head)` and `find_head(tail)`. Simple, but clarify for yourself that either end of a doubly linked list gives you access to the whole structure.

- [x] **4.2** — Status:

Write `pairs_with_sum(head, target)` — given a *sorted* doubly linked list, find all pairs of nodes whose values sum to `target`. Do this in O(n) time using the two-pointer technique: one pointer starts at the head, the other at the tail, and they walk inward. (With a singly linked list, the "start at the tail" part would be a problem.)

- [x] **4.3** — Status:

Write `nth_from_end(head, n)` — return the value of the nth node from the end. You did this with singly linked lists using a two-pointer trick. Here you have a simpler option. Implement both ways and compare.

- [x] **4.4** — Status:

Write `reverse_traversal(head, start, end)` — given indices `start` and `end`, print the values from index `end` back to index `start`. Do this without building any auxiliary data structure.

---

## Level 5: Structural Transformation

Same spirit as the singly linked list versions, but now every pointer swap has a `prev` counterpart to maintain.

- [x] **5.1** — Status:

Write `reverse(head)` — reverse the doubly linked list iteratively. (Hint: what if you just swap `prev` and `next` for every node?)

- [x] **5.2** — Status:

Write `swap_nodes(head, val1, val2)` — swap the two nodes containing `val1` and `val2`. Do not just swap their data fields — actually re-link the nodes. This is pointer surgery at its most demanding: you must handle adjacent nodes, head/tail nodes, and keep all `prev`/`next` links consistent. (Draw this out before coding.)

- [x] **5.3** — Status:

Write `partition(head, x)` — rearrange so all values less than `x` come before all values ≥ `x`, preserving relative order within each group. Return the new head.

- [x] **5.4** — Status:

Write `move_node_to_front(head, node)` — given a reference to a node anywhere in the list, unlink it and re-link it at the front. Return the new head. (This is a building block for LRU-style operations.)

---

## Level 6: Multi-List Operations

- [x] **6.1** — Status:

Write `merge_sorted(head1, head2)` — merge two sorted doubly linked lists into one sorted doubly linked list by re-linking existing nodes. All `prev` pointers must be correct in the result.

- [x] **6.2** — Status:

Write `interleave(head1, head2)` — weave two lists together, alternating nodes. All `prev` and `next` pointers must be correct.

- [x] **6.3** — Status:

Write `split_at(head, index)` — split a doubly linked list into two independent doubly linked lists at the given index. Return both heads. Make sure the `prev` of the second list's head is `None` and the `next` of the first list's tail is `None`.

- [x] **6.4** — Status:

Write `concatenate(head1, head2)` — join two doubly linked lists end to end. Return the head of the combined list.

---

## Level 7: Complex Manipulation

- [x] **7.1** — Status:

Write `reverse_between(head, left, right)` — reverse only the sublist from position `left` to `right` (1-indexed). All `prev` and `next` pointers in the entire list must remain consistent. This is the doubly linked version of the singly linked list challenge, and it's harder because there are more links to get right at the boundaries.

- [x] **7.2** — Status:

Write `sort_biotonic(head)` — a *bitonic* doubly linked list first increases and then decreases (e.g., `1 -> 3 -> 7 -> 5 -> 2`). Sort it in O(n) time. (Hint: think about splitting and merging.)

- [x] **7.3** — Status:

Write `flatten(head)` — each node now has an additional `child` attribute (default `None`) that may point to the head of another doubly linked list. Flatten the entire structure into a single-level doubly linked list. When a node has a child list, insert the child list immediately after that node (before the node's original next). Process all children recursively/iteratively.

Use this extended node:
```python
class Node:
    def __init__(self, data, prev=None, next=None, child=None):
        self.data = data
        self.prev = prev
        self.next = next
        self.child = child
```

- [x] **7.4** — Status:

Write `remove_duplicates_unsorted(head)` — remove duplicate values from an unsorted doubly linked list, keeping the first occurrence. The `prev` pointer makes the unlinking easier than in the singly linked version — notice the difference.

---

## Level 8: The Hairy Stuff

- [x] **8.1** — Status:

Write `reverse_in_groups(head, k)` — reverse in groups of `k`, maintaining all `prev` pointers. The boundary stitching between groups is the hard part: each reversed group's new tail must connect forward to the next group's new head, and all `prev` links must point back correctly.

- [x] **8.2** — Status:

Write `merge_sort(head)` — sort a doubly linked list using merge sort in O(n log n) time. You've written `find_middle`, `split`, and `merge_sorted` in earlier problems. Now combine them, keeping `prev` pointers consistent throughout.

- [x] **8.3** — Status:

Write a simple **LRU Cache** backed by a doubly linked list and a Python dictionary:
```python
class LRUCache:
    def __init__(self, capacity): ...
    def get(self, key): ...
    def put(self, key, value): ...
```
- `get` returns the value if present (and marks it as recently used), or -1 if not.
- `put` inserts or updates. If the cache is at capacity, evict the least recently used item.
- Both operations must be O(1).

This is the classic application of doubly linked lists: the dict gives O(1) lookup, and the doubly linked list gives O(1) insertion, deletion, and move-to-front — together they give you an O(1) LRU cache.

- [x] **8.4** — Status:

Write `clone_with_random(head)` — each node has an additional `random` attribute that points to any node in the list (or `None`). Deep-copy the entire list, including both `next`/`prev` links and `random` pointers. The cloned nodes must point to their cloned counterparts, not to the original nodes.

Use this extended node:
```python
class Node:
    def __init__(self, data, prev=None, next=None, random=None):
        self.data = data
        self.prev = prev
        self.next = next
        self.random = random
```

---

## General Advice

- **Always run `verify(head)` from 1.4** after every operation. A single forgotten `prev` update will silently corrupt your list and cause bewildering bugs later.
- **Draw the before-and-after** for any pointer surgery. Doubly linked nodes have four relevant pointers at any insertion/deletion site (the node's own `prev` and `next`, plus the neighboring nodes' links back). Getting the order of updates wrong can lose references.
- **Compare with singly linked lists** as you go. Some things are harder (more pointers to maintain), some are easier (O(1) delete given a node, backward traversal). Building an intuition for this tradeoff is part of the point.
