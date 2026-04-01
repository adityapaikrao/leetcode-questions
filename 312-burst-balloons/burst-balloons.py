class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        new_nums = [1]
        new_nums.extend(nums)
        new_nums.append(1)

        # memo = {}

        # def solve(start: int, end: int) -> int:
        #     if (start, end) in memo:
        #         return memo[(start, end)]
        #     # Base Case:
        #     if start > end:
        #         return 0
            
        #     # Recurrence
        #     # Choose which balloon to burst last
        #     max_coins = 0
        #     for i in range(start, end + 1):
        #         coins = new_nums[start - 1] * new_nums[i] * new_nums[end + 1]
        #         max_coins = max(solve(start, i - 1) + solve(i + 1, end) + coins, max_coins)

        #     memo[(start, end)] = max_coins    
        #     return max_coins
        
        # return solve(1, len(nums))
        
        dp = [[0] * len(new_nums) for _ in range(len(new_nums))]

        for i in range(len(nums), -1, -1):
            for j in range(i, len(nums) + 1):
                for k in range(i, j + 1):
                    coins = new_nums[i-1] * new_nums[k] * new_nums[j + 1]
                    dp[i][j] = max(dp[i][k-1] + dp[k + 1][j] + coins, dp[i][j])
        
        return dp[1][len(nums)]
