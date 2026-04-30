# Level 9a - BitTrie with insert and max_xor_with
# Implement a bit-trie for maximising XOR queries.

# Complete Exact Problem Statement (from trie-challenges.md):
# ### 9a. `BitTrie` with `insert(value)` and `max_xor_with(query)`
#
# Implement a class with two methods. `insert(value)` adds a 32-bit non-negative integer to the trie. `max_xor_with(query)` returns the maximum value of `value XOR query` over all inserted values. The walk is greedy: at each bit position from MSB to LSB, prefer the child whose bit *differs* from the corresponding bit of `query`; fall back to the other child only if that path doesn't exist.

class BitNode:
    def __init__(self):
        self.children = [None, None]


class BitTrie:
    def __init__(self):
        raise NotImplementedError('Implement BitTrie.__init__().')

    def insert(self, value):
        raise NotImplementedError('Implement BitTrie.insert(value).')

    def max_xor_with(self, query):
        raise NotImplementedError('Implement BitTrie.max_xor_with(query).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    bt = BitTrie()
    bt.insert(3)
    bt.insert(10)
    bt.insert(5)
    _assert_equal(bt.max_xor_with(6), 6 ^ 5 if 6 ^ 5 > max(6 ^ 3, 6 ^ 10) else max(6 ^ 3, 6 ^ 10),
                  "Should return maximum XOR with query 6.")
    # 6^3=5, 6^10=12, 6^5=3 => max is 12
    _assert_equal(bt.max_xor_with(6), 12, "6 XOR 10 = 12 is the maximum.")


def test_02_pedagogy_single_value():
    bt = BitTrie()
    bt.insert(7)
    _assert_equal(bt.max_xor_with(0), 7, "0 XOR 7 = 7.")
    _assert_equal(bt.max_xor_with(7), 0, "7 XOR 7 = 0.")


def test_03_boundaries_zero():
    bt = BitTrie()
    bt.insert(0)
    _assert_equal(bt.max_xor_with(0), 0, "0 XOR 0 = 0.")
    _assert_equal(bt.max_xor_with(15), 15, "15 XOR 0 = 15.")


def test_04_interactions_multiple_values():
    bt = BitTrie()
    for v in [1, 2, 4, 8, 16]:
        bt.insert(v)
    # max XOR with 31 (all 1s): best is to XOR with something that gives most 1s
    # 31 ^ 16 = 15, 31 ^ 8 = 23, 31 ^ 4 = 27, 31 ^ 2 = 29, 31 ^ 1 = 30
    _assert_equal(bt.max_xor_with(31), 30, "31 XOR 1 = 30 is the maximum.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic", test_01_pedagogy_basic),
        ("pedagogy: single value", test_02_pedagogy_single_value),
        ("boundaries: zero", test_03_boundaries_zero),
        ("interactions: multiple values", test_04_interactions_multiple_values),
    ]
    _run_all_tests(TEST_CASES)
