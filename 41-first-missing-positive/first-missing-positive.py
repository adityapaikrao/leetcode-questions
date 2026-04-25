class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        3 4 -1 1 : -> 2
        1 2 0: -> 3

        ideally should have numbers 1 2 3 ... n for n length array [1, n]
        use indices to mark

        -3 -4 -1 1
        0 1  2 3

        mark 3 is present at index 3 - 1: 2 convert num at 2 to negative 

        -1 -2 0
        0 1 2 -> works

        3 2 1 5
        0 1 2 3 

        how do we know the number was "marked" negative vs actually negative number
        - first pass convert all zeros & negatives to n + 1
        - second pass: mark nums[nums[i] - 1] to negative
        - third pass: check i where nums[i] > 0; then answer is i + 1
        if no such i found then return n + 1
        
        i
        -3 4 -5 -1
        0 1 2  3
        """
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            if abs(nums[i]) <= n and nums[abs(nums[i]) - 1] > 0: 
                nums[abs(nums[i]) - 1] *= -1

        for i in range(n):
            if nums[i] > 0: return i + 1
        
        return n + 1