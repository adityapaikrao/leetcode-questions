class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [3, 3, 5, 0, 0, 3, 1, 4]
         4
        """

        # def get_profit(index: int, op: int) -> int:
        #     # Base Case
        #     if op == 0 or index >= len(prices):
        #         return 0
            
        #     # Recurse
        #     if op % 2 != 1: # can buy
        #         profit = max(
        #             -prices[index] + get_profit(index + 1, op - 1),
        #             get_profit(index + 1, op)
        #         )
        #     else:
        #         profit = max(
        #             prices[index] + get_profit(index + 1, op - 1),
        #             get_profit(index + 1, op)
        #         )
            
        #     return profit
        
        # return get_profit(0, 4)

        dp = [[0] * 5 for _ in range(len(prices) + 1)]
        for i in range(len(prices) -1, -1, -1):
            for j in range(1, 5):
                if j % 2 != 1:
                    dp[i][j] = max(
                        dp[i + 1][j], dp[i + 1][j-1] - prices[i]
                    )
                else:
                    dp[i][j] = max(
                        dp[i + 1][j], dp[i + 1][j - 1] + prices[i]
                    )
        return dp[0][4]
        