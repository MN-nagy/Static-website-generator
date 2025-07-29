class Trie:
    # def search_level(self, current_level, current_prefix, words: list):
    #     if self.end_symbol in current_level:
    #         words.append(current_prefix)
    #     for letter in sorted(current_level.keys()):
    #         if letter == self.end_symbol:
    #             continue
    #         self.search_level(current_level[letter], current_prefix + letter, words)
    #     return words

    def search_level(self, start_node, current_prefix):
        words = []
        stack = [(start_node, current_prefix)]

        while stack:
            node, prefix = stack.pop()

            if self.end_symbol in node:
                words.append(prefix)

            for letter in sorted(node.keys(), reverse=True):
                if letter == self.end_symbol:
                    continue
                child_node = node[letter]
                new_prefix = prefix + letter
                stack.append((child_node, new_prefix))
        return words

    def words_with_prefix(self, prefix):
        current_level = self.root
        for letter in prefix:
            if letter not in current_level:
                return []
            current_level = current_level[letter]
        return self.search_level(current_level, prefix)

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True
