from functools import reduce


class HashMap:
    def key_to_index(self, key: str):
        uni_sum = int(reduce(lambda x, y: x + ord(y), key, 0))
        return uni_sum % len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)
