class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        10, 5, 2, 6
            i
               j

        -increase until < k
        -greater than or eq k: then add (j - i) * (j - i  + 1) / 2:
            divide by i until >= k

        if curr_prod < k: count += j - i)

        2 200  3
               i
               j
        """
        count = 0
        curr_prod = 1
        i = 0

        for j in range(len(nums)):
            curr_prod *= nums[j]
            if curr_prod < k:
                count += (j - i + 1)
                continue
            
            while i <=j and curr_prod >= k:
                curr_prod = curr_prod // nums[i]
                i += 1
            if i <= j: count += (j - i + 1)
        return count
            