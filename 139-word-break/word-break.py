class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        # def can_break(idx: int) -> bool:
            
        #     if idx == n:
        #         return True
            
        #     for i in range(idx, n):
        #         curr = s[idx: i + 1]
        #         if curr in word_set:
        #             if can_break(i + 1): return True
            
        #     return False
        
        # return can_break(0)

        dp = [False] * (n + 1)
        dp[-1] = True

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                curr = s[i: j + 1]
                if curr in word_set:
                    dp[i] |= dp[j + 1]
        
        return dp[0]