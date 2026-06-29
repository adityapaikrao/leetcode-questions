class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1 3 4 5 0
                i



        """
        prev = -1
        for i in range(len(nums)):
            if nums[i] != 0 and prev != -1:
                nums[prev], nums[i] = nums[i], nums[prev]
                prev += 1
            elif nums[i] == 0 and prev == -1:
                prev = i
        
        return
        