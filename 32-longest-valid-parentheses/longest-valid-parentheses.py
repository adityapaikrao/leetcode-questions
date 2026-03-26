class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        "" or "(" or ")"-> 0

        "()"
         
         s = []

         c +1 *2

         )()())
              i
         s = []

         c +1 +1
         max_c =
         if curr = (: push in stack; continue
         if curr = ):
            stack empty: -> reset c = 0
         else c++

         ()(() -> wont work here need to somehow track the discontinuity 
         s
        """
        if len(s) <= 1:
            return 0
        
        stack = []
        left_wall = -1
        max_len = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                if not stack:
                    left_wall = i
                else:
                    stack.pop()
                    left = stack[-1] if stack else left_wall
                    max_len = max(max_len, i - left)
        
        return max_len

