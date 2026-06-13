class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        0 1 0 0 
        1 1 1 0

        1 0 1 0 -> count ones
        """
        counts = {}
        hamming_sum = 0
        for i in range(32):
            counts[i] = [0, 0]
            for num in nums:
                counts[i][(num >> i) & 1] += 1
            hamming_sum += counts[i][0] * counts[i][1]
        return hamming_sum