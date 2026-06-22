class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        seen = set()
        max_len = 0

        for j in range(len(s)):
            if s[j] not in seen:
                seen.add(s[j])
                continue
            
            max_len = max((j - i), max_len)
            while i < j and s[j] in seen:
                seen.discard(s[i])
                i += 1
            seen.add(s[j])
        
        return max(max_len, len(s) - i)
