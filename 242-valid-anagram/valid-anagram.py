class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. same letters & same freq of letters

        for s:
            array_s = [0] * 26 -> freq of each letter
        
        for t:
            array_t = [0] * 26 -> freq of chars
        
        return array_s == array_t

        """
        return sorted(s) == sorted(t)