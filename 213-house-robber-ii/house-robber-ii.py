class Solution:


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_houses(houses: List[int]) -> int:
            if len(houses) == 0:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            prev2, prev1 = houses[0], max(houses[0], houses[1])
            for i in range(2, len(houses)):
                prev2, prev1 = prev1, max(prev1, houses[i] + prev2)
            
            return prev1

        return max(rob_houses(nums[:-1]), rob_houses(nums[1:]))

        