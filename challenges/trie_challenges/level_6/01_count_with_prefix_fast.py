# Level 6a - count_with_prefix_fast
# O(|prefix|) word count using augmented trie nodes.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 6a. Augmented insert and `count_with_prefix_fast(root, prefix)`
#
# Add a field `word_count` to each node, defined as the number of complete words at or below that node. Modify `insert` to maintain this on each call. Then implement `count_with_prefix_fast` so it runs in O(|prefix|) regardless of how many words sit under the prefix. Compare with your level-3a implementation: where did the work go?

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word_count = 0


def insert(root, word):
    raise NotImplementedError('Implement insert(root, word).')


def count_with_prefix_fast(root, prefix):
    raise NotImplementedError('Implement count_with_prefix_fast(root, prefix).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


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
    root = TrieNode()
    for w in ["app", "apple", "ape"]:
        insert(root, w)
    _assert_equal(count_with_prefix_fast(root, "ap"), 3,
                  "All three words start with 'ap'.")
    _assert_equal(count_with_prefix_fast(root, "app"), 2,
                  "'app' and 'apple' start with 'app'.")


def test_02_pedagogy_no_match():
    root = TrieNode()
    insert(root, "cat")
    _assert_equal(count_with_prefix_fast(root, "dog"), 0,
                  "No words start with 'dog'.")


def test_03_boundaries_empty_prefix():
    root = TrieNode()
    for w in ["a", "b", "c"]:
        insert(root, w)
    _assert_equal(count_with_prefix_fast(root, ""), 3,
                  "Empty prefix matches all words.")


def test_04_boundaries_root_word_count():
    root = TrieNode()
    insert(root, "hello")
    _assert_equal(root.word_count, 1, "Root word_count should be 1 after one insert.")
    insert(root, "help")
    _assert_equal(root.word_count, 2, "Root word_count should be 2 after two inserts.")


def test_05_interactions_duplicate_insert():
    root = TrieNode()
    insert(root, "cat")
    insert(root, "cat")
    _assert_equal(count_with_prefix_fast(root, "cat"), 2,
                  "Inserting same word twice should count as 2.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("pedagogy: no match", test_02_pedagogy_no_match),
        ("boundaries: empty prefix", test_03_boundaries_empty_prefix),
        ("boundaries: root word_count", test_04_boundaries_root_word_count),
        ("interactions: duplicate insert", test_05_interactions_duplicate_insert),
    ]
    _run_all_tests(TEST_CASES)
