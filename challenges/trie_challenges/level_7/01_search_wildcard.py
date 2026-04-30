# Level 7a - search_wildcard
# Search for a word with '.' wildcard matching any single character.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 7a. `search_wildcard(root, pattern)`
#
# `pattern` is a string that may contain `.`, which matches any single character. Return `True` iff some word in the trie matches the pattern exactly (length must match too).
#
# Example: trie = `{"cat", "car", "dog"}`. Pattern `"c.t"` → `True`; pattern `"c..s"` → `False` (no length-4 words); pattern `".og"` → `True`.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def search_wildcard(root, pattern):
    raise NotImplementedError('Implement search_wildcard(root, pattern).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_dot_matches():
    root = _build_trie(["cat", "car", "dog"])
    _assert_equal(search_wildcard(root, "c.t"), True,
                  "'c.t' matches 'cat'.")


def test_02_pedagogy_no_match_wrong_length():
    root = _build_trie(["cat", "car", "dog"])
    _assert_equal(search_wildcard(root, "c..s"), False,
                  "No length-4 words match 'c..s'.")


def test_03_pedagogy_dot_at_start():
    root = _build_trie(["cat", "car", "dog"])
    _assert_equal(search_wildcard(root, ".og"), True,
                  "'.og' matches 'dog'.")


def test_04_boundaries_all_dots():
    root = _build_trie(["cat", "dog"])
    _assert_equal(search_wildcard(root, "..."), True,
                  "'...' matches any 3-letter word.")


def test_05_boundaries_no_wildcard():
    root = _build_trie(["cat", "car"])
    _assert_equal(search_wildcard(root, "cat"), True, "Exact match without dots.")
    _assert_equal(search_wildcard(root, "cab"), False, "No exact match.")


def test_06_interactions_empty_pattern():
    root = _build_trie(["", "a"])
    _assert_equal(search_wildcard(root, ""), True,
                  "Empty pattern matches empty word.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: dot matches", test_01_pedagogy_dot_matches),
        ("pedagogy: no match wrong length", test_02_pedagogy_no_match_wrong_length),
        ("pedagogy: dot at start", test_03_pedagogy_dot_at_start),
        ("boundaries: all dots", test_04_boundaries_all_dots),
        ("boundaries: no wildcard", test_05_boundaries_no_wildcard),
        ("interactions: empty pattern", test_06_interactions_empty_pattern),
    ]
    _run_all_tests(TEST_CASES)
