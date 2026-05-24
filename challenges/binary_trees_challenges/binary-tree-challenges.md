# Binary Tree Challenges

_Problems: 13/38._

A graduated sequence of programming challenges for building deep fluency with binary trees: construction, the standard traversals, structural operations, search-tree variants, reconstruction, and a final tier of harder applications.

**Language:** Python.

**Constraint:** every problem is solvable with the `Node` class from 1a, plus recursion, an explicit stack, or a queue where appropriate. No external libraries beyond the standard `collections` module. A plain `dict` or `set` as a helper is fine where it falls out naturally.

**Spirit:** when a problem names a technique ("use a queue", "O(1) extra space"), it means *don't bypass the structure with a one-liner*. The point is to grapple with the tree as a structure, not to produce a correct answer by any means.

---

## [x] Level 1 — Build a binary tree

- [x] **1a — Node class** — Status:

Implement a `Node` class with attributes `value`, `left`, `right`, where `left` and `right` are either `None` or another `Node`. Provide a classmethod `Node.from_nested(spec)` that builds a tree from nested tuples of the form `(value, left_subtree, right_subtree)`, where each subtree is either `None` or another such tuple.

```
Node.from_nested((1, (2, None, None), (3, None, None)))
#       1
#      / \
#     2   3
```

`Node.from_nested(None)` returns `None`.

- [x] **1b — Build from level-order** — Status:

Implement `from_level_order(values)` that builds a binary tree from a level-order list where `None` denotes a missing node. Children of a `None` slot are not represented in the list at all. Return the root, or `None` if `values` is empty.

```
from_level_order([1, 2, 3, None, 4, 5, None])
#       1
#      / \
#     2   3
#      \  /
#       4 5
```

---

## [x] Level 2 — Recursive traversals

- [x] **2a — Preorder** — Status:

Implement `preorder(root) -> list` that returns the values of the tree in preorder (root, left, right). For an empty tree, return `[]`.

```
preorder(from_level_order([1, 2, 3, 4, 5]))   # [1, 2, 4, 5, 3]
```

- [x] **2b — Inorder** — Status:

Implement `inorder(root) -> list` that returns the values in inorder (left, root, right). For an empty tree, return `[]`.

```
inorder(from_level_order([1, 2, 3, 4, 5]))    # [4, 2, 5, 1, 3]
```

- [x] **2c — Postorder** — Status:

Implement `postorder(root) -> list` that returns the values in postorder (left, right, root). For an empty tree, return `[]`.

```
postorder(from_level_order([1, 2, 3, 4, 5]))  # [4, 5, 2, 3, 1]
```

---

## [ ] Level 3 — Iterative traversals

For Level 3, you may use an explicit stack. No recursion — assume the tree may be deeper than the call stack allows.

- [x] **3a — Iterative preorder** — Status:

Implement `preorder_iterative(root) -> list`. The output must match `preorder` from 2a.

- [x] **3b — Iterative inorder** — Status:

Implement `inorder_iterative(root) -> list`. The output must match `inorder` from 2b.

- [ ] **3c — Iterative postorder** — Status:

Implement `postorder_iterative(root) -> list`. The output must match `postorder` from 2c. Of the three iterative traversals this one demands the most care: the visit-order constraint means a node is not ready to be emitted at the moment you first reach it.

---

## [x] Level 4 — Level-order traversal

For Level 4, you may use a queue (e.g. `collections.deque`).

- [x] **4a — Level-order flat** — Status:

Implement `level_order(root) -> list` that returns all values in BFS order (top-to-bottom, left-to-right within each level). For an empty tree, return `[]`.

```
level_order(from_level_order([1, 2, 3, 4, None, 5]))   # [1, 2, 3, 4, 5]
```

- [x] **4b — Level-order by layer** — Status:

Implement `level_order_layers(root) -> list[list]` where each inner list is one layer, top-to-bottom.

```
level_order_layers(from_level_order([1, 2, 3, 4, None, 5]))
# [[1], [2, 3], [4, 5]]
```

- [x] **4c — Right view** — Status:

Implement `right_view(root) -> list` returning the rightmost value at each level, top-to-bottom. For an empty tree, return `[]`.

```
right_view(from_level_order([1, 2, 3, None, 4, None, None]))
# [1, 3, 4]
```

---

## [ ] Level 5 — Properties

- [x] **5a — Count nodes** — Status:

Implement `count_nodes(root) -> int`. The empty tree has `0` nodes.

- [x] **5b — Height** — Status:

Implement `height(root) -> int`. The height of an empty tree is `-1`; a single-node tree has height `0`.

- [x] **5c — Sum values** — Status:

Implement `sum_values(root) -> int`. The sum over an empty tree is `0`. Assume node values are integers.

- [ ] **5d — Count leaves** — Status:

Implement `count_leaves(root) -> int`, the number of nodes with no children. The empty tree has `0` leaves; a single node is `1` leaf.

- [ ] **5e — Max value** — Status:

