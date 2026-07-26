class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        1 2 0 -> 3
        3 4 -1 1 -> 2

        ideally should have numbers 1 to n
        1 2 3 4 -> then missing = n + 1

        0 1 2 3 indices every index -> if index + 1 exists in arr
        1 2 3 4

        one_present = True
        3 4 -1 1
        -> 3 4 -1 -1

        1 2 0
        -1 -2 0
        -> 
        
        2 1 
        -2 -1
        """
        n = len(nums)
        one_present = False
        for i in range(n):
            if nums[i] == 1:
                one_present = True
            if nums[i] <= 0:
                nums[i] = 1
        
        if not one_present:
            return 1
        
        for i in range(n):
            if 1 <= abs(nums[i]) <= n:
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1
       
        for i in range(1, n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1