# Level 5.1 - LoggerRateLimiter
# Design a rate-limiting logger that suppresses duplicate messages within 10 seconds.

# Complete Exact Problem Statement (from hashmap-challenges.md):
# ## 15. `LoggerRateLimiter`
#
# ```python
# class LoggerRateLimiter:
#     def __init__(self): ...
#     def should_print(self, timestamp: int, message: str) -> bool: ...
# ```
#
# Design a logger that receives a stream of `(timestamp, message)` calls. `should_print(timestamp, message)` returns `True` if the message has not been logged in the last 10 seconds — that is, if the same message was last logged at `t_prev`, the next call with that message returns `True` only when `timestamp - t_prev >= 10`. Otherwise it returns `False`. Timestamps are non-decreasing.
#
# A returned `True` counts as logging the message; a returned `False` does not.
#
# Example:
# ```python
# logger = LoggerRateLimiter()
# logger.should_print(1, "foo")    # True
# logger.should_print(2, "bar")    # True
# logger.should_print(3, "foo")    # False
# logger.should_print(8, "bar")    # False
# logger.should_print(10, "foo")   # False
# logger.should_print(11, "foo")   # True
# ```

class LoggerRateLimiter:
    def __init__(self):
        raise NotImplementedError('Implement LoggerRateLimiter.__init__().')

    def should_print(self, timestamp, message):
        raise NotImplementedError('Implement LoggerRateLimiter.should_print(timestamp, message).')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


def test_01_pedagogy_basic_sequence():
    logger = LoggerRateLimiter()
    _assert_equal(logger.should_print(1, "foo"), True, "First 'foo' at t=1 should print.")
    _assert_equal(logger.should_print(2, "bar"), True, "First 'bar' at t=2 should print.")
    _assert_equal(logger.should_print(3, "foo"), False, "'foo' at t=3 is within 10s of t=1.")
    _assert_equal(logger.should_print(8, "bar"), False, "'bar' at t=8 is within 10s of t=2.")
    _assert_equal(logger.should_print(10, "foo"), False, "'foo' at t=10 is still within 10s (10-1=9 < 10).")
    _assert_equal(logger.should_print(11, "foo"), True, "'foo' at t=11: 11-1=10 >= 10, should print.")


def test_02_pedagogy_different_messages_independent():
    logger = LoggerRateLimiter()
    _assert_equal(logger.should_print(0, "a"), True, "First 'a' prints.")
    _assert_equal(logger.should_print(0, "b"), True, "First 'b' prints (independent of 'a').")
    _assert_equal(logger.should_print(5, "a"), False, "'a' at t=5 within 10s.")
    _assert_equal(logger.should_print(5, "b"), False, "'b' at t=5 within 10s.")


def test_03_boundaries_exact_boundary():
    logger = LoggerRateLimiter()
    _assert_equal(logger.should_print(0, "msg"), True, "First print at t=0.")
    _assert_equal(logger.should_print(9, "msg"), False, "t=9: 9-0=9 < 10, still suppressed.")
    _assert_equal(logger.should_print(10, "msg"), True, "t=10: 10-0=10 >= 10, should print.")


def test_04_boundaries_false_does_not_update_timestamp():
    logger = LoggerRateLimiter()
    _assert_equal(logger.should_print(0, "x"), True, "Print at t=0.")
    _assert_equal(logger.should_print(5, "x"), False, "Suppressed at t=5.")
    _assert_equal(logger.should_print(10, "x"), True, "t=10: 10-0=10 >= 10 (not 10-5).")


def test_05_interactions_never_seen_message():
    logger = LoggerRateLimiter()
    _assert_equal(logger.should_print(100, "new"), True, "Never-seen message always prints.")


if __name__ == "__main__":
    TEST_CASES = [
        ("pedagogy: basic sequence", test_01_pedagogy_basic_sequence),
        ("pedagogy: different messages independent", test_02_pedagogy_different_messages_independent),
        ("boundaries: exact boundary", test_03_boundaries_exact_boundary),
        ("boundaries: false does not update timestamp", test_04_boundaries_false_does_not_update_timestamp),
        ("interactions: never seen message", test_05_interactions_never_seen_message),
    ]
    _run_all_tests(TEST_CASES)
