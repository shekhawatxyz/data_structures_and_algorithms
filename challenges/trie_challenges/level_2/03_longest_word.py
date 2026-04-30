# Level 2c - longest_word
# Return the longest word in the trie.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 2c. `longest_word(root)`
#
# Return the longest word in the trie. Tie-break however you like, but state your rule in a comment.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def longest_word(root):
    raise NotImplementedError('Implement longest_word(root).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_clear_longest():
    root = _build_trie(["hi", "hello", "hey"])
    _assert_equal(longest_word(root), "hello", "'hello' is the longest word.")


def test_02_pedagogy_tie_break_lexicographic():
    root = _build_trie(["abc", "xyz", "def"])
    _assert_equal(longest_word(root), "abc",
                  "All length 3; 'abc' is lexicographically smallest.")


def test_03_boundaries_empty_trie():
    root = TrieNode()
    _assert_equal(longest_word(root), None, "Empty trie should return None.")


def test_04_boundaries_single_word():
    root = _build_trie(["cat"])
    _assert_equal(longest_word(root), "cat", "Single word is the longest.")


def test_05_interactions_prefix_is_also_word():
    root = _build_trie(["app", "apple", "application"])
    _assert_equal(longest_word(root), "application",
                  "'application' is the longest word.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: clear longest", test_01_pedagogy_clear_longest),
        ("pedagogy: tie-break lexicographic", test_02_pedagogy_tie_break_lexicographic),
        ("boundaries: empty trie", test_03_boundaries_empty_trie),
        ("boundaries: single word", test_04_boundaries_single_word),
        ("interactions: prefix is also word", test_05_interactions_prefix_is_also_word),
    ]
    _run_all_tests(TEST_CASES)
