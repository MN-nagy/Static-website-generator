class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            children = list(current.keys())
            if self.end_symbol in children:
                break
            children_len = len(children)
            if children_len == 1:
                prefix += children[0]
                current = current[children[0]]
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
