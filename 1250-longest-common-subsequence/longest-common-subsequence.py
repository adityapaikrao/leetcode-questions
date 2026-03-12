class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # memo = [[-1] * (m + 1) for _ in range(n + 1)]
        # for i in range(n + 1):
        #     memo[i][m] = 0
        # for j in range(m + 1):
        #     memo[n][j] = 0
        
        # def solve(i: int, j: int) -> int:
        #     if memo[i][j] != -1:
        #         return memo[i][j]
            
        #     # Base Case: either of strings is empty
        #     if j == m or i == n:
        #         return 0
            
        #     if text1[i] == text2[j]:
        #         memo[i][j] = 1 + solve(i + 1, j + 1)
        #         return memo[i][j]
        #     else:
        #         memo[i][j] = max(solve(i + 1, j), solve(i, j + 1))
        #         return memo[i][j]
        
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][m] = 0
        for j in range(m + 1):
            dp[n][j] = 0
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]
            
            
        