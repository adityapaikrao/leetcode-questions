class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        n = len(s)
        word_set = set(wordDict)
        memo = {}

        def find_string(index: int) -> List[str]:
            if index in memo:
                return memo[index]
            
            if index == n:
                return [""]
            
            result = []
            for i in range(index, n):
                if s[index: i + 1] in word_set:
                    suffixes = find_string(i + 1)
                    for suffix in suffixes:
                        if suffix == "": 
                            result.append(s[index: i + 1])
                        else:
                            result.append(s[index: i + 1] + f" {suffix}")
            memo[index] = result
            return result
        
        return find_string(0)