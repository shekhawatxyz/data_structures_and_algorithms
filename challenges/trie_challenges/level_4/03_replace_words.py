# Level 4c - replace_words
# Replace words in a sentence with the shortest matching root from the trie.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 4c. `replace_words(root, sentence)`
#
# The trie holds a dictionary of "root words". `sentence` is a space-separated string. For each word in the sentence, if any prefix of that word is in the trie, replace it with the *shortest* such prefix; otherwise leave it unchanged. Return the modified sentence.
#
# Example: trie = `{"cat", "bat", "rat"}`, sentence = `"the cattle was rattled by the battery"` → `"the cat was rat by the bat"`.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def replace_words(root, sentence):
    raise NotImplementedError('Implement replace_words(root, sentence).')
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
    root = _build_trie(["cat", "bat", "rat"])
    _assert_equal(replace_words(root, "the cattle was rattled by the battery"),
                  "the cat was rat by the bat",
                  "Each word should be replaced by shortest matching root.")


def test_02_pedagogy_no_replacement():
    root = _build_trie(["cat"])
    _assert_equal(replace_words(root, "dog run fast"), "dog run fast",
                  "No word has a root prefix; sentence unchanged.")


def test_03_boundaries_empty_sentence():
    root = _build_trie(["cat"])
    _assert_equal(replace_words(root, ""), "", "Empty sentence stays empty.")


def test_04_interactions_shortest_root():
    root = _build_trie(["a", "ab", "abc"])
    _assert_equal(replace_words(root, "abcdef"), "a",
                  "Shortest root 'a' should be used, not 'ab' or 'abc'.")


def test_05_interactions_word_is_exact_root():
    root = _build_trie(["cat"])
    _assert_equal(replace_words(root, "cat"), "cat",
                  "Word that is exactly a root stays as the root.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("pedagogy: no replacement", test_02_pedagogy_no_replacement),
        ("boundaries: empty sentence", test_03_boundaries_empty_sentence),
        ("interactions: shortest root", test_04_interactions_shortest_root),
        ("interactions: word is exact root", test_05_interactions_word_is_exact_root),
    ]
    _run_all_tests(TEST_CASES)
