# Level 6b - kth_lex_word
# Return the k-th word in lexicographic order using augmented word_count.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 6b. `kth_lex_word(root, k)`
#
# Using the `word_count` augmentation, return the `k`-th word in lexicographic order (1-indexed). If `k` exceeds the number of words in the trie, return `None`. The traversal should *descend*, never enumerate: at each level, the augmentation lets you decide which child to step into based on how many words sit under each.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word_count = 0


def kth_lex_word(root, k):
    raise NotImplementedError('Implement kth_lex_word(root, k).')
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


def _build_augmented_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        node.word_count += 1
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.word_count += 1
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
    root = _build_augmented_trie(["apple", "app", "bat", "ball"])
    _assert_equal(kth_lex_word(root, 1), "app", "1st lex word is 'app'.")
    _assert_equal(kth_lex_word(root, 2), "apple", "2nd lex word is 'apple'.")
    _assert_equal(kth_lex_word(root, 3), "ball", "3rd lex word is 'ball'.")
    _assert_equal(kth_lex_word(root, 4), "bat", "4th lex word is 'bat'.")


def test_02_boundaries_k_too_large():
    root = _build_augmented_trie(["cat"])
    _assert_equal(kth_lex_word(root, 2), None, "Only 1 word; k=2 returns None.")


def test_03_boundaries_k_equals_one_single_word():
    root = _build_augmented_trie(["zebra"])
    _assert_equal(kth_lex_word(root, 1), "zebra", "Only word is 'zebra'.")


def test_04_interactions_shared_prefix():
    root = _build_augmented_trie(["a", "ab", "abc"])
    _assert_equal(kth_lex_word(root, 1), "a", "1st is 'a'.")
    _assert_equal(kth_lex_word(root, 2), "ab", "2nd is 'ab'.")
    _assert_equal(kth_lex_word(root, 3), "abc", "3rd is 'abc'.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("boundaries: k too large", test_02_boundaries_k_too_large),
        ("boundaries: single word", test_03_boundaries_k_equals_one_single_word),
        ("interactions: shared prefix", test_04_interactions_shared_prefix),
    ]
    _run_all_tests(TEST_CASES)
