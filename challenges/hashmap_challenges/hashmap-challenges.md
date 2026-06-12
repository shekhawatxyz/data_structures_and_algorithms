# Hashmap Programming Challenges

_Problems: 16._

A graduated sequence of problems for understanding, programming, and manipulating hashmaps (Python `dict`). Work through them in order — each builds on techniques developed in the previous ones.

## Ground rules

- Use only `dict` and its standard methods (`d[k]`, `d.get(k, default)`, `d.setdefault(...)`, `k in d`, `d.items()`, `del d[k]`, etc.) plus basic Python primitives (`list`, `str`, `tuple`, `set`, `int`, and `random` where indicated). **No `collections.Counter` and no `collections.defaultdict`** for the first solve — write the patterns out yourself; the point is to feel the mechanics. After you've solved a problem cleanly, you may, if you like, refactor with `defaultdict` for comparison.
- Two problems use a **sliding window** and two use **prefix sums**. These are general techniques rather than separate data structures; the hashmap remains the load-bearing piece. Everything else is pure hashmap work.

---

- [ ] **1. `build_phonebook`** — Status:

```python
def build_phonebook(entries: list[tuple[str, str]]) -> dict[str, str]:
```

Given a list of `(name, number)` tuples, return a dictionary mapping each name to its number. If the same name appears more than once, the later number takes precedence.

Examples:
- `build_phonebook([("Alice", "555-1234"), ("Bob", "555-9876")])` → `{"Alice": "555-1234", "Bob": "555-9876"}`
- `build_phonebook([("Alice", "555-1234"), ("Alice", "555-0000")])` → `{"Alice": "555-0000"}`
- `build_phonebook([])` → `{}`

---

- [ ] **2. `char_count`** — Status:

```python
def char_count(s: str) -> dict[str, int]:
```

Return a dictionary mapping each character in `s` to the number of times it appears.

Examples:
- `char_count("hello")` → `{"h": 1, "e": 1, "l": 2, "o": 1}`
- `char_count("")` → `{}`
- `char_count("aaa")` → `{"a": 3}`

---

- [ ] **3. `first_unique_char`** — Status:

```python
def first_unique_char(s: str) -> int:
```

Return the index of the first character in `s` that appears exactly once. If no such character exists, return `-1`.

Examples:
- `first_unique_char("leetcode")` → `0`
- `first_unique_char("loveleetcode")` → `2`
- `first_unique_char("aabb")` → `-1`
- `first_unique_char("")` → `-1`

---

- [ ] **4. `most_frequent_element`** — Status:

```python
def most_frequent_element(nums: list[int]) -> int:
```

Return the element of `nums` that appears most often. If there is a tie, return the one whose first occurrence is earliest in `nums`. The list is non-empty.

Examples:
- `most_frequent_element([1, 2, 2, 3, 3, 3])` → `3`
- `most_frequent_element([4, 4, 1, 1])` → `4`
- `most_frequent_element([7])` → `7`

---

- [ ] **5. `is_anagram`** — Status:

```python
def is_anagram(s: str, t: str) -> bool:
```

Return `True` if `t` contains exactly the same characters as `s` with the same frequencies, regardless of order.

Examples:
- `is_anagram("listen", "silent")` → `True`
- `is_anagram("hello", "world")` → `False`
- `is_anagram("a", "ab")` → `False`
- `is_anagram("", "")` → `True`

---

- [ ] **6. `two_sum`** — Status:

```python
def two_sum(nums: list[int], target: int) -> list[int]:
```

Given a list of integers and a target, return the indices `[i, j]` (in any order, with `i != j`) of two numbers such that `nums[i] + nums[j] == target`. You may assume exactly one solution exists.

Examples:
- `two_sum([2, 7, 11, 15], 9)` → `[0, 1]`
- `two_sum([3, 2, 4], 6)` → `[1, 2]`
- `two_sum([3, 3], 6)` → `[0, 1]`

---

- [ ] **7. `contains_nearby_duplicate`** — Status:

```python
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
```

Return `True` if there exist two distinct indices `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

Examples:
- `contains_nearby_duplicate([1, 2, 3, 1], 3)` → `True`
- `contains_nearby_duplicate([1, 0, 1, 1], 1)` → `True`
- `contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)` → `False`

---

- [ ] **8. `word_to_indices`** — Status:

```python
def word_to_indices(words: list[str]) -> dict[str, list[int]]:
```

Given a list of words, return a dictionary mapping each distinct word to the list of indices (in ascending order) at which it appears.

Examples:
- `word_to_indices(["cat", "dog", "cat", "bird", "dog", "cat"])` → `{"cat": [0, 2, 5], "dog": [1, 4], "bird": [3]}`
- `word_to_indices([])` → `{}`
- `word_to_indices(["x"])` → `{"x": [0]}`

---

- [ ] **9. `group_by_length`** — Status:

```python
def group_by_length(words: list[str]) -> dict[int, list[str]]:
```

Group words by their length. Return a dictionary mapping each length to the list of words of that length, preserving the order in which they appeared in the input.

Examples:
- `group_by_length(["hi", "world", "go", "is", "code"])` → `{2: ["hi", "go", "is"], 5: ["world"], 4: ["code"]}`
- `group_by_length([])` → `{}`

---

- [ ] **10. `group_anagrams`** — Status:

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
```

