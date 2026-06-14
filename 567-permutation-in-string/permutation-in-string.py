class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s2 is query string 
        s1 is base string

        check if s1 permutations exist in s2
        - if len(s1) > len(s2): false
        - s1 -> [0, 1, 2, ....] 26 sized char array

        check in each window of size len(s1) in s2
        e, i, d,  b, a, o, o, o 
                  i
                     j

        map_s2 = [b:1, a:1]
        map_s1 = [a:1, b:1]
        a b

        Approach:
        - check in len(s1) <= len(s2)
        - build char map of s1
        - for each fixed sized rolling window of len(s1) in s2:
            - check if char map matches char map of s1
        """
        if len(s1) > len(s2):
            return False
        
        map_s1 = [0] * 26
        for char in s1:
            map_s1[ord(char) - ord("a")] += 1
        
        i = 0
        map_s2 = [0] * 26
        for j in range(len(s2)):
            map_s2[ord(s2[j]) - ord("a")] += 1
            if j - i + 1 < len(s1):
                continue
            
            if map_s1 == map_s2:
                return True
            
            map_s2[ord(s2[i]) - ord("a")] -= 1
            i += 1
        
        return False

