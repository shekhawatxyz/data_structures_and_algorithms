# Level 1a - insert
# Insert a word into the trie rooted at root.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 1a. `insert(root, word)`
#
# Insert `word` into the trie rooted at `root`. Inserting the same word twice should not create a duplicate path.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def insert(root, word):
    raise NotImplementedError('Implement insert(root, word).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_single_word():
    root = TrieNode()
    insert(root, "cat")
    _assert_true("c" in root.children, "Root should have child 'c' after inserting 'cat'.")
    c_node = root.children["c"]
    _assert_true("a" in c_node.children, "'c' node should have child 'a'.")
    a_node = c_node.children["a"]
    _assert_true("t" in a_node.children, "'a' node should have child 't'.")
    t_node = a_node.children["t"]
    _assert_true(t_node.is_end, "End of 'cat' should be marked as terminal.")


def test_02_pedagogy_two_words_shared_prefix():
    root = TrieNode()
    insert(root, "cat")
    insert(root, "car")
    c_node = root.children["c"]
    a_node = c_node.children["a"]
    _assert_true("t" in a_node.children, "'cat' path should exist.")
    _assert_true("r" in a_node.children, "'car' path should exist.")
    _assert_true(a_node.children["t"].is_end, "'cat' terminal should be set.")
    _assert_true(a_node.children["r"].is_end, "'car' terminal should be set.")


def test_03_boundaries_empty_word():
    root = TrieNode()
    insert(root, "")
    _assert_true(root.is_end, "Inserting empty string should mark root as terminal.")
    _assert_equal(len(root.children), 0, "No children should be created for empty string.")


def test_04_boundaries_duplicate_insert_no_duplicate_path():
    root = TrieNode()
    insert(root, "hi")
    insert(root, "hi")
    h_node = root.children["h"]
    _assert_equal(len(h_node.children), 1, "Duplicate insert should not create extra children.")


def test_05_interactions_prefix_word():
    root = TrieNode()
    insert(root, "app")
    insert(root, "apple")
    a_node = root.children["a"]
    p1 = a_node.children["p"]
    p2 = p1.children["p"]
    _assert_true(p2.is_end, "'app' should be marked as terminal.")
    l_node = p2.children["l"]
    e_node = l_node.children["e"]
    _assert_true(e_node.is_end, "'apple' should be marked as terminal.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: single word", test_01_pedagogy_single_word),
        ("pedagogy: shared prefix", test_02_pedagogy_two_words_shared_prefix),
        ("boundaries: empty word", test_03_boundaries_empty_word),
        ("boundaries: duplicate insert", test_04_boundaries_duplicate_insert_no_duplicate_path),
        ("interactions: prefix word", test_05_interactions_prefix_word),
    ]
    _run_all_tests(TEST_CASES)
