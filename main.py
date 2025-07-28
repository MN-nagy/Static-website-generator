class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        cl = self.current_load()
        if cl == 0:
            self.hashmap.append(None)
            return
        elif cl < 0.05:
            return
        else:
            old_elements = []
            for item in self.hashmap:
                if item is not None:
                    old_elements.append(item)

            new_size = 10 * len(self.hashmap)
            if new_size == 0:
                return 1

            self.hashmap = [None for _ in range(new_size)]
            for key, value in old_elements:
                index = self.key_to_index(key)
                self.hashmap[index] = (key, value)

    def current_load(self):
        length = len(self.hashmap)
        if length == 0:
            return 0
        filled_buckets = 0
        for i in self.hashmap:
            if i is not None:
                filled_buckets += 1
        return filled_buckets / length

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
