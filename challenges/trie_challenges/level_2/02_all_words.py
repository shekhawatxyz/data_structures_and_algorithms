# Level 2b - all_words
# Return a list of all words in the trie.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 2b. `all_words(root)`
#
# Return a list of all words in the trie. The order is up to you (lexicographic falls out naturally if you visit children in sorted-key order).

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def all_words(root):
    raise NotImplementedError('Implement all_words(root).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_basic():
    root = _build_trie(["cat", "car", "dog"])
    _assert_equal(sorted(all_words(root)), ["car", "cat", "dog"],
                  "Should return all three inserted words.")


def test_02_boundaries_empty_trie():
    root = TrieNode()
    _assert_equal(all_words(root), [], "Empty trie should return empty list.")


def test_03_boundaries_single_word():
    root = _build_trie(["hello"])
    _assert_equal(all_words(root), ["hello"], "Single word trie.")


def test_04_interactions_shared_prefix():
    root = _build_trie(["app", "apple", "ape"])
    _assert_equal(sorted(all_words(root)), ["ape", "app", "apple"],
                  "Words with shared prefixes should all be returned.")


def test_05_interactions_includes_empty_string():
    root = _build_trie(["", "a"])
    result = sorted(all_words(root))
    _assert_equal(result, ["", "a"], "Empty string should be included in results.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("boundaries: empty trie", test_02_boundaries_empty_trie),
        ("boundaries: single word", test_03_boundaries_single_word),
        ("interactions: shared prefix", test_04_interactions_shared_prefix),
        ("interactions: includes empty string", test_05_interactions_includes_empty_string),
    ]
    _run_all_tests(TEST_CASES)
