class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        """
        [3, 5, 7]

        - generate all subarrays
        - for each subarray basically check the max score from it
            - gcd(subrray) 
            - if count min power of 2s <= k => effective gcd = gcd * 2
            - update max score if possible  
        """
        n = len(nums)
        max_score = 0

        powersTwo = []
        for num in nums:
            power = 0
            while num % 2 == 0:
                num >>= 1
                power += 1
            powersTwo.append(power)

        for start in range(n):
            curr_gcd = 0
            min_power, min_count = float('inf'), 0

            for end in range(start, n):
                curr_gcd = gcd(curr_gcd, nums[end])
                power = powersTwo[end]
                
                if power == min_power: min_count += 1
                elif power < min_power: min_power, min_count = power, 1
                max_score = max(
                    max_score,
                    (end - start + 1) * curr_gcd * (2 if min_count <= k else 1)
                )
        return max_score