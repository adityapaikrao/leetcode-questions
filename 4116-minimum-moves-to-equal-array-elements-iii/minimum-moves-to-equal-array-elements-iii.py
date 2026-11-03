class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_elem = max(nums)
        return sum(max_elem - num for num in nums)