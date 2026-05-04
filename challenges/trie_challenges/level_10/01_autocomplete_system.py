# Level 10a - AutocompleteSystem
# A stateful autocomplete system using a trie.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 10a. `AutocompleteSystem`
#
# A stateful object that processes a stream of characters and returns the top-3 most frequent matching past sentences after each character.
#
# Constructor: `AutocompleteSystem(sentences, frequencies)` — equal-length lists; sentence `i` has been "submitted" `frequencies[i]` times.
#
# Method: `input(c)` — `c` is a single character. If `c == '#'`, the user has finished a sentence: increment that sentence's count (creating the entry if new), reset the input buffer, and return `[]`. Otherwise, append `c` to the buffer and return up to three sentences from the dictionary that begin with the current buffer, ordered by frequency descending, then lexicographically ascending. If fewer than three match, return all of them.
#
# Tries fit naturally because each `#`-terminated input both queries and updates the dictionary, and successive non-`#` `input(c)` calls walk progressively further down the same path — which lets you cache the current node between calls.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0


class AutocompleteSystem:
    def __init__(self, sentences, frequencies):
        raise NotImplementedError('Implement AutocompleteSystem.__init__(sentences, frequencies).')

    def input(self, c):
        raise NotImplementedError('Implement AutocompleteSystem.input(c).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


def _assert_equal(actual, expected, context):
    if actual != expected:
        raise AssertionError(f"{context} Expected {expected!r}, got {actual!r}.")


def _run_test(name, test_fn):
    try:
        test_fn()
    except NotImplementedError as exc:
        print(f"[FAIL] {name}: Function is not implemented yet ({exc}).")
        return False
    except AssertionError as exc:
        print(f"[FAIL] {name}: {exc}")
        return False
    except Exception as exc:
        print(f"[FAIL] {name}: Unexpected {type(exc).__name__}: {exc}")
        return False

    print(f"[PASS] {name}")
    return True


def _run_all_tests(test_cases):
    passed = 0
    total = len(test_cases)

    for name, fn in test_cases:
        if _run_test(name, fn):
            passed += 1

    print(f"\nPassed {passed}/{total} tests.")
    if passed != total:
        raise SystemExit(1)


def test_01_pedagogy_basic_input():
    ac = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
    result = ac.input("i")
    _assert_equal(result, ["i love you", "island", "i love leetcode"],
                  "Top 3 starting with 'i' by frequency.")


def test_02_pedagogy_narrowing():
    ac = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
    ac.input("i")
    result = ac.input(" ")
    _assert_equal(result, ["i love you", "i love leetcode"],
                  "After 'i ', only 'i love...' sentences match.")


def test_03_pedagogy_hash_terminates():
    ac = AutocompleteSystem(["hello"], [1])
    ac.input("h")
    result = ac.input("#")
    _assert_equal(result, [], "'#' finishes input and returns [].")


def test_04_boundaries_new_sentence():
    ac = AutocompleteSystem([], [])
    ac.input("a")
    ac.input("b")
    ac.input("#")
    result = ac.input("a")
    _assert_equal(result, ["ab"], "After entering 'ab#', 'ab' should appear for prefix 'a'.")


def test_05_interactions_frequency_update():
    ac = AutocompleteSystem(["abc", "abd"], [1, 1])
    # Type 'abc#' to increment abc's count
    for c in "abc":
        ac.input(c)
    ac.input("#")
    # Now abc has count 2, abd has count 1
    result = ac.input("a")
    _assert_equal(result, ["abc", "abd"], "'abc' should now sort before 'abd' by higher frequency.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic input", test_01_pedagogy_basic_input),
        ("pedagogy: narrowing", test_02_pedagogy_narrowing),
        ("pedagogy: hash terminates", test_03_pedagogy_hash_terminates),
        ("boundaries: new sentence", test_04_boundaries_new_sentence),
        ("interactions: frequency update", test_05_interactions_frequency_update),
    ]
    _run_all_tests(TEST_CASES)
