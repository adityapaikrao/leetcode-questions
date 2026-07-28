class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        [1,8,6,2,5,4,8,3,7]
         i
                         j
        
        - max water it can store = min of its (height, other end) * (distance between them)
        - if height_i < other end: i++ -> because even if we find a taller building on right
            water stored would be lesser because height * new_width where new_width < width
        - 
        Output: 49
        """
        max_water = 0
        i = 0
        j = len(height) - 1

        while i < j:
            water = (j - i) * min(height[i], height[j])
            max_water = max(water, max_water)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return max_water        
        