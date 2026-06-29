class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        0 3 2 0 -1
        1 0 0 0  0
        0 0 0 -1  1
        prev = 0
        """
        prod = []
        prev = 1
        for num in nums:
            prod.append(prev)
            prev *= num
        
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            prod[i] *= prev
            prev *= nums[i]
        
        return prod

            

        