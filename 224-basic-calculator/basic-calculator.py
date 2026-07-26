class Solution:
    def calculate(self, s: str) -> int:
        """
        1+(4+5+2)-3+(6+8)
                i 

        eval = 0 + 4 + 5 + 2
        

        stack = [1, +]

        if "(":
            stack + [eval, op]
            eval = 0        
            op = +1
        if +, -:
            eval += num * op
            op = -1
            num = 0
        if ):
            prev, prev_op = stack.pop() twice
            eval = prev + prev_op * num
            num = 0
            op = 1
        else:
            num = num * 10 + digit

        """
        stack = []
        num = 0
        op = 1
        result = 0

        for char in s:
            if char == " ": continue
            elif char == "+":
                result += num * op
                num = 0
                op = 1
            elif char == "-":
                result += num * op
                num = 0
                op = -1
            elif char == "(":
                stack.extend([result, op])
                num = 0
                result = 0
                op = 1
            elif char == ")":
                result += num * op
                prev_op, prev_res = stack.pop(), stack.pop()
                result = prev_res + prev_op * result
                num = 0
                op = 1
            else:
                num = num * 10 + int(char)
        
        return result + num * op