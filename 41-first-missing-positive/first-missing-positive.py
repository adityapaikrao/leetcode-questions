class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        3 4 -1 1

        cycle sort 
        3 4 -1 1
        1 4 3 -1
        """
        i = 0
        n = len(nums)

        while i < len(nums):
            correct_idx = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1