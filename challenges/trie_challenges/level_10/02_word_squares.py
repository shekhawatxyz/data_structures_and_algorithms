# Level 10b - word_squares
# Find all word squares from a list of words.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 10b. `word_squares(words)`
#
# A *word square* is a `k × k` grid of letters where the `i`-th row equals the `i`-th column for every `i` in `0..k-1` — so reading across or down gives the same set of words, in the same order. Given a list of unique words all of length `k`, return all word squares that can be formed using the words from the list. Each word may be used more than once across different squares but not more than once within a single square.
#
# Example: words = `["area", "lead", "wall", "lady", "ball"]`. One valid square:
#
# ```
# b a l l
# a r e a
# l e a d
# l a d y
# ```
#
# Trie indexed on the input words supports the inner loop: while filling row `i`, the prefix the row's word must have is determined by the first `i` letters of rows `0..i-1` (read column-wise, since rows must equal columns). Find all words sharing that prefix using your level-3b primitive, try each in turn, recurse, backtrack.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


def word_squares(words):
    raise NotImplementedError('Implement word_squares(words).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def _is_valid_word_square(square):
    k = len(square)
    for i in range(k):
        for j in range(k):
            if square[i][j] != square[j][i]:
                return False
    return True


def _assert_word_squares(result, words, expected):
    word_set = set(words)
    k = len(words[0]) if words else 0
    normalized = {tuple(square) for square in result}
    expected_normalized = {tuple(square) for square in expected}
    _assert_equal(normalized, expected_normalized, "Returned word squares differ from expected.")
    for square in result:
        _assert_equal(len(square), k, f"Square {square} should have {k} rows.")
        _assert_equal(len(set(square)), len(square), f"Square {square} should not reuse a word.")
        for row in square:
            _assert_true(row in word_set, f"Row {row!r} should come from the input words.")
            _assert_equal(len(row), k, f"Row {row!r} should have length {k}.")
        _assert_true(_is_valid_word_square(square), f"Square {square} is not valid.")


def test_01_pedagogy_basic():
    words = ["area", "lead", "wall", "lady", "ball"]
    expected = [
        ["wall", "area", "lead", "lady"],
        ["ball", "area", "lead", "lady"],
    ]
    _assert_word_squares(word_squares(words), words, expected)


def test_02_pedagogy_small():
    words = ["ab", "ba"]
    _assert_word_squares(word_squares(words), words, [["ab", "ba"], ["ba", "ab"]])


def test_03_boundaries_single_char_words():
    words = ["a", "b"]
    _assert_word_squares(word_squares(words), words, [["a"], ["b"]])


def test_04_interactions_no_valid_square():
    words = ["abc", "def", "ghi"]
    _assert_word_squares(word_squares(words), words, [])


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("pedagogy: small 2x2", test_02_pedagogy_small),
        ("boundaries: single char words", test_03_boundaries_single_char_words),
        ("interactions: validity check", test_04_interactions_no_valid_square),
    ]
    _run_all_tests(TEST_CASES)
