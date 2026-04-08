class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        [10, 6, 8, 5, 11, 9]
          i
        
        s [11, 10]
        [1, 1, 2, 1, 1, 0]

        [4, 3, 2, 1]

        [1, 1, 1, 0]

        """
        n = len(heights)
        ans = [0] * n
        ans[-1] = 0
        stack = []

        for i in range(n - 1, -1, -1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
            
            ans[i] += count + (1 if stack else 0)
            stack.append(heights[i])
        
        return ans
