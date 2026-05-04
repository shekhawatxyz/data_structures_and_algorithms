# Binary Tree Challenges

A graduated sequence of programming challenges for building deep fluency with binary trees and the standard traversals, structural operations, and search-tree variants built on top of them.

**Language:** Python.

**Constraint:** every problem is solvable with the `Node` class from 1a (plus stacks, queues, or recursion where appropriate). No external libraries beyond what the standard `collections` module provides.

**Spirit:** when a problem says "the intended technique uses recursion" or "use a queue," it means: don't bypass the structure with a one-liner. The point is to grapple with the tree as a structure, not to produce a correct answer by any means.

---

## Level 1 — Build a binary tree

### 1a — Node class

Implement a `Node` class with attributes `value`, `left`, `right`, where `left` and `right` are either `None` or another `Node`. Provide a classmethod `Node.from_nested(spec)` that builds a tree from nested tuples of the form `(value, left_subtree, right_subtree)`, where each subtree is either `None` or another such tuple.

```
Node.from_nested((1, (2, None, None), (3, None, None)))
#       1
#      / \
#     2   3
```

`Node.from_nested(None)` returns `None`.

### 1b — Build from level-order

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

## Level 2 — Recursive traversals

### 2a — Preorder

Implement `preorder(root) -> list` that returns the values of the tree in preorder (root, left, right). For an empty tree, return `[]`.

```
preorder(from_level_order([1, 2, 3, 4, 5]))   # [1, 2, 4, 5, 3]
```

### 2b — Inorder

Implement `inorder(root) -> list` that returns the values in inorder (left, root, right). For an empty tree, return `[]`.

```
inorder(from_level_order([1, 2, 3, 4, 5]))    # [4, 2, 5, 1, 3]
```

### 2c — Postorder

Implement `postorder(root) -> list` that returns the values in postorder (left, right, root). For an empty tree, return `[]`.

```
postorder(from_level_order([1, 2, 3, 4, 5]))  # [4, 5, 2, 3, 1]
```

---

## Level 3 — Iterative traversals

For Level 3, you may use an explicit stack. No recursion — assume the tree may be deeper than the call stack allows.

### 3a — Iterative preorder

Implement `preorder_iterative(root) -> list`. The output must match `preorder` from 2a.

### 3b — Iterative inorder

Implement `inorder_iterative(root) -> list`. The output must match `inorder` from 2b.

---

## Level 4 — Level-order traversal

For Level 4, you may use a queue (e.g. `collections.deque`).

### 4a — Level-order flat

Implement `level_order(root) -> list` that returns all values in BFS order (top-to-bottom, left-to-right within each level). For an empty tree, return `[]`.

```
level_order(from_level_order([1, 2, 3, 4, None, 5]))   # [1, 2, 3, 4, 5]
```

### 4b — Level-order by layer

Implement `level_order_layers(root) -> list[list]` where each inner list is one layer, top-to-bottom.

```
level_order_layers(from_level_order([1, 2, 3, 4, None, 5]))
# [[1], [2, 3], [4, 5]]
```

### 4c — Right view

Implement `right_view(root) -> list` returning the rightmost value at each level, top-to-bottom. For an empty tree, return `[]`.

```
right_view(from_level_order([1, 2, 3, None, 4, None, None]))
# [1, 3, 4]
```

---

## Level 5 — Properties

### 5a — Count nodes

Implement `count_nodes(root) -> int`. The empty tree has `0` nodes.

### 5b — Height

Implement `height(root) -> int`. The height of an empty tree is `-1`; a single-node tree has height `0`.

### 5c — Sum values

Implement `sum_values(root) -> int`. The sum over an empty tree is `0`. Assume node values are integers.

---

## Level 6 — Paths

### 6a — Has path sum

Implement `has_path_sum(root, target) -> bool`. Return `True` iff there exists a root-to-leaf path whose values sum to `target`. Return `False` for an empty tree.

```
has_path_sum(from_level_order([5, 4, 8, 11, None, 13, 4, 7, 2]), 22)   # True
has_path_sum(from_level_order([1, 2, 3]), 5)                            # False
```

### 6b — All root-to-leaf paths

Implement `all_paths(root) -> list[list]`. Each inner list is the values along one root-to-leaf path, in root-to-leaf order. The relative order of paths must be the order in which their leaves appear in a left-to-right preorder traversal. For an empty tree, return `[]`.

```
all_paths(from_level_order([1, 2, 3, 4, 5]))
# [[1, 2, 4], [1, 2, 5], [1, 3]]
```

---

## Level 7 — Structural operations

### 7a — Equal

Implement `equals(a, b) -> bool`. Two trees are equal iff they have the same shape and the same values at corresponding positions. Two empty trees are equal.

### 7b — Mirror in place

Implement `mirror_in_place(root) -> None`. Swap `left` and `right` at every node. The empty tree is a no-op.

```
t = from_level_order([1, 2, 3, 4, 5])
mirror_in_place(t)
level_order(t)   # [1, 3, 2, 5, 4]
```

### 7c — Is symmetric

Implement `is_symmetric(root) -> bool`. The tree is symmetric iff its left subtree is a mirror image of its right subtree (in both shape and values). The empty tree is symmetric.

```
is_symmetric(from_level_order([1, 2, 2, 3, 4, 4, 3]))   # True
is_symmetric(from_level_order([1, 2, 2, None, 3, None, 3]))   # False
```

---

## Level 8 — Binary search trees

For Level 8, treat the input as a binary search tree built by left-then-right key comparisons. Duplicate keys (where applicable) go to the right.

### 8a — BST search

Implement `bst_search(root, target) -> Node | None`. Return the first node found (in BST search order) whose `value == target`, or `None`.

### 8b — BST insert

Implement `bst_insert(root, value) -> Node`. Return the (possibly new) root. Duplicates go to the right. Build the tree by chained calls:

```
root = None
for v in [5, 2, 8, 1, 3]:
    root = bst_insert(root, v)
inorder(root)   # [1, 2, 3, 5, 8]
```

### 8c — Is valid BST

Implement `is_valid_bst(root) -> bool`. A valid BST satisfies: for every node, all values in its left subtree are strictly less than the node's value, and all values in its right subtree are greater than or equal to the node's value. The empty tree is a valid BST.

```
is_valid_bst(from_level_order([2, 1, 3]))           # True
is_valid_bst(from_level_order([5, 1, 4, None, None, 3, 6]))   # False
```

---

## Level 9 — Hairy applications

### 9a — Lowest common ancestor

Implement `lowest_common_ancestor(root, a, b) -> Node | None`, where `a` and `b` are `Node` references known to be present in the tree rooted at `root`. Return the deepest node that is an ancestor of both `a` and `b`. A node is its own ancestor. Return `None` only if `root` is `None`.

### 9b — Diameter

Implement `diameter(root) -> int`. The diameter is the number of edges on the longest path between any two nodes in the tree. The diameter of an empty or single-node tree is `0`. Total runtime should be O(n).

```
diameter(from_level_order([1, 2, 3, 4, 5]))   # 3
```
