class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        num = 0
        i = 0
        curr_prod = 1

        for j in range(len(nums)):
            curr_prod *= nums[j]

            while i <= j and curr_prod >= k:
                curr_prod = curr_prod // nums[i]
                i += 1
            
            num += (j - i + 1)
        
        return num
            