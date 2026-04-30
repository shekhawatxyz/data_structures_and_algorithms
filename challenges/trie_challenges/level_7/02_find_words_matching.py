# Level 7b - find_words_matching
# Return all words matching a wildcard pattern.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 7b. `find_words_matching(root, pattern)`
#
# Same wildcard rules; return the list of all matching words.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def find_words_matching(root, pattern):
    raise NotImplementedError('Implement find_words_matching(root, pattern).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    root = _build_trie(["cat", "car", "bat", "bar"])
    _assert_equal(sorted(find_words_matching(root, "c.t")), ["cat"],
                  "'c.t' matches only 'cat'.")


def test_02_pedagogy_multiple_matches():
    root = _build_trie(["cat", "car", "bat", "bar"])
    _assert_equal(sorted(find_words_matching(root, ".a.")), ["bar", "bat", "car", "cat"],
                  "'.a.' matches all four words.")


def test_03_boundaries_no_matches():
    root = _build_trie(["cat", "dog"])
    _assert_equal(find_words_matching(root, "...."), [],
                  "No 4-letter words; empty result.")


def test_04_interactions_exact_match():
    root = _build_trie(["hello", "help"])
    _assert_equal(sorted(find_words_matching(root, "hel.o")), ["hello"],
                  "'hel.o' matches 'hello' only.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("pedagogy: multiple matches", test_02_pedagogy_multiple_matches),
        ("boundaries: no matches", test_03_boundaries_no_matches),
        ("interactions: exact match with dot", test_04_interactions_exact_match),
    ]
    _run_all_tests(TEST_CASES)
