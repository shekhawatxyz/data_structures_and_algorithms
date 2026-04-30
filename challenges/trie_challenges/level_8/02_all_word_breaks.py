# Level 8b - all_word_breaks
# Return all valid space-separated segmentations of a string.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 8b. `all_word_breaks(root, s)`
#
# Return all valid space-separated segmentations of `s`.
#
# Example: trie = `{"cat", "cats", "and", "sand", "dog"}`, `s = "catsanddog"` → `["cat sand dog", "cats and dog"]`.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def all_word_breaks(root, s):
    raise NotImplementedError('Implement all_word_breaks(root, s).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_multiple_segmentations():
    root = _build_trie(["cat", "cats", "and", "sand", "dog"])
    result = sorted(all_word_breaks(root, "catsanddog"))
    _assert_equal(result, sorted(["cat sand dog", "cats and dog"]),
                  "Two valid segmentations exist.")


def test_02_pedagogy_single_segmentation():
    root = _build_trie(["apple", "pen"])
    result = all_word_breaks(root, "applepen")
    _assert_equal(result, ["apple pen"], "Only one valid segmentation.")


def test_03_boundaries_empty_string():
    root = _build_trie(["cat"])
    result = all_word_breaks(root, "")
    _assert_equal(result, [""], "Empty string has one segmentation: empty.")


def test_04_boundaries_no_segmentation():
    root = _build_trie(["cat"])
    result = all_word_breaks(root, "dog")
    _assert_equal(result, [], "No valid segmentation.")


def test_05_interactions_repeated_word():
    root = _build_trie(["a"])
    result = all_word_breaks(root, "aaa")
    _assert_equal(result, ["a a a"], "Only segmentation is 'a a a'.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: multiple segmentations", test_01_pedagogy_multiple_segmentations),
        ("pedagogy: single segmentation", test_02_pedagogy_single_segmentation),
        ("boundaries: empty string", test_03_boundaries_empty_string),
        ("boundaries: no segmentation", test_04_boundaries_no_segmentation),
        ("interactions: repeated word", test_05_interactions_repeated_word),
    ]
    _run_all_tests(TEST_CASES)
