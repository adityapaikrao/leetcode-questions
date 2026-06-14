class Solution:
    def isValid(self, s: str) -> bool:
        """
        (]) -> invalid
        ([()()] ->invalid
             i

        (->stack
        """
        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for char in s:
            if char not in bracket_map:
                stack.append(char)
                continue
            
            if not stack or stack.pop() != bracket_map[char]:
                return False
        
        return len(stack) == 0