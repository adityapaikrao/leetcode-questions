class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        a a b 
        
        max freq <= len // 2 
        
        """
        if not s: 
            return ""
        n = len(s)
        freq = {}
        maxFreq = 0
        maxChar = s[0]
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            if freq[char] > maxFreq: 
                maxFreq = freq[char]
                maxChar = char
        
        if maxFreq > (n + 1) // 2:
            return ""
        
        order = ["" for _ in range(n)]
        
        
        # place maxFreq char first
        i = 0
        while maxFreq > 0:
            order[i] = maxChar
            i += 2 
            maxFreq -= 1 
        del freq[maxChar]
        
        for char, val in freq.items():
            while val > 0:
                if i >= n:
                    i = 1
                order[i] = char
                val -= 1 
                i += 2
            
        
        return "".join(order)
            
    