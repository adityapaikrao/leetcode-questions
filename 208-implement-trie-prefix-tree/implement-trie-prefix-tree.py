class TrieNode:
    def __init__(self):
        self.chars = [None] * 26
        self.is_end = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.chars[ord(char) - ord('a')] is None:
                node.chars[ord(char) - ord('a')] = TrieNode()
            node = node.chars[ord(char) - ord('a')]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node.chars[ord(char) - ord('a')] is None: return False
            node = node.chars[ord(char) - ord('a')]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if node.chars[ord(char) - ord('a')] is None: return False
            node = node.chars[ord(char) - ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)