Group words that are anagrams of each other. Return a list of groups. Within each group, words appear in the order they appeared in the input. The order of the groups themselves doesn't matter.

Examples:
- `group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])` → `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]` (groups in any order)
- `group_anagrams([""])` → `[[""]]`
- `group_anagrams(["a"])` → `[["a"]]`

---

- [ ] **11. `isomorphic_strings`** — Status:

```python
def isomorphic_strings(s: str, t: str) -> bool:
```

Two strings are *isomorphic* if there is a bijection between the characters of `s` and the characters of `t` such that replacing each character of `s` according to the mapping yields `t`. Two different characters in `s` cannot map to the same character in `t`, and a single character in `s` cannot map to two different characters in `t`. The two strings have equal length.

Examples:
- `isomorphic_strings("egg", "add")` → `True`
- `isomorphic_strings("foo", "bar")` → `False`
- `isomorphic_strings("paper", "title")` → `True`
- `isomorphic_strings("badc", "baba")` → `False`
- `isomorphic_strings("ab", "aa")` → `False`

---

- [ ] **12. `longest_substring_without_repeating`** — Status:

```python
def longest_substring_without_repeating(s: str) -> int:
```

Return the length of the longest substring of `s` that contains no repeated characters.

Examples:
- `longest_substring_without_repeating("abcabcbb")` → `3`
- `longest_substring_without_repeating("bbbbb")` → `1`
- `longest_substring_without_repeating("pwwkew")` → `3`
- `longest_substring_without_repeating("")` → `0`

---

- [ ] **13. `subarray_sum_equals_k`** — Status:

```python
def subarray_sum_equals_k(nums: list[int], k: int) -> int:
```

Return the number of contiguous, non-empty subarrays of `nums` whose elements sum to exactly `k`. Elements may be negative.

Examples:
- `subarray_sum_equals_k([1, 1, 1], 2)` → `2`
- `subarray_sum_equals_k([1, 2, 3], 3)` → `2`
- `subarray_sum_equals_k([1, -1, 1, -1], 0)` → `4`

---

- [ ] **14. `longest_subarray_with_sum_k`** — Status:

```python
def longest_subarray_with_sum_k(nums: list[int], k: int) -> int:
```

Return the length of the longest contiguous, non-empty subarray of `nums` summing to exactly `k`. If no such subarray exists, return `0`. Elements may be negative.

Examples:
- `longest_subarray_with_sum_k([1, -1, 5, -2, 3], 3)` → `4`
- `longest_subarray_with_sum_k([-2, -1, 2, 1], 1)` → `2`
- `longest_subarray_with_sum_k([1, 2, 3], 7)` → `0`

---

- [ ] **15. `LoggerRateLimiter`** — Status:

```python
class LoggerRateLimiter:
    def __init__(self): ...
    def should_print(self, timestamp: int, message: str) -> bool: ...
```

Design a logger that receives a stream of `(timestamp, message)` calls. `should_print(timestamp, message)` returns `True` if the message has not been logged in the last 10 seconds — that is, if the same message was last logged at `t_prev`, the next call with that message returns `True` only when `timestamp - t_prev >= 10`. Otherwise it returns `False`. Timestamps are non-decreasing.

A returned `True` counts as logging the message; a returned `False` does not.

Example:
```python
logger = LoggerRateLimiter()
logger.should_print(1, "foo")    # True
logger.should_print(2, "bar")    # True
logger.should_print(3, "foo")    # False
logger.should_print(8, "bar")    # False
logger.should_print(10, "foo")   # False
logger.should_print(11, "foo")   # True
```

---

- [ ] **16. `RandomizedSet`** — Status:

```python
class RandomizedSet:
    def __init__(self): ...
    def insert(self, val: int) -> bool: ...
    def remove(self, val: int) -> bool: ...
    def get_random(self) -> int: ...
```

Design a data structure supporting all three operations in **O(1) average time**:

- `insert(val)`: insert `val` if not already present; return `True` if newly inserted, else `False`.
- `remove(val)`: remove `val` if present; return `True` if removed, else `False`.
- `get_random()`: return a uniformly random element from the current set. You may assume the set is non-empty when this is called.

You may use the `random` module. Alongside the dict you may use a list as auxiliary storage. The hard part is satisfying the O(1) constraint for *all three* operations — note that `list.remove(x)` and `del lst[i]` for non-final `i` are O(n) and so are forbidden by the constraint. `list.append(x)` and `list.pop()` (no index, popping the last element) are O(1) and are fine.

Example:
```python
rs = RandomizedSet()
rs.insert(1)        # True
rs.remove(2)        # False (2 not present)
rs.insert(2)        # True
rs.get_random()     # 1 or 2, each with probability 1/2
rs.remove(1)        # True
rs.insert(2)        # False (already present)
rs.get_random()     # 2
```
