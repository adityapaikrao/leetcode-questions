class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def can_break(start: int) -> bool:
            if start in memo:
                return memo[start]

            if start >= len(s):
                return True
            
            for i in range(start, len(s)):
                if s[start: i + 1] in word_set:
                    if can_break(i + 1):
                        memo[start] = True
                        return True
            
            memo[start] = False
            return False
        
        return can_break(0)