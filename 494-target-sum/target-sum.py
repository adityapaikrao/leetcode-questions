class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def solve(index: int, curr_sum: int) -> int:
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            
            # Base Case: no more numbers to add
            if index == n:
                if curr_sum == target:
                    memo[(index, curr_sum)] = 1
                    return 1
                else:
                    memo[(index, curr_sum)] = 0
                    return 0
            
            # Recurrence
            pos = solve(index + 1, curr_sum + nums[index])
            neg = solve(index + 1, curr_sum - nums[index])
            memo[(index, curr_sum)] = pos + neg
            return pos + neg
        
        return solve(0, 0)