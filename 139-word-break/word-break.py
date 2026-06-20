class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}
        def can_break(i: int) -> bool:
            if i in memo:
                return memo[i]
            
            if i >= len(s): 
                return True
            
            for j in range(i, len(s)):
                new_word = s[i:j+1]
                if new_word in word_set:
                    if can_break(j + 1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False       

        return can_break(0)