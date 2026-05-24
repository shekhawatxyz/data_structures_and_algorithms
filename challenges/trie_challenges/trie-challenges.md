# Trie programming challenges

_Problems: 0/22._

A graduated sequence of programming challenges to build and stress-test understanding of tries (prefix trees) in Python. Each level introduces one new conceptual demand on top of the previous; sub-problems within a level explore variations of that demand and consolidate the new mental move.

## Conceptual progression

| Level | New demand |
|-------|-----------|
| 1 | Build the structure; primitive lookups (terminal flag matters) |
| 2 | Full DFS traversals — visit every node, track path and extrema |
| 3 | Navigate to a subtree, *then* traverse |
| 4 | Walk down following an external string, tracking state along the way |
| 5 | Mutation harder than insert: pruning shared structure on delete |
| 6 | Augment nodes with extra info to make queries faster |
| 7 | Branching recursion (wildcard expansion) |
| 8 | Trie used as a sub-procedure inside another algorithm (segmentation) |
| 9 | Domain shift: trie over bits instead of characters |
| 10 | Multi-feature, stateful, or backtracking-heavy uses |

## Conventions

Pick a node representation and stick with it. The standard one is

```python
class TrieNode:
    def __init__(self):
        self.children = {}    # char -> TrieNode
        self.is_end = False
```

"The trie" means a `TrieNode` you treat as the root. The bit-trie problems in level 9 will use a different node shape — that's noted there.

Edge cases worth keeping in your peripheral vision throughout: the empty string, querying a word not in the trie, queries longer than anything in the trie, prefixes that are not complete words, and the empty trie.

---

## [ ] Level 1 — Build and lookup

- [ ] **1a. `insert(root, word)`** — Status:

Insert `word` into the trie rooted at `root`. Inserting the same word twice should not create a duplicate path.

- [ ] **1b. `search(root, word)`** — Status:

Return `True` iff `word` was inserted (and not deleted). The terminal flag is what distinguishes a word from a strict prefix of one.

- [ ] **1c. `starts_with(root, prefix)`** — Status:

Return `True` iff some inserted word has `prefix` as a prefix. The terminal flag is irrelevant here.

---

## [ ] Level 2 — Full traversals

Now you visit nodes you didn't navigate to via a known string. The skill is DFS over the whole trie, often carrying the current path.

- [ ] **2a. `count_words(root)`** — Status:

Return the number of distinct words currently in the trie.

- [ ] **2b. `all_words(root)`** — Status:

Return a list of all words in the trie. The order is up to you (lexicographic falls out naturally if you visit children in sorted-key order).

- [ ] **2c. `longest_word(root)`** — Status:

Return the longest word in the trie. Tie-break however you like, but state your rule in a comment.

---

## [ ] Level 3 — Navigate, then traverse

Same DFS skill as level 2, but starting from a node deep in the trie rather than the root.

- [ ] **3a. `count_words_with_prefix(root, prefix)`** — Status:

Number of words in the trie that begin with `prefix`. If the prefix is not present at all, the answer is 0.

- [ ] **3b. `all_words_with_prefix(root, prefix)`** — Status:

List the words. Each returned word should be the *full* word, not just the suffix below the prefix.

---

## [ ] Level 4 — Walking with state

An external string drives the walk; you maintain bookkeeping along the way. The recurring question is *what do I remember as I descend, and when do I commit to it*.

- [ ] **4a. `longest_word_prefix_of(root, query)`** — Status:

Return the longest word in the trie that is a prefix of `query`, or `None` if no word in the trie is a prefix of `query`.

Example: trie contains `{"cat", "cattle", "ratchet"}`, query `"cattlepuss"` → `"cattle"`. Query `"car"` → `None` (neither `"c"`, `"ca"`, nor `"car"` is itself a complete word in the trie).

- [ ] **4b. `all_word_prefixes_of(root, query)`** — Status:

Return the list of all words in the trie that are prefixes of `query`, in increasing length.

Example: same trie, query `"cattlepuss"` → `["cat", "cattle"]`.

- [ ] **4c. `replace_words(root, sentence)`** — Status:

The trie holds a dictionary of "root words". `sentence` is a space-separated string. For each word in the sentence, if any prefix of that word is in the trie, replace it with the *shortest* such prefix; otherwise leave it unchanged. Return the modified sentence.

Example: trie = `{"cat", "bat", "rat"}`, sentence = `"the cattle was rattled by the battery"` → `"the cat was rat by the bat"`.

---

## [ ] Level 5 — Deletion

- [ ] **5a. `delete(root, word)`** — Status:

Remove `word` from the trie if present. After the call: `search(root, word)` returns `False`; any other word that shared a prefix with `word` is unaffected; no childless, non-terminal nodes are left dangling on what used to be `word`'s path; if `word` was not present, the trie is unchanged.

Cases worth thinking through *before* you code (try to enumerate your own list before reading mine): `word` shares its full path with another, longer word; `word` has a tail of nodes no other word uses; `word` is itself a prefix of another word in the trie; another word is a prefix of `word`; `word` is not in the trie at all.

