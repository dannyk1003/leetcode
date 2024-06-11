class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True
        
    def search(self, word: str) -> bool:
        return self._search_in_node(word, 0, self.root)
    
    def _search_in_node(self, word, index, node):
        if index == len(word):
            return node.is_end

        char = word[index]
        if char == '.':
            for child in node.children.values():
                if self._search_in_node(word, index + 1, child):
                    return True
        else:
            if char in node.children:
                return self._search_in_node(word, index + 1, node.children[char])

        return False
        
