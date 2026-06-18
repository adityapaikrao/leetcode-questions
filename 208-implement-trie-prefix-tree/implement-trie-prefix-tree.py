class Node:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False
    
    def isEnd(self) -> bool:
        return self.is_end
    
    def setEnd(self):
        self.is_end = True
    
    def hasChar(self, char: str) -> bool:
        return (self.links[ord(char) - ord('a')] is not None)
    
    def addChar(self, char: str):
        self.links[ord(char) - ord('a')] = Node()
    
    def getCharNode(self, char: str) -> Optional[Node]:
        if not self.hasChar(char): return None
        return self.links[ord(char) - ord('a')]

class Trie:

    def __init__(self):
        self._root = Node()        

    def insert(self, word: str) -> None:
        node = self._root
        for char in word:
            if not node.hasChar(char):
                node.addChar(char)
            node = node.getCharNode(char)

        node.setEnd()

    def search(self, word: str) -> bool:
        node = self._root
        for char in word:
            if not node.hasChar(char): return False
            node = node.getCharNode(char)
        return node.isEnd()

    def startsWith(self, prefix: str) -> bool:
        node = self._root
        for char in prefix:
            if not node.hasChar(char): return False
            node = node.getCharNode(char)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)