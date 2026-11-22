class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        """ 
        - build Trie of root words O(R * L)
        - for each word in sentence
            - see if any root is prefix O(L)
            - if yes, replace with the smallest prefix O(1)
        
        c -> a - > t -> end
                        n
        """
        trie_root = {}
        for root_word in dictionary:
            node = trie_root
            for char in root_word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['end'] = True
        
        def has_prefix(trie_root: dict[str, dict], word: str) -> str:
            node = trie_root
            for i, char in enumerate(word):
                if char not in node: 
                    return ''
                node = node[char]
                if 'end' in node:
                    return word[:i + 1]
            return ''
        
        words = sentence.split()
        for i, word in enumerate(words):
            smallest_root = has_prefix(trie_root, word)
            if smallest_root != '':
                words[i] = smallest_root
        return ' '.join(words)
