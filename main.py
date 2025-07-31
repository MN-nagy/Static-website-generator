class Trie:
    def find_matches(self, document):
        matches = set()
        for index in range(len(document)):
            current_level = self.root
            for sec_index in range(index, len(document)):
                char = document[sec_index]
                if char not in current_level:
                    break
                else:
                    current_level = current_level[char]
                if self.end_symbol in current_level:
                    matches.add(document[index : sec_index + 1])
        return matches

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
