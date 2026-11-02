class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        median = nums[n // 2]

        moves = 0
        for num in nums:
            moves += abs(num - median)
        return moves
        