class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            children = current.keys()
            children_list = list(children)

            if self.end_symbol in children_list:
                break

            children_count = len(children_list)

            if children_count == 1:
                char = children_list[0]
                prefix += char
                current = current[char]
            else:
                break

        return prefix

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
