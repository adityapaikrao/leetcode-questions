class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0] * (2*k + 1) for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            for j in range(1, 2*k + 1):
                if j % 2 != 1:
                    dp[i][j] = max(
                        dp[i + 1][j], dp[i + 1][j - 1] -prices[i]
                    )
                else:
                    dp[i][j] = max(
                        dp[i + 1][j], dp[i + 1][j - 1] + prices[i]
                    )
        return dp[0][2*k]