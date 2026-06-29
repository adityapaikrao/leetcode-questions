class Solution:
    def reverseWords(self, s: str) -> str:
        chars = []
        i = len(s) - 1

        while i >= 0:
            # skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1
            
            if i < 0: break

            # read word
            word = []
            j = i
            while j >= 0 and s[j] != " ":
                j -= 1
            chars.append(s[j + 1: i + 1])
            i = j
        
        return " ".join(chars)
        
