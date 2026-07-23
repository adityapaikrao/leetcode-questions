class Solution:
    def minOperations(self, s: str) -> int:
        """
        1 1 1 1
              i
        p = 0
        ops = 1
        """
        prev = s[0]
        num_ops = 0
        for i in range(1, len(s)):
            if s[i] == prev:
                num_ops += 1
                prev = '1' if s[i] == '0' else '0'
            else:
                prev = s[i]
        return min(num_ops, len(s) - num_ops)