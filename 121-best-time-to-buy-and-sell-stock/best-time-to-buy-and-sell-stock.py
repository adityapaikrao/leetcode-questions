class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        [7, 1, 5, 3, 6, 4]
                        i
        curr_max = -inf
        max_profit = max(max_profit, curr_max - prices[i])
        curr_max = max(curr_max, prices[i])
        
        choose to buy on day i => max profit = prices[max_i] - prices[i]
        max_i = max to right of i 

        [5,  90,  1, 4]
        """
        curr_max = float('-inf')
        max_profit = 0

        for j in range(len(prices) -1, -1, -1):
            if curr_max - prices[j] > max_profit:
                max_profit = curr_max - prices[j]
            curr_max = max(curr_max, prices[j])
        
        return max_profit