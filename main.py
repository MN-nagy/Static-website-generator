# TODO:
class Trie:
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            current_level = self.root
            for j in range(i, len(document)):
                char = document[j]
                if char not in current_level:
                    break
                else:
                    current_level = current_level[char]

                    if self.end_symbol in current_level:
                        matched_word = document[i : j + 1]
                        matches.add(matched_word)
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