Implement `max_value(root) -> int`, the largest value in the tree. Choose and document a behaviour for the empty tree (e.g. raise `ValueError`).

- [ ] **5f — Min depth** — Status:

Implement `min_depth(root) -> int`, the number of edges on the shortest path from the root to *any leaf*. Empty: `-1`. Single node: `0`. Mind the case where a node has only one child:

```
min_depth(from_level_order([1, None, 2, None, 3]))   # 2
#   1
#    \
#     2
#      \
#       3
```

---

## [ ] Level 6 — Paths

- [ ] **6a — Has path sum** — Status:

Implement `has_path_sum(root, target) -> bool`. Return `True` iff there exists a root-to-leaf path whose values sum to `target`. Return `False` for an empty tree.

```
has_path_sum(from_level_order([5, 4, 8, 11, None, 13, 4, 7, 2]), 22)   # True
has_path_sum(from_level_order([1, 2, 3]), 5)                            # False
```

- [ ] **6b — All root-to-leaf paths** — Status:

Implement `all_paths(root) -> list[list]`. Each inner list is the values along one root-to-leaf path, in root-to-leaf order. The relative order of paths must be the order in which their leaves appear in a left-to-right preorder traversal. For an empty tree, return `[]`.

```
all_paths(from_level_order([1, 2, 3, 4, 5]))
# [[1, 2, 4], [1, 2, 5], [1, 3]]
```

---

## [ ] Level 7 — Structural operations

- [ ] **7a — Equal** — Status:

Implement `equals(a, b) -> bool`. Two trees are equal iff they have the same shape and the same values at corresponding positions. Two empty trees are equal.

- [ ] **7b — Mirror in place** — Status:

Implement `mirror_in_place(root) -> None`. Swap `left` and `right` at every node. The empty tree is a no-op.

```
t = from_level_order([1, 2, 3, 4, 5])
mirror_in_place(t)
level_order(t)   # [1, 3, 2, 5, 4]
```

- [ ] **7c — Is symmetric** — Status:

Implement `is_symmetric(root) -> bool`. The tree is symmetric iff its left subtree is a mirror image of its right subtree (in both shape and values). The empty tree is symmetric.

```
is_symmetric(from_level_order([1, 2, 2, 3, 4, 4, 3]))         # True
is_symmetric(from_level_order([1, 2, 2, None, 3, None, 3]))   # False
```

- [ ] **7d — Is balanced** — Status:

Implement `is_balanced(root) -> bool`: at every node, the heights of its two subtrees differ by at most 1. The empty tree is balanced. A naive solution recomputes heights and runs in O(n²); an O(n) solution returns height information as it goes — that one-pass idea returns in Level 9.

```
is_balanced(from_level_order([1, 2, 3]))         # True
is_balanced(from_level_order([1, 2, None, 3]))   # False
```

---

## [ ] Level 8 — Structural modification

These return or rearrange nodes. Be precise, on paper, about which pointers change and in what order.

- [ ] **8a — Prune zero subtrees** — Status:

Implement `prune_zero_subtrees(root) -> Node | None`. Remove every subtree all of whose nodes have value `0`. Return the (possibly `None`) modified root.

```
prune_zero_subtrees(from_level_order([5, 0, 3, 0, 0]))
# Before:        After:
#     5              5
#    / \              \
#   0   3              3
#  / \
# 0   0
```

- [ ] **8b — Merge two trees** — Status:

Implement `merge_two_trees(t1, t2) -> Node`. A position present in both inputs holds the sum of the two values; a position present in only one input holds that input's node. Mutating `t1` in place and returning it is fine.

```
t1 = from_level_order([1, 3, 2, 5])
t2 = from_level_order([2, 1, 3, None, 4, None, 7])
level_order(merge_two_trees(t1, t2))   # [3, 4, 5, 5, 4, 7]
```

- [ ] **8c — Flatten to the right** — Status:

Implement `flatten_to_right(root) -> None`. Rearrange the tree in place into a right-leaning chain (every `left` is `None`) whose values, read down the `right` pointers, are the tree's preorder sequence.

```
flatten_to_right(from_level_order([1, 2, 5, 3, 4, None, 6]))
# Before:          After:  1
#     1                     \
#    / \                     2
#   2   5                     \
#  / \   \                     3
# 3   4   6                     \
#                                4
#                                 \
#                                  5
#                                   \
#                                    6
```

---

## [ ] Level 9 — Information flowing both ways

Each subtree returns a small piece of information *up* while a result is accumulated *across* the whole tree. 9a and 9d are the same shape at two intensities.

- [ ] **9a — Diameter** — Status:

Implement `diameter(root) -> int`. The diameter is the number of edges on the longest path between any two nodes. The diameter of an empty or single-node tree is `0`. Total runtime should be O(n).

```
diameter(from_level_order([1, 2, 3, 4, 5]))   # 3
```

- [ ] **9b — Lowest common ancestor** — Status:

