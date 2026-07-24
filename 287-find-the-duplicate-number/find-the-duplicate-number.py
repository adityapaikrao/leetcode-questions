class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        1 3 4 2 2 

        # cycle sort
        1 2 3 4 2 
                i

        correct idx = numsi[i] - 1
        if nums[i] == i + 1:
            i += 1
        else:
            if nums[correct_idx] == 2: this is duplicate
            swap i & correct idx
        """

        i = 0 
        while i < len(nums):
            correct_idx = nums[i] - 1
            if i == correct_idx:
                i += 1
            else:
                if nums[correct_idx] == nums[i]:
                    return nums[i]
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        return -1