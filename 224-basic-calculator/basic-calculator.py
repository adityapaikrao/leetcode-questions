class Solution:
    def calculate(self, s: str) -> int:
        """
        (1 + (4 + 11) - 3)
                         i
        
        s = [0, 1]
        ans = 13
        num = 0
        op = 1 

        if (:
            - add prev & op to stack
            - set ans & num to 0
        if num:
            - convert num to num * 10 + digit        
        if +:
            - add num * op to ans
            - set num to 0
            - set op = 1
        if ):
            - add num * op to ans
            - set num to 0

            - stack pop to get prev res: but how to know if it was x + (exp) or x - (exp)?
                - stack needs to store the operation as well for the prev
            
            - prev, sign = stack.pop() twice
            - ans = prev + sign * sign
        """

        stack = []
        num = 0
        ans = 0
        op = 1

        for char in s:
            if char == " ": continue
            if char == ")":
                ans += num * op
                num = 0

                sign = stack.pop()
                prev = stack.pop()
                ans = prev + sign * ans

            elif char == "(":
                stack.extend([ans, op])
                num = 0
                ans = 0
                op = 1
            
            elif char == "+":
                ans += op * num
                num = 0
                op = 1
            
            elif char == "-":
                ans += op * num
                num = 0
                op = -1
            else:
                num = num * 10 + int(char)
        
        return ans + num * op

        