Implement `lowest_common_ancestor(root, a, b) -> Node | None`, where `a` and `b` are `Node` references known to be present in the tree rooted at `root`. Return the deepest node that is an ancestor of both `a` and `b`. A node is its own ancestor. Return `None` only if `root` is `None`.

- [ ] **9c — Count paths with sum** — Status:

Implement `count_paths_with_sum(root, target) -> int`: the number of distinct downward paths (following `left`/`right` pointers, any start node, ending at or below it, length ≥ 1) whose values sum to `target`.

```
count_paths_with_sum(from_level_order([1, 2, 3]), 3)   # 2
# the single node 3, and the path 1 -> 2
```

- [ ] **9d — Max path sum** — Status:

Implement `max_path_sum(root) -> int`: the largest possible sum of values along any path, where a path is a sequence of distinct nodes in which each consecutive pair is joined by an edge. A single node is a valid path. Values may be negative; assume at least one node.

```
max_path_sum(from_level_order([-10, 9, 20, None, None, 15, 7]))   # 42
# 15 -> 20 -> 7
```

---

## [ ] Level 10 — Binary search trees

A binary search tree is a binary tree carrying an ordering invariant. This is the one genuinely new *idea* in the sequence — everything else is the recursion machinery you already have. Treat the input as a BST built by left-then-right key comparisons; duplicate keys (where applicable) go to the right.

- [ ] **10a — BST search** — Status:

Implement `bst_search(root, target) -> Node | None`. Return the first node found (in BST search order) whose `value == target`, or `None`.

- [ ] **10b — BST insert** — Status:

Implement `bst_insert(root, value) -> Node`. Return the (possibly new) root. Duplicates go to the right. Build the tree by chained calls:

```
root = None
for v in [5, 2, 8, 1, 3]:
    root = bst_insert(root, v)
inorder(root)   # [1, 2, 3, 5, 8]
```

- [ ] **10c — Is valid BST** — Status:

Implement `is_valid_bst(root) -> bool`. A valid BST satisfies: for every node, all values in its left subtree are strictly less than the node's value, and all values in its right subtree are greater than or equal to the node's value. The empty tree is a valid BST.

```
is_valid_bst(from_level_order([2, 1, 3]))                     # True
is_valid_bst(from_level_order([5, 1, 4, None, None, 3, 6]))   # False
```

---

## [ ] Level 11 — Reconstruction and serialization

Recovering structure from sequences; round-trippable representations.

- [ ] **11a — Build from preorder and inorder** — Status:

Implement `build_from_preorder_inorder(preorder, inorder) -> Node | None`, reconstructing the unique tree with the given preorder and inorder traversals (two lists of the same distinct values). Return `None` for empty inputs.

```
t = build_from_preorder_inorder([1, 2, 4, 5, 3], [4, 2, 5, 1, 3])
level_order(t)   # [1, 2, 3, 4, 5]
```

- [ ] **11b — Serialize** — Status:

Implement `serialize(root) -> str`, encoding the tree as preorder tokens separated by commas. Use `#` for null children, so the empty tree is `#` and a single node `7` is `7,#,#`. `deserialize` (11c) must invert this same format.

- [ ] **11c — Deserialize** — Status:

Implement `deserialize(data) -> Node | None`, the inverse of `serialize` (11b). The string contains preorder tokens separated by commas. `#` represents a null child, so `#` is the empty tree and `7,#,#` is a single node `7`.

---

## [ ] Level 12 — The hairy tier

- [ ] **12a — Morris inorder** — Status:

Implement `morris_inorder(root) -> list`, returning the inorder sequence (matching 2b) using **O(1) extra space**: no recursion, no explicit stack, queue, or set — only the output list. The tree must be unchanged when the call returns.

- [ ] **12b — Boundary traversal** — Status:

Implement `boundary_traversal(root) -> list`, the anti-clockwise boundary as a list of values:

1. The root.
2. The left boundary (excluding the root and excluding leaves), top to bottom.
3. All leaves, left to right.
4. The right boundary (excluding the root and excluding leaves), bottom to top.

Each node appears exactly once.

```
boundary_traversal(from_level_order([1, 2, 3, 4, 5, None, 6, None, None, 7, 8]))
# [1, 2, 4, 7, 8, 6, 3]
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
#        / \
#       7   8
```

---

## Beyond Level 12

When the sequence is cleared, directions to push into:

- **Zigzag level order.** Like 4b, but alternate left-to-right and right-to-left by layer.
- **Vertical order traversal.** Group nodes by horizontal column index; within a column, top to bottom.
- **`count_paths_with_sum` in O(n).** Revisit 9c with a running prefix-sum frequency map.
- **Constrained `max_path_sum`.** Maximum sum from root to any leaf; from any leaf to any leaf.
- **`build_from_inorder_postorder`.** As 11a, with postorder instead of preorder. Mind the orientation difference.
- **BST delete.** Remove a key from a BST, preserving the invariant — the three cases (leaf, one child, two children) are the whole problem.
- **Recover a swapped BST.** Two nodes of a valid BST have had their values exchanged; restore it. Ties the ordering invariant back to inorder traversal.
