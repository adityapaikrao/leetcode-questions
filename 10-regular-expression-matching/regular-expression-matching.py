class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        . -> any char
        * -> zero or more of preceeding elem

        .* -> matches anything

        a a a
        i 
        . * 
        j

        if p[j + 1] == "*":
            if p[j] != s[i] and p[j] != '.' : (i, j + 2)
            else:
                (i, j + 2) or (i + 1, j) 
        if p[j] == s[i] or p[j] == '.':
            (i + 1, j + 1)
        else:
            false
        c
        i
        c * d * e *
        j
                    
        """
        pattern_matches = [False] * (len(p) + 1)
        pattern_matches[-1] = True

        memo = {}
        for k in range(len(p) -1, -1, -2):
            if p[k] != "*": break
            pattern_matches[k-1] = True

        def check(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            # Base Case
            if i < len(s) and j >= len(p):
                return False
            if i == len(s):
                return pattern_matches[j]
            
            next_char = p[j + 1] if j + 1 < len(p) else ""
            if next_char == "*":
                if p[j] != s[i] and p[j] != ".":
                    memo[(i, j)] = check(i, j + 2)
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = check(i, j + 2) or check(i + 1, j)
                    return check(i, j + 2) or check(i + 1, j)
            
            elif p[j] == "." or s[i] == p[j]:
                memo[(i, j)] = check(i + 1, j + 1)
                return check(i + 1, j + 1)
            
            memo[(i, j)] = False
            return False
        
        return check(0, 0)

