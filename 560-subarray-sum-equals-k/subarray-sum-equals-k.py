class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
          [1, 1, 1] nums
           i
        [0,1, 2, 3] prefix
        """
        prefix = [0] * (len(nums) + 1)
        hmap = defaultdict(int) # prefix_sum -> counts
        hmap[0] = 1 
        count = 0

        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num
            if prefix[i + 1] - k in hmap:
                count += hmap[prefix[i + 1] - k]
            hmap[prefix[i + 1]] += 1
        return count
        
        

