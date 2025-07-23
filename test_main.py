from commit import commit
from main import *

run_cases = [([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 2686826), ([12, 12, 12], 36)]

submit_cases = run_cases + [
    ([10, 200, 3000, 5000, 4], 8214),
    ([], 0),
    ([1], 1),
    ([123456789], 123456789),
    ([-1, -2, -3], -6),
    ([0, 0, 0, 0, 0], 0),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * nums: {input1}")
    print(f"Expecting: {expected_output}")
    result = sum(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
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

