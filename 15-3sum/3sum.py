class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        n = len(nums)
        nums.sort()


        for i in range(n - 2):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]: continue
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum > 0:
                    k -= 1
                elif curr_sum < 0:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    # skip same number on left
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    
                    # skip same number on right
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
        
        return triplets
                