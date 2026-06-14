class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        7, 1, 5, 3, 6, 4
        b
        s
        """
        memo = {}
        def get_profit(index: int, can_buy: bool) -> int:
            # check memo
            if (index, can_buy) in memo:
                return memo[(index, can_buy)]

            # Base Case
            if index >= len(prices):
                return 0
            
            # Recurse
            if can_buy:
                profit = max(-prices[index] + get_profit(index + 1, False), 
                    get_profit(index + 1, True))
            else:
                profit = max(prices[index] + get_profit(index + 1, True), 
                get_profit(index + 1, False))
            
            memo[(index, can_buy)] = profit
            return profit
        
        return get_profit(0, True)
            

