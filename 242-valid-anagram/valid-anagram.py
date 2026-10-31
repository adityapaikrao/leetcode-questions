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
        array_s = [0] * 26
        for char in s:
            array_s[ord(char) - ord('a')] += 1
        
        for char in t:
            array_s[ord(char) - ord('a')] -= 1
        
        return all(num == 0 for num in array_s)
        