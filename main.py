class Trie:
    def add(self, word):
        current_level = self.root
        for char in word:
            if char not in current_level:
                current_level[char] = {}
            current_level = current_level[char]
        current_level[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
