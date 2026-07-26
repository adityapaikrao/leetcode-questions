class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        2 1 + 3 *
        = 3 * (2 + 1) 

        4 13 5 / +
        = 4 + (13 / 5)


        stack = [4, 2, +]
        eval = 0

        if operator:
            pop two nums from stack, compute & add to stack
        else:
            add num to stack

        """
        stack = []
        for token in tokens:
            if token == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif token == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif token == "*":
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif token == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(token))
        
        return stack[-1]