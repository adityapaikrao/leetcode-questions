class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
          [1, 1, 1] nums
           i
        [0,1, 2, 3] prefix
        """
        # prefix = [0] * (len(nums) + 1)
        curr_sum = 0
        hmap = {0: 1} # prefix_sum -> counts
        count = 0

        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum - k in hmap:
                count += hmap[curr_sum - k]
            hmap[curr_sum] = hmap.get(curr_sum, 0) + 1
        return count
        
        

