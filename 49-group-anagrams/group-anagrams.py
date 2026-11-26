class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list) # char_freq -> list words
        for string in strs:
            char_freq = [0] * 26
            for ch in string:
                char_freq[ord(ch) - ord('a')] += 1
            anagrams[tuple(char_freq)].append(string)
        
        return list(anagrams.values())