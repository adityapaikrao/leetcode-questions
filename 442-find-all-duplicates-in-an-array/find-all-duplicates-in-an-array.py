class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        4,3,2,7,8,2,3,1
        
        7,3,2,4,8,2,3,1
        3,3,2,4,8,2,7,1
        2,3,3,4,8,2,7,1
        3,2,3,4,8,2,7,1

        -> 1 2 2 3 3 4 7 8
           0 1 2 3 4 5 6 7
        """
        i = 0
        while i < len(nums):
            correct_idx = nums[i] - 1
            if nums[correct_idx] == nums[i]:
                i += 1
            else:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        dups = []
        for i in range(len(nums)):
            if i != nums[i] - 1:
                dups.append(nums[i])

        return dups