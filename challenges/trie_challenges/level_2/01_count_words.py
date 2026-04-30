# Level 2a - count_words
# Return the number of distinct words in the trie.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 2a. `count_words(root)`
#
# Return the number of distinct words currently in the trie.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def count_words(root):
    raise NotImplementedError('Implement count_words(root).')
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


def _assert_true(condition, context):
    if not condition:
        raise AssertionError(context)


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


def test_01_pedagogy_several_words():
    root = _build_trie(["cat", "car", "dog"])
    _assert_equal(count_words(root), 3, "Three words inserted should give count 3.")


def test_02_boundaries_empty_trie():
    root = TrieNode()
    _assert_equal(count_words(root), 0, "Empty trie has 0 words.")


def test_03_boundaries_single_word():
    root = _build_trie(["hello"])
    _assert_equal(count_words(root), 1, "One word inserted should give count 1.")


def test_04_interactions_shared_prefix():
    root = _build_trie(["app", "apple", "application"])
    _assert_equal(count_words(root), 3, "Three words with shared prefix: count 3.")


def test_05_interactions_includes_empty_string():
    root = _build_trie(["", "a", "ab"])
    _assert_equal(count_words(root), 3, "Empty string counts as a word.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: several words", test_01_pedagogy_several_words),
        ("boundaries: empty trie", test_02_boundaries_empty_trie),
        ("boundaries: single word", test_03_boundaries_single_word),
        ("interactions: shared prefix", test_04_interactions_shared_prefix),
        ("interactions: includes empty string", test_05_interactions_includes_empty_string),
    ]
    _run_all_tests(TEST_CASES)
