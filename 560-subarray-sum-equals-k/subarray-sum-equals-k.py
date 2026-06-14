class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:
        """
        [1, 2, 3, -3, 6, 0, 3]
                      i

        hmap_sum = {0:1, 1:1, 3:2, 6:1
        }
        curr_sum = 9

        count = 0 + 1 + 1 + 1 + 1
        """
        hmap_sum = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            if curr_sum - target in hmap_sum:
                count += hmap_sum[curr_sum - target]
            hmap_sum[curr_sum] = hmap_sum.get(curr_sum, 0) + 1
        
        return count