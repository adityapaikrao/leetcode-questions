class Node:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False

class Trie:

    def __init__(self):
        self._root = Node()        

    def insert(self, word: str) -> None:
        node = self._root
        for char in word:
            if not node.links[ord(char) - ord('a')]:
                node.links[ord(char) - ord('a')] = Node()
            node = node.links[ord(char) - ord('a')]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._root
        for char in word:
            if not node.links[ord(char) - ord('a')]: return False
            node = node.links[ord(char) - ord('a')]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self._root
        for char in prefix:
            if not node.links[ord(char) - ord('a')]: return False
            node = node.links[ord(char) - ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)