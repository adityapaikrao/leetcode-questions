class Solution:
    def minOperations(self, s: str) -> int:
        """
        0 1 0 0 -> 0 1 0 1 (1) OR 1 0 1 0 (3)
        0 0 1 0 -> 0 1 0 1 (3) OR 1 0 1 0 (1)
        """
        ops = 0
        prev = s[0]
        for i in range(1, len(s)):
            if s[i] == prev:
                # need to change 
                ops += 1
                prev = '0' if s[i] == '1' else '1'
            else:
                prev = s[i]
            
        return min(ops, len(s) - ops)