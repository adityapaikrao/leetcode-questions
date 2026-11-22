
class TrieNode:
    def __init__(self):
        self.chars = [None] * 26
        self.is_end = False
    
class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        """
        ["mobile","mouse","moneypot","monitor","mousepad"]
        mouse
          i
        
        at each i:
            0: mobile, moneypot, monitor
            1: mobile, moneypot, monitor
            2: mouse, mousepad
            ...

        - at each char (Q)
        - find strings with prefix matching query N
        - sort lexicorgraphically NlogN * L
        - pick top 3 1

        O(Q * NlogN * L)

        repetiive work

        - build catalog using Tries O(N * L)
        - proceed query chars through the trie
                 j
                                                k
         root -> m -> o -> b -> i -> l -> e -> END
                        -> u -> s -> e -> END   
                                       -> p -> a -> d END
                        -> n -> e -> y -> p -> o -> t -> END
                             -> i -> t -> o -> r -> END
        
        m o u s e
        i
                        
        """
        # Build a Trie
        root = TrieNode()
        for product in products:
            node = root
            for char in product:
                if node.chars[ord(char) - ord('a')] is None:
                    node.chars[ord(char) - ord('a')] = TrieNode()
                node = node.chars[ord(char) - ord('a')]
            node.is_end = True
        
        def dfs(curr_node: TrieNode):
            nonlocal all_words
            if curr_node.is_end:
                all_words.append(''.join(curr_word[:]))
            
            for i in range(26):
                if curr_node.chars[i] is not None:
                    curr_word.append(chr(ord('a') + i))
                    dfs(curr_node.chars[i])
                    curr_word.pop()
            
            return 
        
        suggestions = []
        curr_word = []
        node = root
        for char in searchWord:
            curr_word.append(char)
            if node.chars[ord(char) - ord('a')] is None:
                break
            
            next_node = node.chars[ord(char) - ord('a')]
            all_words = []
            dfs(next_node)
            suggestions.append(sorted(all_words)[:3])
            node = next_node
        
        while len(suggestions) < len(searchWord):
            suggestions.append([])
        return suggestions