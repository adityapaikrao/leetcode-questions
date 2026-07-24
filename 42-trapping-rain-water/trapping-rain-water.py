class Solution:
    def trap(self, height: List[int]) -> int:
        """
        4 2 0 3 6 5
        0 2 4 1 0 0
                  l
                r
        lmax = 4
        rmax = 5
        each bar can only trap min(lmax, rmax) - itself


        """
        lmax, rmax = height[0], height[-1]
        l, r = 0, len(height) - 1
        water = 0

        while l <= r:
            if lmax <= rmax:
                water += max(lmax - height[l], 0)
                lmax = max(lmax, height[l])
                l += 1
            else:
                water += max(rmax - height[r], 0)
                rmax = max(rmax, height[r])
                r -= 1
        
        return water

