# Level 10a - Parse Nested List String
# Write parse_nested_list(text) for inputs like [1,[2,3],[4,[5,6]]].
# Return actual nested Python list using stack-based list assembly.

# Complete Exact Problem Statement (from stack-challenges.md):
# **10a.** Write a function that takes a nested list represented as a string like `"[1,[2,3],[4,[5,6]]]"` and returns the actual nested Python list. Use a stack: when you see `[`, push a new empty list; when you see `]`, pop the completed list and append it to whatever is now on top. Numbers between commas get appended to the current top-of-stack list.


def parse_nested_list(text):
    nested_stack = []
    buffer = ""
    prev = None
    for t in range(len(text)):
        if text[t] == "[":
            nested_stack.append([])
            prev = "open"
        elif text[t] == "]":
            if len(buffer) > 0:
                nested_stack[-1].append(int(buffer))
            elif prev is None:
                raise Exception
            elif prev == "comma":
                raise Exception
            buffer = ""
            popped_list = nested_stack.pop()
            if not nested_stack:
                return popped_list
            else:
                nested_stack[-1].append(popped_list)
                prev = "closed"
        elif text[t] == ",":
            if prev == "comma":
                raise Exception
            elif len(buffer) > 0:
                nested_stack[-1].append(int(buffer))
            prev = "comma"
            buffer = ""
        else:
            buffer = buffer + text[t]
            prev = "digit"
    raise Exception


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    ("empty list", "[]", []),
    ("flat list", "[1,2,3]", [1, 2, 3]),
    ("single nested list", "[1,[2,3]]", [1, [2, 3]]),
    ("given-style nested list", "[1,[2,3],[4,[5,6]]]", [1, [2, 3], [4, [5, 6]]]),
    ("nested empty sublist", "[1,[],2]", [1, [], 2]),
]


BOUNDARY_CASES = [
    (
        "multi-digit and negative numbers",
        "[-10,[20,[-3,4]],5]",
        [-10, [20, [-3, 4]], 5],
    ),
    ("deeply nested single chain", "[1,[2,[3,[4]]]]", [1, [2, [3, [4]]]]),
    ("missing closing bracket", "[1,2", _CASE_EXPECTS_RAISE),
    ("missing opening bracket", "1,2]", _CASE_EXPECTS_RAISE),
    ("empty input string", "", _CASE_EXPECTS_RAISE),
]


INTERACTION_CASES = [
    ("mixed nesting with empties", "[[1,2],[],[3,[4],5]]", [[1, 2], [], [3, [4], 5]]),
    ("all negatives nested", "[[-1],[-2,[-3]],4]", [[-1], [-2, [-3]], 4]),
    (
        "multiple sibling nested groups",
        "[1,[2],[3,[4,[5]]],6]",
        [1, [2], [3, [4, [5]]], 6],
    ),
    ("invalid repeated commas", "[1,,2]", _CASE_EXPECTS_RAISE),
    ("invalid trailing comma", "[1,2,]", _CASE_EXPECTS_RAISE),
]


def _run_case_group(group_name, cases):
    for case_index, (case_label, input_value, expected) in enumerate(cases, start=1):
        if expected is _CASE_EXPECTS_RAISE:
            _assert_raises(
                lambda value=copy.deepcopy(input_value): parse_nested_list(value),
                (
                    f"{group_name} case {case_index} ({case_label}) expected an exception "
                    f"for input {input_value!r}."
                ),
            )
            continue

        actual = parse_nested_list(copy.deepcopy(input_value))
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
