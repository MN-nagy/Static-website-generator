from main import HashMap
from commit import commit

import random


class User:
    def __init__(self, id, age, job_title):
        self.id = id
        user_names = [
            "Blake",
            "Ricky",
            "Shelley",
            "Dave",
            "George",
            "John",
            "James",
            "Mitch",
            "Williamson",
            "Burry",
            "Vennett",
            "Shipley",
            "Geller",
            "Rickert",
            "Carrell",
            "Baum",
            "Brownfield",
            "Lippmann",
            "Moses",
        ]
        self.user_name = f"{user_names[id % len(user_names)]}#{id}"
        self.age = age
        self.job_title = job_title

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id

    def __lt__(self, other):
        return isinstance(other, User) and self.id < other.id

    def __gt__(self, other):
        return isinstance(other, User) and self.id > other.id

    def __repr__(self):
        parts = self.user_name.split("#")
        return f"(Name: {parts[0]}, ID: {self.id}, Age: {self.age}, Job Title: {self.job_title})"


def get_users(num):
    random.seed(1)
    job_titles = ["Engineer", "Designer", "Manager", "Clerk", "Analyst"]
    users = []
    ids = list(range(num * 3))
    random.shuffle(ids)
    ids = ids[:num]
    for id in ids:
        age = random.randint(20, 60)
        job_title = random.choice(job_titles)
        user = User(id, age, job_title)
        users.append(user)
    return users


run_cases = [
    (
        512,
        [User(1, 30, "Engineer"), User(2, 25, "Designer")],
        [
            ("Ricky#1", User(1, 30, "Engineer")),
            ("Shelley#2", User(2, 25, "Designer")),
            ("FakeyFaker#2", None),
        ],
    ),
]

submit_cases = run_cases + [
    (
        1028,
        [User(4, 36, "Clerk"), User(5, 29, "Chef"), User(6, 55, "Pilot")],
        [
            ("George#4", User(4, 36, "Clerk")),
            ("John#5", User(5, 29, "Chef")),
            ("Blake#1", None),
        ],
    ),
]


def test(size, users, expected_hashmap):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * HashMap size: {size}")
    hm = HashMap(size)
    for user in users:
        hm.insert(user.user_name, user)
        print(f"   * Inserted ({user.user_name}, {user})")

    passes = True
    for user_name, expected in expected_hashmap:
        try:
            result = hm.get(user_name)
            if result == expected:
                print(f"Get {user_name}: Pass")
            else:
                print(f"Get {user_name}: Fail")
                print(f"   * Expect: {expected}")
                print(f"   * Actual: {result}")
                passes = False
        except Exception as e:
            actualErr = str(e)
            expectedErr = "sorry, key not found"

            if expected is not None:
                print(f"Get {user_name}: Fail")
                print(f"   * Expect: {expected}")
                print(f"   * Actual: exception: {actualErr}")
                passes = False
            elif actualErr == expectedErr:
                print(f"Get {user_name}: Pass")
            else:
                print(f"Get {user_name}: Fail")
                print(f"   * Expect exception: {expectedErr}")
                print(f"   * Actual exception: {actualErr}")
                passes = False

    if passes:
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
