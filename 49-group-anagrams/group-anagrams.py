class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            char_counts = [0] * 26
            for char in word:
                char_counts[ord(char) - ord("a")] += 1
            anagrams[tuple(char_counts)].append(word)
        
        return [words for words in anagrams.values()]