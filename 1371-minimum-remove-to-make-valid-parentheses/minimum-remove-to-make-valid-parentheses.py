class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        
        l e e ( t ( c ) o ) d e )
              i

        - maintain stack of indices of (
        - when ):
            if stack empty: mark s[i] = ""
            else: pop from stack
        - when (:
            append to stack

        for all remaining indices: mark s[i] = ""
        stack = []
        """

        stack = []
        s = list(s)

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if not stack:
                    s[i] = ""
                else:
                    stack.pop()
        
        while stack:
            s[stack.pop()] = ""
        
        return "".join(s)
