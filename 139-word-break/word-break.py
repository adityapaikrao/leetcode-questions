class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        # memo = {}
        # def can_break(i: int) -> bool:
        #     if i in memo:
        #         return memo[i]
            
        #     if i >= len(s): 
        #         return True
            
        #     for j in range(i, len(s)):
        #         new_word = s[i:j+1]
        #         if new_word in word_set:
        #             if can_break(j + 1):
        #                 memo[i] = True
        #                 return True
        #     memo[i] = False
        #     return False       

        # return can_break(0)

        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if dp[j + 1] and s[i: j+1] in word_set:
                    dp[i] = True
                    break
        
        return dp[0]