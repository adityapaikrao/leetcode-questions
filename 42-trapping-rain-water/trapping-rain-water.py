class Solution:
    def trap(self, height: List[int]) -> int:
        """
        lmax 0
        rmax 1

        0,1,0,2,1,0,1,3,2,1,2,1
          i
                            j

        if lmax <= rmax: water += lmax - height[i]; i++; lmax = max(lmax, hieght[i])

        """
        lmax = height[0]
        rmax = height[-1]

        i = 1
        j = len(height) - 2
        water = 0

        while i <= j:
            if lmax <= rmax:
                if lmax >= height[i]: water += lmax - height[i]  
                else: lmax = height[i]
                i += 1
            else:
                if rmax >= height[j]: water += rmax - height[j]  
                else: rmax = height[j]
                j -= 1
        
        return water
