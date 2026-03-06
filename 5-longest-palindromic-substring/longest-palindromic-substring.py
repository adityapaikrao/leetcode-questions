class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = 1
        start = 0
        
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        for i in range(1, n):
            if s[i-1] == s[i]:
                dp[i-1][i] = True
                longest = 2
                start = i - 1
        
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if k > longest:
                        longest = k
                        start = i
        return s[start: start + longest]

        
