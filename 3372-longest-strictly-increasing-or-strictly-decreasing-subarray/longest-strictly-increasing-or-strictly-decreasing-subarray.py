class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incr_len = 1
        max_len = 1
        decr_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                incr_len += 1
            else:
                max_len = max(max_len, incr_len)
                incr_len = 1
            
            if nums[i] < nums[i-1]:
                decr_len += 1
            else:
                max_len = max(max_len, decr_len)
                decr_len = 1
        
        max_len = max(decr_len, incr_len, max_len)
        return max_len

        