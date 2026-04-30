# Level 1b - search
# Return True iff the word was inserted into the trie.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 1b. `search(root, word)`
#
# Return `True` iff `word` was inserted (and not deleted). The terminal flag is what distinguishes a word from a strict prefix of one.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def search(root, word):
    raise NotImplementedError('Implement search(root, word).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _assert_raises(callable_obj, context):
    try:
        callable_obj()
    except Exception:
        return
    raise AssertionError(f"{context} Expected an exception, but none was raised.")


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


def test_01_pedagogy_word_found():
    root = _build_trie(["cat", "car", "dog"])
    _assert_equal(search(root, "cat"), True, "'cat' was inserted and should be found.")


def test_02_pedagogy_word_not_found():
    root = _build_trie(["cat", "car", "dog"])
    _assert_equal(search(root, "cab"), False, "'cab' was not inserted.")


def test_03_boundaries_prefix_is_not_word():
    root = _build_trie(["apple"])
    _assert_equal(search(root, "app"), False,
                  "'app' is a prefix of 'apple' but not a complete word.")


def test_04_boundaries_empty_trie():
    root = TrieNode()
    _assert_equal(search(root, "anything"), False, "Empty trie contains no words.")


def test_05_boundaries_empty_string():
    root = _build_trie([""])
    _assert_equal(search(root, ""), True, "Empty string was inserted and should be found.")


def test_06_interactions_word_longer_than_any():
    root = _build_trie(["hi"])
    _assert_equal(search(root, "high"), False,
                  "'high' extends beyond any path in the trie.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: word found", test_01_pedagogy_word_found),
        ("pedagogy: word not found", test_02_pedagogy_word_not_found),
        ("boundaries: prefix is not word", test_03_boundaries_prefix_is_not_word),
        ("boundaries: empty trie", test_04_boundaries_empty_trie),
        ("boundaries: empty string", test_05_boundaries_empty_string),
        ("interactions: word longer than any", test_06_interactions_word_longer_than_any),
    ]
    _run_all_tests(TEST_CASES)
