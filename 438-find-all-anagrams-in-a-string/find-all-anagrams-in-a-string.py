class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        s = "c b a e b a b a c d"
        
        p = "a b c" 

        freq = {a: 1, b: 1, c: 1}


        """
        p_freq = [0] * 26
        for char in p:
            p_freq[ord(char) - ord('a')] += 1
        
        start = 0
        n = len(s)
        s_freq = [0] * 26
        starts = []
        for end in range(n):
            s_freq[ord(s[end]) - ord('a')] += 1
            if end - start + 1 < len(p):
                continue
            else:
                if s_freq == p_freq:
                    starts.append(start)
                s_freq[ord(s[start]) - ord('a')] -= 1
                start += 1
        
        if s_freq == p_freq: starts.append(start)
        return starts

            
                
                