class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        0 1 0 0 
        1 1 1 0

        1 0 1 0 -> count ones
        """
        hamming_sum = 0
        for i in range(32):
            ones = 0
            for num in nums:
                if (num >> i) & 1: ones += 1
            hamming_sum += ones * (len(nums) - ones)
        return hamming_sum