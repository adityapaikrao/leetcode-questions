class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        prefix = []
        i = 0

        while i < len(strs[0]):
            if strs[0][i] != strs[-1][i]:
                break
            prefix.append(strs[0][i])
            i += 1

        return "".join(prefix)