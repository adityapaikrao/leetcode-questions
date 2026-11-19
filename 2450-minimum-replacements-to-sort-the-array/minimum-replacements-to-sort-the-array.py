class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        """
        3, 9, 3
        9 -> 6, 3 -> 3, 3, 3
        ceil(curr / next) = 3 => 2 splits
        max of these = curr // #nums



        3, 10, 3
        10 -> 3, 7 -> 3, 3, 4 -> 3, 3, 3, 1 => 3 splits
        ceil(curr / next) - 1 
        max of these = cur // nums

        14 -> 3, 11 -> 3, 3, 8 -> 3, 3, 3, 5 -> 3, 3, 3, 3, 2 
        4 splits
        min of these cur % next
        """
        n = len(nums)
        curr_max = nums[-1]
        splits = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > curr_max:
                k = (nums[i] // curr_max) + (1 if nums[i] % curr_max != 0 else 0)
                splits += k - 1
                curr_max = nums[i] // k
            else:
                curr_max = nums[i]
        return splits
        