---

## [ ] Level 6 — Augmented tries

One small extension to the node enables much faster queries and a new class of operations.

- [ ] **6a. Augmented insert and `count_with_prefix_fast(root, prefix)`** — Status:

Add a field `word_count` to each node, defined as the number of complete words at or below that node. Modify `insert` to maintain this on each call. Then implement `count_with_prefix_fast` so it runs in O(|prefix|) regardless of how many words sit under the prefix. Compare with your level-3a implementation: where did the work go?

- [ ] **6b. `kth_lex_word(root, k)`** — Status:

Using the `word_count` augmentation, return the `k`-th word in lexicographic order (1-indexed). If `k` exceeds the number of words in the trie, return `None`. The traversal should *descend*, never enumerate: at each level, the augmentation lets you decide which child to step into based on how many words sit under each.

---

## [ ] Level 7 — Wildcard search

Branching recursion: the search may fork at certain characters in the query.

- [ ] **7a. `search_wildcard(root, pattern)`** — Status:

`pattern` is a string that may contain `.`, which matches any single character. Return `True` iff some word in the trie matches the pattern exactly (length must match too).

Example: trie = `{"cat", "car", "dog"}`. Pattern `"c.t"` → `True`; pattern `"c..s"` → `False` (no length-4 words); pattern `".og"` → `True`.

- [ ] **7b. `find_words_matching(root, pattern)`** — Status:

Same wildcard rules; return the list of all matching words.

---

## [ ] Level 8 — Trie + segmentation

Trie used as a sub-procedure inside a larger search over an input string.

- [ ] **8a. `word_break(root, s)`** — Status:

Return `True` iff `s` can be partitioned into a sequence of words all present in the trie. The empty string returns `True` (the empty partition).

Example: trie = `{"apple", "pen", "applepen"}`, `s = "applepenapple"` → `True` (e.g. `"apple" "pen" "apple"`). `s = "pineapplepenapple"` → `False`.

- [ ] **8b. `all_word_breaks(root, s)`** — Status:

Return all valid space-separated segmentations of `s`.

Example: trie = `{"cat", "cats", "and", "sand", "dog"}`, `s = "catsanddog"` → `["cat sand dog", "cats and dog"]`.

---

## [ ] Level 9 — Bit trie

Same data structure, different alphabet. Each node has at most two children, indexed `0` and `1`. For these problems integers are treated as fixed-width bit strings — assume 32 bits, most-significant bit first.

A reasonable node shape:

```python
class BitNode:
    def __init__(self):
        self.children = [None, None]   # index 0 or 1
```

- [ ] **9a. `BitTrie` with `insert(value)` and `max_xor_with(query)`** — Status:

Implement a class with two methods. `insert(value)` adds a 32-bit non-negative integer to the trie. `max_xor_with(query)` returns the maximum value of `value XOR query` over all inserted values. The walk is greedy: at each bit position from MSB to LSB, prefer the child whose bit *differs* from the corresponding bit of `query`; fall back to the other child only if that path doesn't exist.

- [ ] **9b. `max_xor_pair(values)`** — Status:

Given a list of non-negative integers, return the maximum XOR over all pairs `(values[i], values[j])` with `i != j`. Use 9a as a sub-procedure: scan once, inserting as you go and querying `max_xor_with` against each value seen so far.

---

## [ ] Level 10 — Capstones

- [ ] **10a. `AutocompleteSystem`** — Status:

A stateful object that processes a stream of characters and returns the top-3 most frequent matching past sentences after each character.

Constructor: `AutocompleteSystem(sentences, frequencies)` — equal-length lists; sentence `i` has been "submitted" `frequencies[i]` times.

Method: `input(c)` — `c` is a single character. If `c == '#'`, the user has finished a sentence: increment that sentence's count (creating the entry if new), reset the input buffer, and return `[]`. Otherwise, append `c` to the buffer and return up to three sentences from the dictionary that begin with the current buffer, ordered by frequency descending, then lexicographically ascending. If fewer than three match, return all of them.

Tries fit naturally because each `#`-terminated input both queries and updates the dictionary, and successive non-`#` `input(c)` calls walk progressively further down the same path — which lets you cache the current node between calls.

- [ ] **10b. `word_squares(words)`** — Status:

A *word square* is a `k × k` grid of letters where the `i`-th row equals the `i`-th column for every `i` in `0..k-1` — so reading across or down gives the same set of words, in the same order. Given a list of unique words all of length `k`, return all word squares that can be formed using the words from the list. Each word may be used more than once across different squares but not more than once within a single square.

Example: words = `["area", "lead", "wall", "lady", "ball"]`. One valid square:

```
b a l l
a r e a
l e a d
l a d y
```

Trie indexed on the input words supports the inner loop: while filling row `i`, the prefix the row's word must have is determined by the first `i` letters of rows `0..i-1` (read column-wise, since rows must equal columns). Find all words sharing that prefix using your level-3b primitive, try each in turn, recurse, backtrack.
