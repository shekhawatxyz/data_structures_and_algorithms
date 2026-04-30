# Level 8a - Daily Temperatures (Monotonic Stack)
# Write daily_temperatures_waits(temps) returning days-until-warmer values.

# Complete Exact Problem Statement (from stack-challenges.md):
# **8a.** Given an array of daily temperatures (integers), return an array where each element tells you how many days you'd have to wait for a warmer temperature. If no warmer day exists, output `0`. Example: `[73, 74, 75, 71, 69, 72, 76, 73]` → `[1, 1, 4, 2, 1, 1, 0, 0]`. Use a stack. (Hint: what should the stack store — values, indices, or both? What invariant should it maintain?)

def daily_temperatures_waits(temps):
    raise NotImplementedError('Implement daily_temperatures_waits(temps).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


import copy

_CASE_EXPECTS_RAISE = object()


PEDAGOGY_CASES = [
    ("empty input", [], []),
    ("single day", [70], [0]),
    ("given example", [73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ("strictly increasing", [60, 61, 62, 63], [1, 1, 1, 0]),
    ("strictly decreasing", [80, 79, 78], [0, 0, 0]),
]


BOUNDARY_CASES = [
    ("all equal temperatures", [70, 70, 70], [0, 0, 0]),
    ("two-day warmer", [70, 71], [1, 0]),
    ("two-day cooler", [71, 70], [0, 0]),
    ("plateau then warmer", [70, 70, 71], [2, 1, 0]),
    ("warm spike then decline", [70, 75, 74, 73], [1, 0, 0, 0]),
]


INTERACTION_CASES = [
    ("multiple local valleys", [65, 60, 62, 58, 70, 59, 71], [4, 1, 2, 1, 2, 1, 0]),
    ("alternating highs and lows", [70, 60, 71, 61, 72], [2, 1, 2, 1, 0]),
    ("late single warmer day", [75, 74, 73, 72, 76], [4, 3, 2, 1, 0]),
    ("warm day never exceeded", [80, 60, 70, 75], [0, 1, 1, 0]),
    ("complex mixed sequence", [68, 69, 67, 70, 66, 71, 65], [1, 2, 1, 2, 1, 0, 0]),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): daily_temperatures_waits(
                    value
                ),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = daily_temperatures_waits(copy.deepcopy(input_value))
        _assert_equal(
            actual,
            expected,
            (
                f"{group_name} case {case_index} ({case_label}) produced an unexpected result "
                f"for input {input_value!r}."
            ),
        )


def test_01_pedagogical_progression():
    _run_case_group("Pedagogy", PEDAGOGY_CASES)


def test_02_boundaries_and_off_by_ones():
    _run_case_group("Boundaries", BOUNDARY_CASES)


def test_03_complex_input_interactions():
    _run_case_group("Interactions", INTERACTION_CASES)


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogical progression", test_01_pedagogical_progression),
        ("boundary and off-by-one coverage", test_02_boundaries_and_off_by_ones),
        ("complex interaction coverage", test_03_complex_input_interactions),
    ]
    _run_all_tests(TEST_CASES)
