# Level 3b - all_words_with_prefix
# List all words that begin with a given prefix.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 3b. `all_words_with_prefix(root, prefix)`
#
# List the words. Each returned word should be the *full* word, not just the suffix below the prefix.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def all_words_with_prefix(root, prefix):
    raise NotImplementedError('Implement all_words_with_prefix(root, prefix).')
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
    root = _build_trie(["app", "apple", "ape", "bat"])
    _assert_equal(sorted(all_words_with_prefix(root, "ap")),
                  ["ape", "app", "apple"],
                  "Words starting with 'ap' are 'ape', 'app', 'apple'.")


def test_02_pedagogy_no_match():
    root = _build_trie(["cat", "car"])
    _assert_equal(all_words_with_prefix(root, "dog"), [],
                  "No words start with 'dog'.")


def test_03_boundaries_empty_prefix():
    root = _build_trie(["a", "b"])
    _assert_equal(sorted(all_words_with_prefix(root, "")), ["a", "b"],
                  "Empty prefix returns all words.")


def test_04_interactions_exact_word():
    root = _build_trie(["cat", "catalog", "category"])
    _assert_equal(sorted(all_words_with_prefix(root, "cat")),
                  ["cat", "catalog", "category"],
                  "'cat' prefix matches all three words.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("pedagogy: no match", test_02_pedagogy_no_match),
        ("boundaries: empty prefix", test_03_boundaries_empty_prefix),
        ("interactions: exact word as prefix", test_04_interactions_exact_word),
    ]
    _run_all_tests(TEST_CASES)
