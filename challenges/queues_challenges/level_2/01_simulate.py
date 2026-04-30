# Level 2a - Command stream
# Simulate enqueue, dequeue, and peek commands.

# Complete Exact Problem Statement (from queue-challenges.md):
# ### 2a — Command stream
#
# ```python
# def simulate(commands: list[str]) -> list:
#     ...
# ```
#
# `commands` is a list, each element being one of:
# - `"E x"` — enqueue the integer `x`
# - `"D"` — dequeue
# - `"P"` — peek
#
# Simulate the commands on an initially empty queue. Return the list of results from each `D` and `P`, in order. You may assume the input never tries to dequeue or peek an empty queue.
#
# ```
# simulate(["E 1", "E 2", "P", "D", "P"])  # [1, 1, 2]
# ```

def simulate(commands):
    raise NotImplementedError("Implement simulate(commands).")

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
    for name, fn in test_cases:
        if _run_test(name, fn):
            passed += 1
    print(f"\nPassed {passed}/{len(test_cases)} tests.")
    if passed != len(test_cases):
        raise SystemExit(1)


def test_sample_commands():
    _assert_equal(simulate(["E 1", "E 2", "P", "D", "P"]), [1, 1, 2],
                  "sample command stream should match expected output.")


def test_multiple_dequeues_and_peeks():
    commands = ["E 5", "E -1", "D", "E 7", "P", "D", "D"]
    _assert_equal(simulate(commands), [5, -1, -1, 7],
                  "results should appear only for D and P commands.")


def test_no_result_commands():
    _assert_equal(simulate(["E 10", "E 20"]), [],
                  "enqueue-only command stream should produce no results.")


if __name__ == "__main__":
    TEST_CASES = [
        ("sample commands", test_sample_commands),
        ("multiple dequeues and peeks", test_multiple_dequeues_and_peeks),
        ("no result commands", test_no_result_commands),
    ]
    _run_all_tests(TEST_CASES)
