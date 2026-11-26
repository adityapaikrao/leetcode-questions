class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key = lambda word: (len(word), word))
        n = len(words)
        dp = [1] * n

        def is_predecessor(prev: str, curr: str) -> bool:
            """
            b d a 
              i 
            b a
              j
            """
            if len(curr) - len(prev) != 1: return False
            i = j = 0

            while j < len(prev) and i < len(curr):
                if prev[j] != curr[i]:
                    return prev[j:] == curr[i + 1:]
                i += 1
                j += 1
            return i == len(curr) - 1

        for i in range(1, n):
            for j in range(i):
                if is_predecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)