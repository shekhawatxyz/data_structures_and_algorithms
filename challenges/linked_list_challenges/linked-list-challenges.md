# Singly Linked Lists: Graduated Programming Challenges

Assume throughout that you are working with this node definition (or your own equivalent):

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
```

---

## Level 1: Getting Comfortable with the Structure

The point here is to get your hands on the basic shape — a node points to the next node, the last node points to `None` — and to write your first traversals.

**1.1** Write a function `build(values)` that takes a Python list and returns the head of a singly linked list containing those values in order.

**1.2** Write a function `to_list(head)` that takes the head of a linked list and returns a Python list of its values.

**1.3** Write a function `print_list(head)` that prints each element on one line, or in the format `3 -> 7 -> 2 -> None`.

**1.4** Write a function `length(head)` that returns the number of nodes in the list.

---

## Level 2: Single-Point Insertion and Search

You now manipulate the list at specific points, which requires thinking about pointer updates.

**2.1** Write `insert_front(head, value)` — returns the new head.

**2.2** Write `insert_back(head, value)` — returns the head. Think about the edge case where the list is empty.

**2.3** Write `search(head, value)` — returns `True` if the value is in the list, `False` otherwise.

**2.4** Write `insert_at(head, index, value)` — inserts a new node at position `index` (0-indexed). Returns the new head. Raise an error if the index is out of range.

---

## Level 3: Deletion

Deletion is where pointer manipulation starts requiring more care: you need to keep track of the node *before* the one you want to remove.

**3.1** Write `delete_first(head, value)` — removes the first node with the given value. Returns the (possibly new) head. Do nothing if the value isn't found.

**3.2** Write `delete_all(head, value)` — removes *every* node with the given value.

**3.3** Write `delete_at(head, index)` — removes the node at position `index`. Returns the new head.

**3.4** Write `delete_range(head, start, end)` — removes all nodes from index `start` to index `end` (inclusive). Returns the new head.

---

## Level 4: Queries That Require Some Thought

These are still single-list problems, but each one requires you to think slightly beyond simple traversal.

**4.1** Write `nth_from_end(head, n)` — returns the value of the nth node from the end (1-indexed, so `n=1` gives the last node). Do this in a single pass.

**4.2** Write `has_cycle(head)` — returns `True` if the linked list contains a cycle. (Construct a test case by manually pointing a node's `next` to an earlier node.)

**4.3** Write `find_middle(head)` — returns the middle node's value. (For even-length lists, return the second of the two middle nodes.) Do this in a single pass.

**4.4** Write `remove_duplicates_sorted(head)` — given a list whose values are in non-decreasing order, remove all duplicate values so each value appears only once.

---

## Level 5: Structural Transformation

Now you're changing the shape of the list itself, not just adding or removing nodes. These require you to hold and update multiple pointers simultaneously.

**5.1** Write `reverse(head)` — reverse the linked list iteratively. Returns the new head.

**5.2** Write `reverse_recursive(head)` — same thing, but recursively.

**5.3** Write `partition(head, x)` — rearrange the list so that all nodes with values less than `x` come before all nodes with values greater than or equal to `x`. The relative order within each partition should be preserved.

**5.4** Write `is_palindrome(head)` — returns `True` if the list reads the same forwards and backwards. Try to do this in O(n) time and O(1) extra space (you are allowed to modify and then restore the list).

---

## Level 6: Multi-List Operations

You now have to reason about two lists at once, advancing through both while maintaining invariants.

**6.1** Write `merge_sorted(head1, head2)` — given two sorted linked lists, merge them into a single sorted linked list (without creating new nodes — re-link the existing ones). Returns the head of the merged list.

**6.2** Write `interleave(head1, head2)` — weave two lists together: if list A is `1 -> 2 -> 3` and list B is `a -> b -> c`, the result is `1 -> a -> 2 -> b -> 3 -> c`. If one list is longer, the remaining elements go at the end.

**6.3** Write `add_numbers(head1, head2)` — each list represents a non-negative integer with digits stored in *reverse* order (so `2 -> 4 -> 3` represents 342). Return a new linked list representing their sum. Handle carries correctly.

**6.4** Write `split_alternating(head)` — split a single list into two lists by alternating nodes. `1 -> 2 -> 3 -> 4 -> 5` becomes `1 -> 3 -> 5` and `2 -> 4`. Return both heads.

---

## Level 7: Complex Manipulation

Each of these demands that you hold more state in your head, manage more pointers at once, or think recursively about subproblems within the list.

**7.1** Write `reverse_between(head, left, right)` — reverse only the sublist from position `left` to position `right` (1-indexed). The rest of the list remains unchanged.

**7.2** Write `rotate(head, k)` — rotate the list to the right by `k` places. So `1 -> 2 -> 3 -> 4 -> 5` rotated by 2 becomes `4 -> 5 -> 1 -> 2 -> 3`. Handle `k` greater than the list length.

**7.3** Write `remove_duplicates_unsorted(head)` — remove duplicates from an *unsorted* list, preserving the first occurrence of each value. You may use a Python `set`.

**7.4** Now write `remove_duplicates_unsorted_no_extra(head)` — same as above, but without using any extra data structure. (This will be O(n²), and that's fine.)

---

## Level 8: The Hairy Stuff

These problems require you to combine multiple ideas — reversal, merging, careful pointer surgery — or demand recursive thinking about groups and substructure within the list.

**8.1** Write `reverse_in_groups(head, k)` — reverse the list in groups of `k`. If the number of remaining nodes is less than `k`, reverse them as well. Example: `1 -> 2 -> 3 -> 4 -> 5` with `k=3` becomes `3 -> 2 -> 1 -> 5 -> 4`.

**8.2** Write `reorder(head)` — rearrange `L₀ -> L₁ -> ... -> Lₙ` into `L₀ -> Lₙ -> L₁ -> Lₙ₋₁ -> L₂ -> Lₙ₋₂ -> ...`. Do this in O(n) time and O(1) space. (Hint: this combines several ideas you've already implemented.)

**8.3** Write `merge_sort(head)` — sort a linked list using merge sort. Returns the new head. This should run in O(n log n) time. You've already written the pieces; now combine them.

**8.4** Write `add_numbers_forward(head1, head2)` — same as 6.3, but now the digits are stored in *forward* order (`3 -> 4 -> 2` represents 342). You may not reverse the input lists. (Think about what makes this harder than the reversed case, and what tool you need.)

---

## General Advice

- For each challenge, think first about what pointers you need and what invariant you're maintaining before writing code.
- Test with: the empty list, a single-node list, a two-node list, and a longer list. Edge cases in linked list problems almost always live at the boundaries.
- If you get stuck, draw the nodes and arrows on paper and step through your pointer updates by hand.
