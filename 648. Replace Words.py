class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_shortest_prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix += char
            if node.is_end_of_word:
                return prefix
        return word

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        
        words = sentence.split()
        replaced_sentence = []
        for word in words:
            replaced_sentence.append(trie.search_shortest_prefix(word))
        
        return ' '.join(replaced_sentence)

# Example usage:
dictionary = ["catt", "cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
solution = Solution()
output = solution.replaceWords(dictionary, sentence)
print(output)  # Output: "the cat was rat by the bat"