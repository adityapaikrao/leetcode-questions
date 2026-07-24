class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        0 2 1 5 3 4 -> 0 1 2 4 5 3
        i
        
        

        """
        n = len(nums)
        for i in range(n):
           x = nums[nums[i]]
           nums[i] = nums[i] + (n * (x % n))
        
        return [num // n for num in nums]
            