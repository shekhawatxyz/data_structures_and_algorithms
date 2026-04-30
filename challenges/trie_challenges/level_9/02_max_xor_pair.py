# Level 9b - max_xor_pair
# Find the maximum XOR over all pairs in a list.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 9b. `max_xor_pair(values)`
#
# Given a list of non-negative integers, return the maximum XOR over all pairs `(values[i], values[j])` with `i != j`. Use 9a as a sub-procedure: scan once, inserting as you go and querying `max_xor_with` against each value seen so far.

class BitNode:
    def __init__(self):
        self.children = [None, None]


def max_xor_pair(values):
    raise NotImplementedError('Implement max_xor_pair(values).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    _assert_equal(max_xor_pair([3, 10, 5, 25, 2, 8]), 28,
                  "5 XOR 25 = 28 is the maximum XOR pair.")


def test_02_pedagogy_small():
    _assert_equal(max_xor_pair([1, 2, 3]), 3,
                  "1 XOR 2 = 3 is the max.")


def test_03_boundaries_two_elements():
    _assert_equal(max_xor_pair([0, 15]), 15,
                  "0 XOR 15 = 15.")


def test_04_interactions_powers_of_two():
    _assert_equal(max_xor_pair([1, 2, 4, 8, 16]), 24,
                  "8 XOR 16 = 24 is the max.")


def test_05_interactions_all_same():
    _assert_equal(max_xor_pair([7, 7, 7]), 0,
                  "All same values; max XOR is 0.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("pedagogy: small", test_02_pedagogy_small),
        ("boundaries: two elements", test_03_boundaries_two_elements),
        ("interactions: powers of two", test_04_interactions_powers_of_two),
        ("interactions: all same", test_05_interactions_all_same),
    ]
    _run_all_tests(TEST_CASES)
