class Node:

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        if node.is_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for chr in prefix:
            if chr not in node.children:
                return False
            node = node.children[chr]
        return True


obj = Trie()
obj.insert('apple')
print(obj.search('apple'))
print(obj.search('app'))
print(obj.startsWith('app'))
obj.insert('app')
print(obj.search('app'))
print(obj.search('apple'))