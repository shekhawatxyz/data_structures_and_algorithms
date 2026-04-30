# Level 1c - starts_with
# Return True iff some inserted word has the given prefix.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 1c. `starts_with(root, prefix)`
#
# Return `True` iff some inserted word has `prefix` as a prefix. The terminal flag is irrelevant here.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def starts_with(root, prefix):
    raise NotImplementedError('Implement starts_with(root, prefix).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_valid_prefix():
    root = _build_trie(["apple", "app", "banana"])
    _assert_equal(starts_with(root, "app"), True,
                  "'app' is a prefix of 'apple' and also a word itself.")


def test_02_pedagogy_prefix_not_present():
    root = _build_trie(["apple", "banana"])
    _assert_equal(starts_with(root, "cat"), False,
                  "No word starts with 'cat'.")


def test_03_boundaries_empty_prefix():
    root = _build_trie(["hello"])
    _assert_equal(starts_with(root, ""), True,
                  "Empty prefix is a prefix of every word.")


def test_04_boundaries_prefix_longer_than_words():
    root = _build_trie(["hi"])
    _assert_equal(starts_with(root, "high"), False,
                  "'high' extends beyond any word in the trie.")


def test_05_interactions_exact_word_as_prefix():
    root = _build_trie(["cat"])
    _assert_equal(starts_with(root, "cat"), True,
                  "A complete word is also a valid prefix of itself.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: valid prefix", test_01_pedagogy_valid_prefix),
        ("pedagogy: prefix not present", test_02_pedagogy_prefix_not_present),
        ("boundaries: empty prefix", test_03_boundaries_empty_prefix),
        ("boundaries: prefix longer than words", test_04_boundaries_prefix_longer_than_words),
        ("interactions: exact word as prefix", test_05_interactions_exact_word_as_prefix),
    ]
    _run_all_tests(TEST_CASES)
