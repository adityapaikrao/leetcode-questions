class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        if len(word1) == 0 or len(word2) == 0:
            return max(len(word2), len(word1))
        
        # memo = {}
        # def num_ops(i: int, j: int) -> int:
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     # Base Case:
        #     if i == len(word1):
        #         return len(word2[j:])
        #     if j == len(word2):
        #         return len(word1[i:])
            
        #     # Options
        #     if word1[i] == word2[j]:
        #         memo[(i, j)] = num_ops(i + 1, j + 1)
        #         return memo[(i, j)] 
        #     else:
        #         memo[(i, j)] = min(
        #             num_ops(i + 1, j), # delete i or insert in j
        #             num_ops(i, j + 1), # delete j or insert in i
        #             num_ops(i + 1, j + 1) # replace i or j
        #         ) + 1
        #         return memo[(i, j)] 
        
        # return num_ops(0, 0)

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1[i:])

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2[j:])

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        dp[i + 1][j + 1],
                        dp[i + 1][j],
                        dp[i][j + 1],
                    ) + 1
        
        return dp[0][0]
        