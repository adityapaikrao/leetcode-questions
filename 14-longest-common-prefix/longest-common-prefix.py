class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0
        while True:
            if i == len(strs[0]): 
                return strs[0]
            
            curr_char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != curr_char:
                    return strs[j][:i]
            
            i += 1
        
        return strs[0]
                

        