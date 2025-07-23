from commit import commit
from main import *

run_cases = [
    ([1], 1),
    ([1, 2, 3, 4, 5, 6, 7], 4),
    ([12, 12, 12], 12),
    ([], None),
]

submit_cases = run_cases + [
    ([0], 0),
    ([100, 200, 300, 400, 500], 300),
    ([5, 10, 200, 3000, 5000], 1643),
    ([12_345, 618_222, 58_832_221, 2_180_831_475, 8_663_863_102], 2_180_831_473),
]


def test(input1, expected_output):
    try:
        print("---------------------------------")
        print(f"Inputs:")
        print(f" * nums: {input1}")
        print(f"Expecting: {expected_output}")
        result = average_followers(input1)
        if expected_output is not None:
            result = int(result)
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(e)
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
        commit()
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
