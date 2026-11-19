class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        n = len(s)
        word_set = set(wordDict)
        strings = []
        curr_words = []

        def find_string(index: int) -> None:
            if index == n:
                strings.append(" ".join(curr_words))
                return
            
            for i in range(index, n):
                if s[index: i + 1] in word_set:
                    curr_words.append(s[index: i + 1])
                    find_string(i + 1)
                    curr_words.pop()
            return 
        
        find_string(0)
        return strings