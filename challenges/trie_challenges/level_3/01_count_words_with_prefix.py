# Level 3a - count_words_with_prefix
# Count how many words begin with a given prefix.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 3a. `count_words_with_prefix(root, prefix)`
#
# Number of words in the trie that begin with `prefix`. If the prefix is not present at all, the answer is 0.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def count_words_with_prefix(root, prefix):
    raise NotImplementedError('Implement count_words_with_prefix(root, prefix).')
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


def test_01_pedagogy_shared_prefix():
    root = _build_trie(["app", "apple", "ape", "bat"])
    _assert_equal(count_words_with_prefix(root, "ap"), 3,
                  "'app', 'apple', 'ape' all start with 'ap'.")


def test_02_pedagogy_no_match():
    root = _build_trie(["cat", "car"])
    _assert_equal(count_words_with_prefix(root, "dog"), 0,
                  "No words start with 'dog'.")


def test_03_boundaries_empty_prefix():
    root = _build_trie(["a", "b", "c"])
    _assert_equal(count_words_with_prefix(root, ""), 3,
                  "Empty prefix matches all words.")


def test_04_boundaries_prefix_equals_word():
    root = _build_trie(["cat", "catalog"])
    _assert_equal(count_words_with_prefix(root, "cat"), 2,
                  "'cat' and 'catalog' both start with 'cat'.")


def test_05_interactions_prefix_longer_than_words():
    root = _build_trie(["hi"])
    _assert_equal(count_words_with_prefix(root, "high"), 0,
                  "Prefix longer than any word should return 0.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: shared prefix", test_01_pedagogy_shared_prefix),
        ("pedagogy: no match", test_02_pedagogy_no_match),
        ("boundaries: empty prefix", test_03_boundaries_empty_prefix),
        ("boundaries: prefix equals word", test_04_boundaries_prefix_equals_word),
        ("interactions: prefix longer than words", test_05_interactions_prefix_longer_than_words),
    ]
    _run_all_tests(TEST_CASES)
