class Solution:
    """
    1. 1

    0 1 2 3 4 5 6 7 8
    1 8 6 2 5 4 8 3 7
      i       
                    j
    
    water = (j-i) * min(h[i], h[j])
    water = 8
    
    max water = 8

    if h[i] <= h[j]: i++ because any smaller width will always store less water than curr
    likewise if h[j] < h[i]: j--

    """
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height) - 1

        water = max_water = 0

        while i < j:
            water = (j - i) * min(height[i], height[j])
            if water > max_water: max_water = water

            if height[i] <= height[j]: i += 1
            else: j -= 1

        return max_water