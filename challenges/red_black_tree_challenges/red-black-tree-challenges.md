# Red-Black Tree Programming Challenges

_Problems: 30._

A graduated sequence of programming challenges for understanding, implementing, and manipulating red-black trees in Python. Each level adds a single new dimension of complexity to what came before. The property checker built in Level 1 is the keystone — reuse it as your verification tool throughout.

---

## Preliminaries — conventions to fix before you start

Pick one and stay consistent across all levels:

1. **Null representation.** CLRS uses a single sentinel `T.nil` (a real black node that all leaves and the root's parent point to). The alternative is `None`. The sentinel makes fix-up cleaner because you can read `nil.color` and `nil.parent` without `None` checks, and you can even temporarily set `nil.parent` during delete fix-up. The `None` approach is more idiomatic Python but forces you to guard against `None` everywhere in fix-up. Recommendation: use the sentinel.

2. **Parent pointers.** Required. CLRS uses them; insert/delete fix-up effectively cannot be written cleanly without them.

3. **Color encoding.** A `Color` enum, two string constants `"R"` and `"B"`, or two integer constants — your call. Pick once.

4. **Tree wrapper.** Have a `Tree` class that holds the `root` (and the `nil` sentinel if you go that route). Operations are methods on `Tree`, not free functions.

The five RBT properties (CLRS notation):
1. Every node is either red or black.
2. The root is black.
3. Every leaf (NIL) is black.
4. If a node is red, then both its children are black. (No two reds in a row on any path.)
5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes (the *black-height*).

---

## Level 1 — Foundations

- [ ] **1a. `Node` class and property verifier** — Status:

Define your `Node` class with: `key`, `color`, `parent`, `left`, `right`. Then write:

```
def is_valid_red_black_tree(tree) -> bool
```

It should check all five properties. Internally, you will need to compute the black-height — the number of black nodes on any simple path from a node to a descendant NIL, not counting the node itself. (Decide your own convention for whether NIL counts; just be consistent.) Property 5 is verified by checking that the black-height is the same on both subtrees of every node.

The function should also implicitly verify the BST property (in-order key ordering), since an RBT is a BST plus the color invariants.

Bonus version: `diagnose(tree) -> List[str]` that returns a list of which specific properties are violated. This is the more useful version for debugging later levels.

- [ ] **1b. Pretty-printer** — Status:

```
def render(tree) -> str
```

Render the tree in a way that lets you actually see what's going on, with colors marked. Indented format works well:

```
30B
├── 20B
│   ├── 10R
│   └── 25R
└── 40B
```

Or sideways with R/B suffixes. Whatever you build, build it well — you will stare at it for hours during the rest of these levels.

- [ ] **1c. Manual construction** — Status:

Construct, by hand (i.e. by directly assigning fields), at least:
- Three valid RBTs of differing shapes.
- One tree that violates property 2 only.
- One that violates property 4 only.
- One that violates property 5 only.

Run them through your verifier from 1a. Confirm valid trees pass and invalid trees fail with the correct diagnosis.

---

## Level 2 — BST operations on an RBT (free reuse)

Color is irrelevant to all of these. Implement them anyway, both to confirm your `Node` interface works and to have them available for later levels.

- [ ] **2a. Search** — Status:

```
def search(tree, key) -> Optional[Node]
```

Iterative version preferred.

- [ ] **2b. Min, max, successor, predecessor** — Status:

```
def minimum(node) -> Node
def maximum(node) -> Node
def successor(node) -> Optional[Node]
def predecessor(node) -> Optional[Node]
```

These take a node, not a key. Successor uses the parent pointer when there is no right subtree.

- [ ] **2c. In-order traversal** — Status:

```
def inorder(tree) -> List[key]
```

Verify the result is sorted on every tree you have. This will be your sanity check after every rotation, insert, and delete.

---

## Level 3 — Rotations

- [ ] **3a. Left rotate** — Status:

```
def left_rotate(tree, x) -> None
```

Pre: `x.right` is not NIL. Post: `x.right` becomes `x`'s old right child's left child, and `x.right` (the old one) becomes the parent of `x`.

Get the pointer surgery exactly right:
- Three pointers change going *down* (children).
- Three pointers change going *up* (parents).
- The root may change (if `x` was the root, the new root is `x`'s old right child).

Draw it on paper before coding. Pointers in both directions must remain consistent.

- [ ] **3b. Right rotate** — Status:

Mirror of 3a. Should fall out almost mechanically once 3a is right.

- [ ] **3c. In-order invariance test** — Status:

Write a test: take any tree, perform any sequence of rotations on any nodes, and confirm in-order traversal is unchanged. Rotations rearrange the tree but never the sorted order — this is the invariant that makes them safe. Build a property-based test that performs random valid rotations and verifies invariance.

---

## Level 4 — Insertion

- [ ] **4a. BST-style colored insert (no fix-up yet)** — Status:

```
def naive_insert(tree, key) -> Node
```

Standard BST insert. Color the newly inserted node red. Return the inserted node.

After the call, the tree may not be a valid RBT — it may violate property 2 (if the tree was empty and the new node is red root) or property 4 (if the parent is red). Property 5 is preserved because the new node is red and replaces a NIL leaf, contributing zero to black-height.

Call your verifier from 1a — confirm it correctly identifies which property is violated.

- [ ] **4b. Identify the violation** — Status:

Given the inserted red node `z` from 4a, write a function that classifies the tree state:

```
def classify_post_insert(tree, z) -> str
```

Returns one of: `"valid"`, `"red_root"`, `"red_red"`. The `"red_red"` case is the one that needs fix-up; if the parent is black or `z` is the root, you handle those trivially.

This is just an exercise in being precise about the case structure before writing fix-up code.

- [ ] **4c. Insert fix-up — the uncle-red case alone** — Status:

The fix-up loop walks up the tree as long as `z.parent.color == RED`. There are three cases (and three mirror cases, depending on whether the parent is a left or right child of the grandparent). Implement only the uncle-red case for now:

> If `z`'s uncle is red: recolor parent and uncle to black, recolor grandparent to red, move `z` up to the grandparent, repeat the loop.

```
def insert_fixup_uncle_red_only(tree, z) -> None
```

This will not produce a fully valid RBT in general — it handles only one of the cases. But it should produce a valid RBT on inputs where the uncle-red case is the only one that ever fires during the entire fix-up. Construct such an input by hand and verify.

- [ ] **4d. Insert fix-up — the uncle-black cases** — Status:

When the uncle is black, the fix is local: one or two rotations plus a recolor, and the loop terminates. There are two sub-cases:

> Case 2: `z` is the "inner" grandchild (e.g. parent is a left child and `z` is a right child). Rotate to convert this to case 3.
>
> Case 3: `z` is the "outer" grandchild. Recolor parent and grandparent, rotate the grandparent, terminate.

Implement these cases (still without combining with 4c yet):

```
def insert_fixup_uncle_black_only(tree, z) -> None
```

Test on hand-constructed inputs where the uncle is always black at the moment of fix-up.

- [ ] **4e. Full `rb_insert`** — Status:

```
def insert(tree, key) -> Node
```

Combine 4a, 4c, and 4d into the full insert with fix-up. Don't forget to set the root to black at the end (handles the red-root case from 4b).

- [ ] **4f. Insertion stress test** — Status:

Write a test that inserts a random sequence of N keys (try N = 100, 1000, 10000) and asserts after each insert that:
- The verifier from 1a passes.
- In-order traversal returns the sorted sequence of keys inserted so far.

If anything fails, your `render` from 1b should be your first stop.

---

## Level 5 — Empirical structural checks

These are not new operations; they are diagnostics that build intuition about *why* the RBT properties give logarithmic height.

- [ ] **5a. Black-height bound** — Status:

After 5a inserts of n random keys, plot or print:
- Tree height (longest root-to-leaf simple path, counting nodes).
- Black-height of the root.
- The bound `2 * log2(n + 1)`.

The height should always be at most `2 * bh(root)`, and `bh(root)` should be at most `log2(n + 1)`. Convince yourself empirically that `height ≤ 2 * log2(n + 1)`.

- [ ] **5b. Operation counts per insert** — Status:

Instrument your `insert` to count rotations performed and recolorings (color flips) per call. Insert n keys; record per-call counts. Compute the average and max. Both should look like `O(1)` amortized for rotations (insert does at most 2) and `O(log n)` worst case for recolorings.

- [ ] **5c. Adversarial input vs naive BST** — Status:

Insert keys `1, 2, 3, ..., n` into:
- A naive BST.
- Your RBT.

Print the height of each. The BST will be `n`. The RBT will be roughly `2 log n`. This is the visible payoff of the balancing.

---

## Level 6 — Deletion

Delete is structurally similar to insert (BST mechanics, then fix-up) but the fix-up is harder: there are four cases instead of three, and the asymmetry between left and right children makes the mirror cases less mechanical.

- [ ] **6a. Transplant** — Status:

```
def transplant(tree, u, v) -> None
```

Replace the subtree rooted at `u` with the subtree rooted at `v`. Update `u.parent`'s child pointer (or the tree root if `u` was the root) and set `v.parent`. Does not touch `u`'s children. This is your delete primitive.

- [ ] **6b. BST-style delete (adapted)** — Status:

```
def naive_delete(tree, z) -> Tuple[Node, Color]
```

Three cases, as in standard BST delete:
- `z` has no left child: transplant `z.right` for `z`.
- `z` has no right child: transplant `z.left` for `z`.
- `z` has two children: find `y = minimum(z.right)`. If `y` is `z.right`, transplant `y` for `z` and reassign `z.left` to `y`. Otherwise transplant `y.right` for `y`, then `y` for `z`, fixing up children.

The wrinkle that makes this RBT-specific: track the *color of the node that was physically removed or moved within the tree* and the *node that took its place*. If a black node was removed/moved, the tree may now violate property 5 (some path lost a black node) or property 4 (red-red at the substitution site).

Return the substituted node and the original color of the moved node, since that is what the fix-up needs.

Run your verifier — confirm it diagnoses the violation correctly when a black node was removed.

- [ ] **6c. Delete fix-up** — Status:

The fix-up walks up the tree from the substituted node `x`, treating `x` as carrying an "extra black" (the doubly-black sentinel of CLRS). Four cases:

> Case 1: `x`'s sibling `w` is red. Rotate to make `w` black; reduces to one of cases 2, 3, 4.
>
> Case 2: `w` is black, both of `w`'s children are black. Recolor `w` red, push the extra black up to `x.parent`.
>
> Case 3: `w` is black, `w`'s left child is red, `w`'s right child is black (when `x` is a left child; mirror otherwise). Rotate `w` to convert to case 4.
>
> Case 4: `w` is black, `w`'s right child is red (when `x` is a left child). Rotate `x.parent`, recolor, terminate.

```
def delete_fixup(tree, x) -> None
```

This is the hardest single piece of the entire RBT machinery. Take it slowly. Each case has a mirror; do them one mirror at a time and lean hard on the verifier. Hand-construct minimal inputs that exercise each case in isolation before testing combinations.

- [ ] **6d. Full `rb_delete`** — Status:

```
def delete(tree, key) -> bool
```

Find the node, run 6b, run 6c if the displaced node was black. Return whether deletion happened (False if key not found).

- [ ] **6e. Mixed insert/delete stress test** — Status:

Run a randomized sequence of inserts and deletes of length 10,000, each from a small key universe (say 1..1000) so deletes hit. After each operation, assert:
- Verifier passes.
- In-order traversal matches the multiset (or set) of keys you've tracked separately.

When something breaks, the trace + your renderer is your debugging path.

---

## Level 7 — Augmentation: order-statistics tree

This is the first step toward seeing RBTs as a substrate that supports *more* than ordered set operations. The key technical insight: any subtree-summary (like size) that can be computed from a node's two children's summaries can be maintained across insert, delete, and rotation in O(1) extra work per structural change.

- [ ] **7a. Add `size` field; maintain it** — Status:

Add `size` to your `Node`: the number of nodes in the subtree rooted at that node. NIL has size 0.

Update insert, delete, left rotate, and right rotate to maintain `size` correctly. Rotation only changes the size of two nodes — the one rotated over and its replacement. Insert and delete update sizes along the path from the affected leaf up to the root.

Write a verifier:

```
def is_size_consistent(tree) -> bool
```

That recomputes sizes from scratch and compares them to the stored values. Run after every insert and delete in a stress test.

- [ ] **7b. `select(i)` — find the i-th smallest** — Status:

```
def select(tree, i) -> Node
```

In O(log n). Walk down from the root: at each node, the rank of the node within its subtree is `node.left.size + 1`. If `i` matches, return; if `i` is smaller, go left; otherwise go right with `i` decreased by `node.left.size + 1`.

- [ ] **7c. `rank(x)` — find the rank of node x** — Status:

```
def rank(tree, x) -> int
```

In O(log n). Start with rank `x.left.size + 1`. Walk up to root: every time you came up from a right child, add `parent.left.size + 1` to the rank.

- [ ] **7d. Range count** — Status:

```
def count_in_range(tree, low, high) -> int
```

How many keys are in `[low, high]`? Equivalent to `rank(predecessor_or_equal(high)) - rank(predecessor(low))` plus careful boundary handling, or a direct tree walk that prunes whole subtrees when their key range is fully outside `[low, high]`.

---

## Level 8 — Truly hairy

Three classic CLRS problems. Each is a multi-day undertaking; do not expect to finish one in a single session.

- [ ] **8a. Build an optimal RBT from a sorted array in O(n)** — Status:

```
def build_from_sorted(keys: List[int]) -> Tree
```

Given a sorted array of `n` keys, construct a valid RBT in O(n). The naive approach (insert one by one) is O(n log n). The trick is to build the tree recursively by midpoint partitioning — this gives a balanced BST. The wrinkle is *coloring* it: most levels can be all black, but the bottom (incomplete) level needs to be red so that black-heights match across all root-to-leaf paths.

The key insight: if `n + 1` is a power of 2, the tree is perfectly complete and can be all black. Otherwise, the bottom level is incomplete; the lowest-level *real* nodes that sit above NIL leaves need to be red, so that paths through them have the same black count as paths that end one level higher.

- [ ] **8b. Join two RBTs** — Status:

```
def join(t1, t2) -> Tree
```

Pre: every key in `t1` is less than every key in `t2`. Post: a single valid RBT containing all keys of both, in O(log n) time.

The technique:
- Find the larger of `t1`'s and `t2`'s black-heights. WLOG say `t1` has the larger black-height (call it `bh1 ≥ bh2`).
- Find a node `x` on the right spine of `t1` whose black-height is exactly `bh2` and whose color is black. Walk down the right spine, decrementing the black-height counter on every black step, until you hit `bh2`.
- Take the maximum of `t1` (or minimum of `t2`) as a new red "bridge" node, splice it between `x` and `t2`.
- Run insert fix-up on the bridge node.

Handling the case where one tree is empty, both are empty, the bridge insertion violates property 4, etc., is fiddly. Tracking black-heights correctly is the conceptual core.

- [ ] **8c. Split an RBT at a key** — Status:

```
def split(tree, k) -> Tuple[Tree, Tree]
```

Given an RBT and a key `k`, produce two valid RBTs `(t_lt, t_ge)` containing the keys less than `k` and the keys greater than or equal to `k` respectively. In O(log n) using `join`.

The technique walks down the tree from the root looking for `k`. At each step you take a left or right turn; the *other* subtree, plus the current node, contributes to one of `t_lt` or `t_ge`. Accumulate by repeatedly joining. The amortized cost works out because at each level you're joining trees of geometrically growing size.

This is the deepest test of your understanding of black-heights and the join primitive.

---

## Suggested cadence

Level 1 in a single session if you can. Levels 2 and 3 should also each be a single session.

Level 4 spans 2–3 sessions: 4a–4b in one, 4c–4d in another, 4e–4f in a third.

Level 5 in one short session. Level 6 across 3 sessions: 6a–6b, 6c, 6d–6e.

Level 7 across 2 sessions: 7a–7b, 7c–7d.

Level 8: each problem is its own session, possibly two.

Total: roughly 12–18 sessions if you go cleanly. Re-solve sessions for prior levels can run alongside.

---

## When you're stuck

Anything you cannot solve after honest attempts goes in the deep practice book and gets re-solved weekly. The classic stumbling blocks here are:

- Insert fix-up case 2 → case 3 transition (the rotation that "saves" you for the next case).
- Delete fix-up case 1 (sibling-red): why it must reduce to one of 2, 3, 4 in one more iteration.
- The doubly-black sentinel: what it really means, why the loop terminates.
- Maintaining augmented data through rotations.
- Tracking black-heights during join.

For any of these, write down precisely where the confusion is — that question goes in the deep practice book even before you find the answer.
