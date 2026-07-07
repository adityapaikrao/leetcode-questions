class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        # memo = {}
        # def can_break(start: int) -> bool:
        #     if start in memo:
        #         return memo[start]

        #     if start >= len(s):
        #         return True
            
        #     for i in range(start, len(s)):
        #         if s[start: i + 1] in word_set:
        #             if can_break(i + 1):
        #                 memo[start] = True
        #                 return True
            
        #     memo[start] = False
        #     return False
        """
        l e e t c o d e 
        i
              j
        0 0 0 0 1 0 0 0 1
                       
        """

        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i: j + 1] in word_set:
                    dp[i] |= dp[j + 1]
                    # break
        return dp[0]