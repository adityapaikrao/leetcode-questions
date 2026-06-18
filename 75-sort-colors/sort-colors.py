class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1 1 2 0 2 1

        0 1 1 1 2 2
        l
              i
                r
        if r== 2: r--
            swap i & r
            i ++
        
        if l==0: l++
            swap i & l
            l ++
        """
        l = 0
        r = len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                while l < i and nums[l] == 0:
                    l += 1
                nums[l], nums[i] = nums[i], nums[l]
                # if nums[i] == 2: continue
            
            elif nums[i] == 2:
                while r > i and nums[r] == 2:
                    r -= 1
                nums[r], nums[i] = nums[i], nums[r]
                if nums[i] == 0: continue
            
            i += 1
        

        