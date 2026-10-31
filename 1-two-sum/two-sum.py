class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        nums = [2,7,11,15], target = 9 -> [0, 1]
                i
                  j.  -> O(n2)
        
        hmap = {} num -> index

        [2,7,11,15], target = 9 -> [0, 1]
           i
           9 - 7 in hmap? return (i, hmap[9 - 7]) else add 7 to hmap
        hmap {2:0}

        """
        hmap = {} # number -> index
        for i, num in enumerate(nums):
            if target - num in hmap:
                return [hmap[target - num], i]    
            hmap[num] = i
        