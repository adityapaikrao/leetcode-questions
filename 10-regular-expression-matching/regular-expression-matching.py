class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Base Case:
        if p empty & s not empty -> no match
        if p empty & s empty -> match
        if s empty & p not empty -> check remaining chars in p can be removed s: "ab" p: "abb*c*d*"

        Recurrence:
        if next char is *
            -> delete curr char (i, j + 2)
            -> extend curr char (i + 1, j) if matches s[i] or p[j] is "."

            
        """
        def can_prune_pattern(pattern: str, idx: int) -> bool:
            for i in range(len(p) - 1, idx - 1, -2):
                if pattern[i] != "*":
                    return False

            return True

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True

        for j in range(len(p)):
            dp[len(s)][j] = can_prune_pattern(p, j)

        # print(dp[len(s)])

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(p) - 1, -1, -1):
                next_char = p[j + 1] if j + 1 < len(p) else ""
                if next_char == "*":
                    dp[i][j] = dp[i][j + 2] | ((s[i] == p[j] or p[j] == ".") and dp[i + 1][j])
                else:
                    if p[j] == ".":
                        dp[i][j] = dp[i + 1][j + 1]
                    else:
                        dp[i][j] = (s[i] == p[j]) and dp[i + 1][j + 1]
        
        return dp[0][0]


        # def solve(i: int, j: int) -> bool:
        #     # Base Cases
        #     if j == len(p):
        #         return i == len(s)
        #     if i == len(s):
        #         return can_prune_pattern(p, j)
            
        #     # Recurrence
        #     next_char = p[j + 1] if j  + 1 < len(p) else ""
        #     if next_char == "*":
        #         # delete char
        #         if solve(i, j + 2):
        #             return True
                
        #         if (s[i] == p[j] or p[j] == ".") and solve(i + 1, j):
        #             return True
            
        #         return False
        
        #     if p[j] == ".":
        #         if solve(i + 1, j + 1):
        #             return True
        #     else:
        #         if s[i] == p[j] and solve(i + 1, j + 1):
        #             return True
            
        #     return False
        
        # return solve(0, 0)

