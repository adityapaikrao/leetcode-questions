"""
b -> a -> k -> END
       -> d -> END
  -> c -> z -> END

b . z
"""


class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char] 
        node['end'] = True

    def search(self, word: str) -> bool:
        n = len(word)
        def search_trie(node: dict[str, dict], index: int) -> bool:
            if index == n:
                return 'end' in node
            
            if word[index] == ".":
                for next_char in node:
                    if next_char == 'end': continue
                    if search_trie(node[next_char], index + 1): 
                        return True
                return False
            elif word[index] not in node:
                return False
            else:
                return search_trie(node[word[index]], index + 1)
        
        
        return search_trie(self.root, 0)
        
        
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)