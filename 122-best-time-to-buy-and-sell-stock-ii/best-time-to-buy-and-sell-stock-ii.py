class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        7, 1, 5, 3, 6, 4
        
        2 - 1 + 3 - 2 = 3 - 1
        """
        prev = float('inf')
        profit = 0

        for num in prices:
            if num > prev:
                profit += num - prev
            prev = num
        
        return profit