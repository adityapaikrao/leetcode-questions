class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [height[0]]
        lmax = height[0]

        for i in range(1, len(height)):
            left_max.append(lmax)
            if height[i] > lmax: lmax = height[i]
        
        right_max = [height[-1]]
        rmax = height[-1]

        for i in range(len(height) - 2, -1, -1):
            right_max.append(rmax)
            if height[i] > rmax: rmax = height[i]
        
        right_max.reverse()

        water = 0

        for i in range(1, len(height) - 1):
            water += max(0, min(left_max[i], right_max[i]) - height[i])
        
        return water