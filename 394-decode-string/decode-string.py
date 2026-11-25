class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curr = []
                while stack[-1] != "[":
                    curr.append(stack.pop())
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num 
                stack.append(int(num) * ''.join(curr[::-1]))
        
        return ''.join(stack)

                
                
                
