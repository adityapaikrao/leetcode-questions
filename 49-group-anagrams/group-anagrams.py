class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        for every string -> sort it & check which other strings have same sorted results
        group them together

        map = {} # string -> sortedString
        map = {} # sortedString -> string

        N  * mlogM

        string -> char_freq eat -> [a:1, e:1, t:1] ->hashable type Tuple [1,0, 0, 0, 1...] * 26
                            tea -> [a:1, e:1, t:1]
        
        ["eat","tea","tan","ate","nat","bat"]
           i

        hmap = {} # char_freq = []strings
        """
        char_freqs = defaultdict(list)
        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            char_freqs[tuple(freq)].append(string)
        
        return [anagrams for anagrams in char_freqs.values()]