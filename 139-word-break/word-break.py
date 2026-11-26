class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[-1] = True

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                curr = s[i: j + 1]
                if dp[j + 1] and curr in word_set:
                    dp[i] = True
                    break
        
        return dp[0]