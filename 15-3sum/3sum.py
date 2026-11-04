class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        [-1, 0, 1]
          
        [-1, 0, 1, 2, -1, -4, 1, 0, -1]
          i  j.    k

        [-4, -1, -1 -1, 0, 1, 2, 2].  -> [-1, -1, 2]
              i
                     j
                              k
        for every i 
            - fix j at i + 1 and k at n - 1

            - while j < k:
                if n[j] + n[k] > -n[i]:
                    k --
                elif less:
                    j ++
                equal:
                    increase j until new val != prev val
                    decrease k  until new val != prev val
        [-4, -1, -1, 0, 1, 2].
                  i
                        j
                     k
        
        curr_sum = 0
        [-1, -1, 2], [-1, 0, 1]
        """
        triplets = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            if i > 0 and nums[i] == nums[i-1]: continue
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum > 0:
                    k -= 1
                elif curr_sum < 0:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]: j += 1
                    
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]: k -= 1
        
        return triplets