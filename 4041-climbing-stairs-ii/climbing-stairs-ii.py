class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        """
        step  0. 1  2 3 4 ..k.. n + 1
        cost at k = costs[k-1]

        cost[0] = cost of step 1 
        cost[k-1] = cost of step k 
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            jump_1 = dp[i-1] + costs[i-1] + 1 if i - 1 >= 0 else float('inf')
            jump_2 = dp[i-2] + costs[i-1] + 4 if i - 2 >= 0 else float('inf')
            jump_3 = dp[i-3] + costs[i-1] + 9 if i - 3 >= 0 else float('inf')

            dp[i] = min(jump_1, jump_2, jump_3)
        
        return dp[-1]