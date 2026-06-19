class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        min_sum = float('inf')

        curr_max = 0
        curr_min = 0
        for num in nums:
            curr_max += num
            curr_min += num
            if curr_max > max_sum:
                max_sum = curr_max
            if curr_max < 0:
                curr_max = 0
            
            if curr_min < min_sum:
                min_sum = curr_min
            if curr_min > 0:
                curr_min = 0
        
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, sum(nums) - min_sum)