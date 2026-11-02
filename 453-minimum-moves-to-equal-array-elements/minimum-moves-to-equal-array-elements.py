class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_elem = min(nums)
        return sum(num - min_elem for num in nums)