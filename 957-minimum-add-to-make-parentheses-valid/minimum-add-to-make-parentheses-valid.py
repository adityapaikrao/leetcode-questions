class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        num_unmatched = 0
        num_opens = 0

        for char in s:
            if char == "(":
                num_opens += 1
            else:
                if num_opens > 0:
                    num_opens -= 1
                else:
                    num_unmatched += 1
        
        return num_unmatched + num_opens