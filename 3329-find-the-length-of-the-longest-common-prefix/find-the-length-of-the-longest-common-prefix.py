class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}
        for num in arr1:
            node = trie
            string = str(num)
            for char in string:
                if char not in node:
                    node[char] = {}
                node = node[char]
        
        longest = 0

        for num in arr2:
            node = trie
            string = str(num)
            for i in range(len(string)):
                if string[i] not in node:
                    break
                longest = max(longest, i + 1)
                node = node[string[i]]
        
        return longest

