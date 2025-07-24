from main import *

run_cases = [
    (10, "fitness", 1, 40),
    (10, "fitness", 2, 160),
    (12, "cosmetic", 4, 972),
]

submit_cases = run_cases + [
    (15, "business", 4, 240),
    (10, "fitness", 5, 10240),
    (10, "fitness", 6, 40960),
    (10, "fitness", 7, 163840),
    (10, "fitness", 8, 655360),
    (10, "tech", 9, 5120),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Follower count: {input1}")
    print(f" * Influencer type: {input2}")
    print(f" * Number of months: {input3}")
    print(f"Expecting: {expected_output}")
    result = get_follower_prediction(input1, input2, input3)
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
