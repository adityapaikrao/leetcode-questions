class Solution:
    def numDecodings(self, s: str) -> int:
        """
        6 0 6
        

        """
        # memo = {}
        # def count_ways(index: int) -> int:
        #     if index in memo:
        #         return memo[index]
            
        #     # Base Case
        #     if index == len(s):
        #         # reached end of string 1 way to decode
        #         return 1 
        #     if int(s[index]) == 0:
        #         # no way to decode 
        #         return 0

        #     num_ways = 0
        #     # 1 digit way 
        #     num_ways += count_ways(index + 1)
        #     if index + 1 < len(s) and (int(s[index]) * 10 + int(s[index + 1])) <= 26:
        #         num_ways += count_ways(index + 2)
        #     memo[index] = num_ways
        #     return num_ways
        
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) == 0:
                dp[i] = 0
                continue
            dp[i] += dp[i + 1]
            if i + 1 < len(s) and (int(s[i]) * 10 + int(s[i + 1])) <= 26:
                dp[i] += dp[i + 2]
        
        return dp[0]


            