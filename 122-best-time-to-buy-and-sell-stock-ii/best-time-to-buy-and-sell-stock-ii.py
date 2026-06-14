class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        7, 1, 5, 3, 6, 4
        b
        s
        """
        # memo = {}
        # def get_profit(index: int, can_buy: bool) -> int:
        #     # check memo
        #     if (index, can_buy) in memo:
        #         return memo[(index, can_buy)]

        #     # Base Case
        #     if index >= len(prices):
        #         return 0
            
        #     # Recurse
        #     if can_buy:
        #         profit = max(-prices[index] + get_profit(index + 1, False), 
        #             get_profit(index + 1, True))
        #     else:
        #         profit = max(prices[index] + get_profit(index + 1, True), 
        #         get_profit(index + 1, False))
            
        #     memo[(index, can_buy)] = profit
        #     return profit
        
        # return get_profit(0, True)
        
        dp = [[0] * 2 for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            dp[i][0] = max(dp[i + 1][1] -prices[i], dp[i + 1][0])
            dp[i][1] = max(dp[i + 1][0] + prices[i], dp[i + 1][1])
        
        return dp[0][0]

