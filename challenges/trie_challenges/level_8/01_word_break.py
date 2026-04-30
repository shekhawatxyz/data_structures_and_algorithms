# Level 8a - word_break
# Determine if a string can be segmented into trie words.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 8a. `word_break(root, s)`
#
# Return `True` iff `s` can be partitioned into a sequence of words all present in the trie. The empty string returns `True` (the empty partition).
#
# Example: trie = `{"apple", "pen", "applepen"}`, `s = "applepenapple"` → `True` (e.g. `"apple" "pen" "apple"`). `s = "pineapplepenapple"` → `False`.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def word_break(root, s):
    raise NotImplementedError('Implement word_break(root, s).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_breakable():
    root = _build_trie(["apple", "pen", "applepen"])
    _assert_equal(word_break(root, "applepenapple"), True,
                  "'apple' + 'pen' + 'apple' is a valid segmentation.")


def test_02_pedagogy_not_breakable():
    root = _build_trie(["apple", "pen", "applepen"])
    _assert_equal(word_break(root, "pineapplepenapple"), False,
                  "Cannot segment 'pineapplepenapple' using given words.")


def test_03_boundaries_empty_string():
    root = _build_trie(["cat"])
    _assert_equal(word_break(root, ""), True,
                  "Empty string is always breakable (empty partition).")


def test_04_boundaries_single_word():
    root = _build_trie(["hello"])
    _assert_equal(word_break(root, "hello"), True, "'hello' is in the trie.")
    _assert_equal(word_break(root, "hell"), False, "'hell' is not in the trie.")


def test_05_interactions_overlapping_words():
    root = _build_trie(["cat", "cats", "and", "sand", "dog"])
    _assert_equal(word_break(root, "catsanddog"), True,
                  "'cats' + 'and' + 'dog' or 'cat' + 'sand' + 'dog'.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: breakable", test_01_pedagogy_breakable),
        ("pedagogy: not breakable", test_02_pedagogy_not_breakable),
        ("boundaries: empty string", test_03_boundaries_empty_string),
        ("boundaries: single word", test_04_boundaries_single_word),
        ("interactions: overlapping words", test_05_interactions_overlapping_words),
    ]
    _run_all_tests(TEST_CASES)
