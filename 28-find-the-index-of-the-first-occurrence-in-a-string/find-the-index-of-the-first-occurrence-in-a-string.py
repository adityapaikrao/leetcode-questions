class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        i = 1
        length = 0

        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length > 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        i = 0
        j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
                if j == len(needle):
                    return i - j # first start at i - j
                # occurences.append(i-j)
                # j = lps[j-1]
            else:
                if j > 0:
                    j = lps[j-1]
                else:
                    i += 1
        return -1
