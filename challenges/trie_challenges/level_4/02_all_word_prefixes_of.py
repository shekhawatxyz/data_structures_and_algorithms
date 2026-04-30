# Level 4b - all_word_prefixes_of
# Return all words in the trie that are prefixes of the query.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 4b. `all_word_prefixes_of(root, query)`
#
# Return the list of all words in the trie that are prefixes of `query`, in increasing length.
#
# Example: same trie, query `"cattlepuss"` → `["cat", "cattle"]`.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def all_word_prefixes_of(root, query):
    raise NotImplementedError('Implement all_word_prefixes_of(root, query).')
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


def test_01_pedagogy_multiple_prefixes():
    root = _build_trie(["cat", "cattle", "ratchet"])
    _assert_equal(all_word_prefixes_of(root, "cattlepuss"), ["cat", "cattle"],
                  "'cat' and 'cattle' are both prefixes of 'cattlepuss'.")


def test_02_pedagogy_no_prefixes():
    root = _build_trie(["dog", "deer"])
    _assert_equal(all_word_prefixes_of(root, "cat"), [],
                  "No words are prefixes of 'cat'.")


def test_03_boundaries_query_shorter_than_words():
    root = _build_trie(["hello"])
    _assert_equal(all_word_prefixes_of(root, "he"), [],
                  "No word is a prefix of 'he' (only 'hello' which is longer).")


def test_04_interactions_nested_prefixes():
    root = _build_trie(["a", "ab", "abc", "abcd"])
    _assert_equal(all_word_prefixes_of(root, "abcde"), ["a", "ab", "abc", "abcd"],
                  "All four words are prefixes of 'abcde'.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: multiple prefixes", test_01_pedagogy_multiple_prefixes),
        ("pedagogy: no prefixes", test_02_pedagogy_no_prefixes),
        ("boundaries: query shorter than words", test_03_boundaries_query_shorter_than_words),
        ("interactions: nested prefixes", test_04_interactions_nested_prefixes),
    ]
    _run_all_tests(TEST_CASES)
