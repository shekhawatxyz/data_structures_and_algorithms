# Doubly Linked Lists: Graduated Programming Challenges

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

**1.1** Write `build(values)` — takes a Python list and returns the head of a doubly linked list. Make sure every node's `prev` pointer is correctly set.

**1.2** Write `to_list(head)` — returns a Python list of values by traversing forward.

**1.3** Write `to_list_backward(head)` — given the *head*, first find the tail, then traverse backward to produce the list in reverse. (This verifies your `prev` pointers are correct: `to_list_backward(head)` should equal `to_list(head)[::-1]`.)

**1.4** Write `verify(head)` — traverses the entire list and checks that for every node `n`, if `n.next` is not `None` then `n.next.prev is n`, and if `n.prev` is not `None` then `n.prev.next is n`. Returns `True` if all links are consistent, `False` otherwise. Use this to test everything you write from here on.

---

## Level 2: Insertion

Each of these requires updating two pointers per affected node instead of one. Get in the habit of thinking: "which pointers need to change, and in what order?"

**2.1** Write `insert_front(head, value)` — returns the new head.

**2.2** Write `insert_back(head, value)` — returns the head. (You'll need to find the tail first, or think about whether to maintain one.)

**2.3** Write `insert_at(head, index, value)` — inserts at position `index` (0-indexed). Returns the new head.

**2.4** Write `insert_after_node(node, value)` — given a direct reference to a node (not the head, not an index), insert a new node immediately after it. Notice that you don't need the head at all. This is something you *couldn't* do as cleanly with singly linked lists.

**2.5** Write `insert_before_node(node, value)` — same, but insert before the given node. Again, no head needed. Think about why this is trivial with a doubly linked list and awkward with a singly linked one.

---

## Level 3: Deletion

Deletion is where the doubly linked list really shines: given a reference to a node, you can remove it in O(1) without needing to find its predecessor.

**3.1** Write `delete_node(head, node)` — given a reference to a node, remove it. Returns the (possibly new) head.

**3.2** Write `delete_first(head, value)` — removes the first node with the given value. Returns the new head.

**3.3** Write `delete_all(head, value)` — removes every node with the given value.

**3.4** Write `delete_range(head, start, end)` — removes all nodes from index `start` to index `end` (inclusive). Think about how many pointer updates you actually need, regardless of how many nodes you're removing.

---

## Level 4: Exploiting Bidirectionality

These problems are either easier or only possible because you can go backwards.

**4.1** Write `find_tail(head)` and `find_head(tail)`. Simple, but clarify for yourself that either end of a doubly linked list gives you access to the whole structure.

**4.2** Write `pairs_with_sum(head, target)` — given a *sorted* doubly linked list, find all pairs of nodes whose values sum to `target`. Do this in O(n) time using the two-pointer technique: one pointer starts at the head, the other at the tail, and they walk inward. (With a singly linked list, the "start at the tail" part would be a problem.)

**4.3** Write `nth_from_end(head, n)` — return the value of the nth node from the end. You did this with singly linked lists using a two-pointer trick. Here you have a simpler option. Implement both ways and compare.

**4.4** Write `reverse_traversal(head, start, end)` — given indices `start` and `end`, print the values from index `end` back to index `start`. Do this without building any auxiliary data structure.

---

## Level 5: Structural Transformation

Same spirit as the singly linked list versions, but now every pointer swap has a `prev` counterpart to maintain.

**5.1** Write `reverse(head)` — reverse the doubly linked list iteratively. (Hint: what if you just swap `prev` and `next` for every node?)

**5.2** Write `swap_nodes(head, val1, val2)` — swap the two nodes containing `val1` and `val2`. Do not just swap their data fields — actually re-link the nodes. This is pointer surgery at its most demanding: you must handle adjacent nodes, head/tail nodes, and keep all `prev`/`next` links consistent. (Draw this out before coding.)

**5.3** Write `partition(head, x)` — rearrange so all values less than `x` come before all values ≥ `x`, preserving relative order within each group. Return the new head.

**5.4** Write `move_node_to_front(head, node)` — given a reference to a node anywhere in the list, unlink it and re-link it at the front. Return the new head. (This is a building block for LRU-style operations.)

---

## Level 6: Multi-List Operations

**6.1** Write `merge_sorted(head1, head2)` — merge two sorted doubly linked lists into one sorted doubly linked list by re-linking existing nodes. All `prev` pointers must be correct in the result.

**6.2** Write `interleave(head1, head2)` — weave two lists together, alternating nodes. All `prev` and `next` pointers must be correct.

**6.3** Write `split_at(head, index)` — split a doubly linked list into two independent doubly linked lists at the given index. Return both heads. Make sure the `prev` of the second list's head is `None` and the `next` of the first list's tail is `None`.

**6.4** Write `concatenate(head1, head2)` — join two doubly linked lists end to end. Return the head of the combined list.

---

## Level 7: Complex Manipulation

**7.1** Write `reverse_between(head, left, right)` — reverse only the sublist from position `left` to `right` (1-indexed). All `prev` and `next` pointers in the entire list must remain consistent. This is the doubly linked version of the singly linked list challenge, and it's harder because there are more links to get right at the boundaries.

**7.2** Write `sort_biotonic(head)` — a *bitonic* doubly linked list first increases and then decreases (e.g., `1 -> 3 -> 7 -> 5 -> 2`). Sort it in O(n) time. (Hint: think about splitting and merging.)

**7.3** Write `flatten(head)` — each node now has an additional `child` attribute (default `None`) that may point to the head of another doubly linked list. Flatten the entire structure into a single-level doubly linked list. When a node has a child list, insert the child list immediately after that node (before the node's original next). Process all children recursively/iteratively.

Use this extended node:
```python
class Node:
    def __init__(self, data, prev=None, next=None, child=None):
        self.data = data
        self.prev = prev
        self.next = next
        self.child = child
```

**7.4** Write `remove_duplicates_unsorted(head)` — remove duplicate values from an unsorted doubly linked list, keeping the first occurrence. The `prev` pointer makes the unlinking easier than in the singly linked version — notice the difference.

---

## Level 8: The Hairy Stuff

**8.1** Write `reverse_in_groups(head, k)` — reverse in groups of `k`, maintaining all `prev` pointers. The boundary stitching between groups is the hard part: each reversed group's new tail must connect forward to the next group's new head, and all `prev` links must point back correctly.

**8.2** Write `merge_sort(head)` — sort a doubly linked list using merge sort in O(n log n) time. You've written `find_middle`, `split`, and `merge_sorted` in earlier problems. Now combine them, keeping `prev` pointers consistent throughout.

**8.3** Write a simple **LRU Cache** backed by a doubly linked list and a Python dictionary:
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

**8.4** Write `clone_with_random(head)` — each node has an additional `random` attribute that points to any node in the list (or `None`). Deep-copy the entire list, including both `next`/`prev` links and `random` pointers. The cloned nodes must point to their cloned counterparts, not to the original nodes.

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
