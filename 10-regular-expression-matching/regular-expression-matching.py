class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        * -> 0 or more of preceeding
        . -> any char

        aa
        i
        a*
        j

        aa
        aa*c*d*
        if next == *:
            if curr not match: 
                (i, j + 2)
            else:
                (i, j + 2) or (i + 1, j) or (i + 1, j + 2)
        if curr == .:
            (i + 1, j + 1)
        else:
            if curr not match: False
            else: (i + 1, j + 1)

        """
        memo = {}

        def can_prune(pattern: str, j: int) -> bool:
            for k in range(m - 1, j - 1, -2):
                if pattern[k] != "*": return False
            return True

        n, m = len(s), len(p)
        def solve(i: int, j: int) -> bool:
            # Base Case
            if i == n:
                print(i, j)
                return (j == m) or can_prune(p, j)
            if j == m:
                return False
            
            if (i, j) in memo: return memo[(i, j)] 

            # Recurrent Cases
            next_char = p[j+1] if j + 1 < m else ""
            if next_char == "*":
                if s[i] != p[j] and p[j] != ".":
                    memo[(i, j)] = solve(i, j + 2)
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = solve(i, j + 2) or solve(i + 1, j)
                    return memo[(i, j)]
            if p[j] == ".":
                memo[(i, j)] = solve(i + 1, j + 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] =  s[i] == p[j] and solve(i + 1, j + 1)
                return memo[(i, j)]
        
        return solve(0, 0)

        