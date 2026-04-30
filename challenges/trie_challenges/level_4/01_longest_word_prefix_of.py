# Level 4a - longest_word_prefix_of
# Find the longest word in the trie that is a prefix of the query.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 4a. `longest_word_prefix_of(root, query)`
#
# Return the longest word in the trie that is a prefix of `query`, or `None` if no word in the trie is a prefix of `query`.
#
# Example: trie contains `{"cat", "cattle", "ratchet"}`, query `"cattlepuss"` → `"cattle"`. Query `"car"` → `None` (neither `"c"`, `"ca"`, nor `"car"` is itself a complete word in the trie).

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def longest_word_prefix_of(root, query):
    raise NotImplementedError('Implement longest_word_prefix_of(root, query).')
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


def _build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    return root


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


def test_01_pedagogy_basic():
    root = _build_trie(["cat", "cattle", "ratchet"])
    _assert_equal(longest_word_prefix_of(root, "cattlepuss"), "cattle",
                  "'cattle' is the longest word that is a prefix of 'cattlepuss'.")


def test_02_pedagogy_no_word_prefix():
    root = _build_trie(["cat", "cattle", "ratchet"])
    _assert_equal(longest_word_prefix_of(root, "car"), None,
                  "No word in the trie is a prefix of 'car'.")


def test_03_boundaries_query_equals_word():
    root = _build_trie(["hello"])
    _assert_equal(longest_word_prefix_of(root, "hello"), "hello",
                  "Word equals query; it is a prefix of itself.")


def test_04_boundaries_empty_string_word():
    root = _build_trie(["", "a"])
    _assert_equal(longest_word_prefix_of(root, "anything"), "a" if "a" == "anything"[:1] else "",
                  "Empty string is prefix of everything.")
    # More precise test:
    root2 = _build_trie([""])
    _assert_equal(longest_word_prefix_of(root2, "xyz"), "",
                  "Empty string word is a prefix of any query.")


def test_05_interactions_multiple_prefix_words():
    root = _build_trie(["a", "ab", "abc", "abcd"])
    _assert_equal(longest_word_prefix_of(root, "abcde"), "abcd",
                  "Longest prefix word of 'abcde' is 'abcd'.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("pedagogy: no word prefix", test_02_pedagogy_no_word_prefix),
        ("boundaries: query equals word", test_03_boundaries_query_equals_word),
        ("boundaries: empty string word", test_04_boundaries_empty_string_word),
        ("interactions: multiple prefix words", test_05_interactions_multiple_prefix_words),
    ]
    _run_all_tests(TEST_CASES)
