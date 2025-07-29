import json
from main import *
from commit import commit

run_cases = [
    (
        ["dev", "devops", "devs"],
        {
            "d": {
                "e": {
                    "v": {"*": True, "o": {"p": {"s": {"*": True}}}, "s": {"*": True}}
                }
            }
        },
    ),
    (
        ["qa", "qaops", "qam"],
        {
            "q": {
                "a": {"*": True, "o": {"p": {"s": {"*": True}}}, "m": {"*": True}},
            }
        },
    ),
]

submit_cases = run_cases + [
    (
        ["pm", "po", "pojo", "pope", "cs", "ce", "ceo", "cfo"],
        {
            "p": {
                "m": {"*": True},
                "o": {"*": True, "j": {"o": {"*": True}}, "p": {"e": {"*": True}}},
            },
            "c": {
                "s": {"*": True},
                "e": {"*": True, "o": {"*": True}},
                "f": {"o": {"*": True}},
            },
        },
    ),
]


def test(words, expected_trie):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Words: {words}")
    print(" * Expected trie:")
    print(f"{json.dumps(expected_trie, sort_keys=True, indent=2)}")
    try:
        trie = Trie()
        for word in words:
            trie.add(word)
            print(f"Adding {word}...")
        print("Actual Trie:")
        print(json.dumps(trie.root, sort_keys=True, indent=2))
        if trie.root == expected_trie:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
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
