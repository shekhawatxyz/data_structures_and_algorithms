# Graduated Stack Challenges

_Problems: 34._

A sequence of programming challenges for learning stacks in Python. Each level is a cluster of problems that build toward a key idea, with interstitial steps to make the progression gradual.

---

## Level 1 — Implement the Thing

**Core demand:** Understanding the stack ADT itself.

- [x] **1a.** — Status:

Write a `Stack` class from scratch using a Python list internally. Support `push(item)`, `pop()`, `peek()`, `is_empty()`, and `size()`. Raise an appropriate error when popping or peeking an empty stack.

- [x] **1b.** — Status:

Write a small test script that creates a stack, pushes the integers 1 through 5, then pops and prints them all. Predict the output before running it. Verify your prediction.

- [x] **1c.** — Status:

Add a `__str__` method to your `Stack` class that prints the stack contents from top to bottom (so you can see what's in it at any point). Then write a script that interleaves pushes and pops — e.g., push 1, push 2, pop, push 3, pop, pop — printing the stack after each operation. Predict the full output before running.

---

## Level 2 — Single-Pass, Uniform Use

**Core demand:** The basic push-everything-then-pop-everything pattern.

- [x] **2a.** — Status:

Write a function that takes a string and returns it reversed, using only a stack. (Push every character, then pop them all.)

- [x] **2b.** — Status:

Write a function that takes a list of integers and checks whether it is a palindrome, using only a stack. Do *not* reverse the list directly — use the stack to produce the reversed sequence and compare element by element.

- [x] **2c.** — Status:

Write a function that takes a positive integer and returns its binary representation as a string, using a stack. (Repeatedly divide by 2, push the remainders, then pop them all to form the binary string.)

---

## Level 3 — Conditional Push/Pop

**Core demand:** Push/pop decisions depend on what you encounter.

- [x] **3a.** — Status:

Write a function that takes a string of parentheses — only `(` and `)` — and returns whether they are balanced. Think carefully about what "balanced" means: every opener has a corresponding closer *in the right order*, and there are no unmatched closers or openers.

- [x] **3b.** — Status: shaky

Write a function that takes a string (of any characters, not just parentheses) and removes all adjacent duplicates, using a stack. For example: `"abbaca"` → `"ca"`. (Process each character: if it matches the top of the stack, pop; otherwise push. Whatever remains in the stack is the result.)

- [x] **3c.** — Status: hard

Write a function that takes a string containing `(` and `)` among other characters and returns the string with the minimum number of parentheses removed to make it valid. For example: `"a(b(c)d"` → `"ab(c)d"` (one possible answer). Use a stack to identify which parentheses are unmatched, then build the output string excluding them.

---

## Level 4 — Matching Across Types

**Core demand:** Pop decisions require inspecting and comparing what's on top.

- [x] **4a.** — Status:

Extend your balanced-parentheses checker from 3a to handle three types: `()`, `[]`, and `{}`. Each closer must match the most recently unmatched opener of the *correct* type. For example: `"([{}])"` is valid; `"([)]"` is not.

- [x] **4b.** — Status:

Write a function that takes a string of brackets like the above, and if it is *invalid*, returns the index of the *first* offending character (either the first unmatched closer or, if all closers matched but openers remain, the index of the earliest unmatched opener). If valid, return `-1`.

- [x] **4c.** — Status:

Write a function that takes an incomplete bracket string and returns the *minimum* string of closing brackets to append to make it valid — or reports that it's already invalid and unfixable. For example: `"({["` → `"]})"`. But `"({]"` → invalid, can't be fixed by appending.

---

## Level 5 — Stack as Computation Engine

**Core demand:** The stack holds intermediate computed values; you operate on popped values and push results back.

- [x] **5a.** — Status:

Write a function that evaluates a postfix (reverse Polish notation) expression. Input is a list of tokens like `["3", "4", "+", "2", "*"]` → `14`. Support `+`, `-`, `*`, `/` (integer division, truncating toward zero).

- [x] **5b.** — Status:

Extend your evaluator to support a unary negation token, say `"neg"`, which pops the top value and pushes its negation. For example: `["5", "neg", "3", "+"]` → `-2`. This forces you to handle operators with different arities.

- [x] **5c.** — Status:

Add support for a `"dup"` operator (duplicates the top of the stack) and a `"swap"` operator (swaps the top two elements). Evaluate: `["3", "dup", "*", "4", "swap", "-"]`. Predict the result before running it. These stack-manipulation operations are how real stack-based languages (Forth, PostScript) and virtual machines work.

---

## Level 6 — Precedence and Associativity

**Core demand:** When to pop is governed by comparing precedence of the incoming operator vs. the stack top.

- [x] **6a.** — Status:

Start simple: write a function that converts a *fully parenthesised* infix expression to postfix. By "fully parenthesised" I mean every operation is wrapped: `"( ( 3 + 4 ) * 2 )"`. This is easier because the parentheses already tell you the structure — you don't need precedence rules yet. Tokens are space-separated. Use a stack.

- [x] **6b.** — Status:

Now implement the full shunting-yard algorithm: convert an infix expression (with the standard operators `+`, `-`, `*`, `/` and parentheses, but *not* necessarily fully parenthesised) to postfix. You will need a precedence table and a rule for left-associativity. Tokens are given as a list of strings.

- [x] **6c.** — Status:

Chain your 6b converter with your 5a evaluator to evaluate infix expressions end-to-end. Test on: `"3 + 4 * 2 / ( 1 - 5 )"` → should give `1` (with integer division).

- [x] **6d.** — Status:

Extend your shunting-yard to handle right-associative exponentiation `^`. For example, `"2 ^ 3 ^ 2"` should be treated as `2 ^ (3 ^ 2) = 512`, not `(2 ^ 3) ^ 2 = 64`. The key: the only thing that changes is the comparison — for right-associative operators, you pop only when the stack-top has *strictly greater* precedence, not greater-or-equal.

---

## Level 7 — Auxiliary Stack as Design Constraint

**Core demand:** Figure out what auxiliary information to maintain and keep it synchronised.

- [x] **7a.** — Status:

Design a `MaxStack` class that supports `push`, `pop`, `peek`, and `get_max` (returns the current maximum element), all in O(1) time. You may use additional stacks but no other data structures. (Hint: think about what information you need to preserve when you push, and what you need to restore when you pop.)

- [x] **7b.** — Status:

Now design a `MinStack` with the same interface but for `get_min`. If you did 7a, this is almost identical — but do it from scratch to reinforce the pattern. Then think: can you reduce the space used by the auxiliary stack? (Hint: you don't need to push onto the auxiliary stack on *every* push.)

- [x] **7c.** — Status:

Using only stacks, implement a queue. That is, build a class `StackQueue` supporting `enqueue(item)` and `dequeue()` (FIFO order), using two stacks internally. Each individual `enqueue` and `dequeue` should be O(1) *amortised*. Think about when to transfer elements from one stack to the other.

---

## Level 8 — Monotonic Stack Reasoning

**Core demand:** Maintain a stack invariant (monotonicity) and reason about what the stack *represents*.

- [x] **8a.** — Status:

Given an array of daily temperatures (integers), return an array where each element tells you how many days you'd have to wait for a warmer temperature. If no warmer day exists, output `0`. Example: `[73, 74, 75, 71, 69, 72, 76, 73]` → `[1, 1, 4, 2, 1, 1, 0, 0]`. Use a stack. (Hint: what should the stack store — values, indices, or both? What invariant should it maintain?)

- [x] **8b.** — Status:

Given an array of integers, for each element, find the *next greater element* — i.e., the first element to its right that is strictly larger. If none exists, output `-1`. Example: `[4, 2, 6, 1, 3]` → `[6, 6, -1, 3, -1]`. Do this in O(n).

- [x] **8c.** — Status:

Variation: for each element, find the *previous greater element* — the nearest element to its *left* that is strictly larger. Output `-1` if none. Example: `[4, 2, 6, 1, 3]` → `[-1, 4, -1, 6, 6]`. Same O(n) constraint. Notice how the direction change affects when you process elements vs. when you read answers off the stack.

- [x] **8d.** — Status:

Given a circular array (the element after the last is the first), find the next greater element for each position. Example: `[1, 2, 1]` → `[2, -1, 2]` (the `1` at index 2 wraps around to find `2` at index 0). (Hint: a standard trick for circular arrays — iterate through the array twice.)

---

## Level 9 — Hard Monotonic Stack

**Core demand:** Subtler invariant, boundary reasoning on each pop, tricky edge cases.

- [x] **9a.** — Status:

Warm-up: given an array of non-negative integers representing heights, and a fixed width of 1 per bar, find the area of the largest rectangle of height `min(array)` spanning the *entire* array. This is trivial (just `min * len`) — but phrase it to yourself as: "the rectangle constrained to use all bars." Now: what if you could pick any *contiguous* subarray? The rectangle's height is the minimum in that subarray, and its width is the subarray's length. Write a brute-force O(n²) solution for this (for each bar, expand left and right to find how far it can extend as the minimum). Verify on `[2, 1, 5, 6, 2, 3]` → `10`.

- [x] **9b.** — Status:

Now think about what information you'd need to compute each bar's "extent" (how far left and right it can go as the minimum) in O(n). This is exactly what a monotonic stack gives you. For each element, use a stack to find the index of the *nearest smaller element to the left* and the *nearest smaller element to the right*. These two arrays, combined, give you each bar's maximal rectangle. Implement this.

- [x] **9c.** — Status:

Put it all together: solve the largest rectangle in a histogram in O(n) using a single stack pass. The classic approach processes bars left to right, maintaining a stack of bars in increasing height order. When you encounter a bar shorter than the stack top, you pop and compute the area for the popped bar (using the current index and the new stack top to determine width). Handle the end-of-array case (flush the remaining stack). Test on `[2, 1, 5, 6, 2, 3]` → `10`.

- [x] **9d.** — Status:

Extension: given a binary matrix (0s and 1s) of size m × n, find the largest rectangle containing only 1s. (Hint: build a histogram for each row — treating consecutive 1s going upward as bar heights — then run your 9c solution on each row's histogram. The answer is the maximum across all rows.)

---

## Level 10 — Nested Structure with State Recovery

**Core demand:** The stack saves and restores entire computation state across nesting levels.

- [x] **10a.** — Status:

Write a function that takes a nested list represented as a string like `"[1,[2,3],[4,[5,6]]]"` and returns the actual nested Python list. Use a stack: when you see `[`, push a new empty list; when you see `]`, pop the completed list and append it to whatever is now on top. Numbers between commas get appended to the current top-of-stack list.

- [x] **10b.** — Status:

Write a function that "flattens" nested brackets with multipliers, but *only one level deep* (no nesting). Format: `"3[ab]2[c]"` → `"ababababcc"`. Use a stack to handle the boundary between "outside" characters and "inside a bracket group" — when you see a digit followed by `[`, push your current string onto the stack and start a fresh one; when you see `]`, pop and combine.

- [x] **10c.** — Status:

Now handle full nesting: `"3[a2[c]]"` → `"accaccacc"` and `"2[abc]3[cd]ef"` → `"abcabccdcdcdef"`. The stack must save and restore the *entire state* of your in-progress computation (the string built so far *and* the repeat count) when entering/exiting a nesting level. You are essentially using the stack to simulate a call stack.

- [x] **10d.** — Status:

Write a simple calculator that handles nested parenthesised expressions with `+` and `*` (no precedence needed since parentheses are explicit), e.g., `"2*(3+4*(2+1))"` → `30`. Use a stack to save the current accumulated value and pending operator when you enter a `(`, and restore and combine when you hit `)`. This is the same state-save/restore pattern as 10c, but applied to arithmetic instead of string building.
