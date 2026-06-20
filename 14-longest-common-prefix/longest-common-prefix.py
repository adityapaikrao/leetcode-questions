class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        i = 0
        
        while i < len(strs[0]):
            curr_char = strs[0][i]

            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != curr_char:
                    return "".join(prefix)
            prefix.append(curr_char)
            i += 1
        
        return "".join(prefix)
            
                