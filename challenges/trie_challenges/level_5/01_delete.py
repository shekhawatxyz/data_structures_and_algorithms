# Level 5a - delete
# Remove a word from the trie without disturbing other words.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 5a. `delete(root, word)`
#
# Remove `word` from the trie if present. After the call: `search(root, word)` returns `False`; any other word that shared a prefix with `word` is unaffected; no childless, non-terminal nodes are left dangling on what used to be `word`'s path; if `word` was not present, the trie is unchanged.
#
# Cases worth thinking through *before* you code (try to enumerate your own list before reading mine): `word` shares its full path with another, longer word; `word` has a tail of nodes no other word uses; `word` is itself a prefix of another word in the trie; another word is a prefix of `word`; `word` is not in the trie at all.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def delete(root, word):
    raise NotImplementedError('Implement delete(root, word).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _search(root, word):
    node = root
    for ch in word:
        if ch not in node.children:
            return False
        node = node.children[ch]
    return node.is_end


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


def test_01_pedagogy_delete_existing():
    root = _build_trie(["cat", "car"])
    delete(root, "cat")
    _assert_equal(_search(root, "cat"), False, "'cat' should no longer be found.")
    _assert_equal(_search(root, "car"), True, "'car' should still be found.")


def test_02_pedagogy_delete_with_longer_word():
    root = _build_trie(["app", "apple"])
    delete(root, "app")
    _assert_equal(_search(root, "app"), False, "'app' should be gone.")
    _assert_equal(_search(root, "apple"), True, "'apple' should remain.")


def test_03_boundaries_delete_nonexistent():
    root = _build_trie(["hello"])
    delete(root, "world")
    _assert_equal(_search(root, "hello"), True, "Trie should be unchanged.")


def test_04_boundaries_delete_prunes_dangling():
    root = _build_trie(["abc"])
    delete(root, "abc")
    _assert_equal(len(root.children), 0,
                  "After deleting 'abc' (the only word), root should have no children.")


def test_05_interactions_delete_prefix_of_another():
    root = _build_trie(["cat", "catalog"])
    delete(root, "cat")
    _assert_equal(_search(root, "cat"), False, "'cat' deleted.")
    _assert_equal(_search(root, "catalog"), True, "'catalog' still present.")
    # The path for 'catalog' should remain intact
    _assert_true("c" in root.children, "Path to 'catalog' should still exist.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: delete existing", test_01_pedagogy_delete_existing),
        ("pedagogy: delete with longer word", test_02_pedagogy_delete_with_longer_word),
        ("boundaries: delete nonexistent", test_03_boundaries_delete_nonexistent),
        ("boundaries: delete prunes dangling", test_04_boundaries_delete_prunes_dangling),
        ("interactions: delete prefix of another", test_05_interactions_delete_prefix_of_another),
    ]
    _run_all_tests(TEST_CASES)
