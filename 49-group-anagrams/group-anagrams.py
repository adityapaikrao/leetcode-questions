class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        eat tea tan ate nat bat

        bat  nat, tan   ate, tea, eat

        anagram -> same chars with same frequency 
        eat: e1, a1, t1 -> [1, 0, 0, 0, 1,.....1,, ] 26-length char & store it in map
        tea: t1 e1 a1
        anagrams = []
        """

        hmap = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            hmap[tuple(freq)].append(word)
        
        return list(hmap.values())