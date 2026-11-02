class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        a b c a b c b b
                    -1` 54s
                      e

        set = {} # set of chars

        While end in bounds:
        - keep track of start & end of window
        - expand window until no dups
        - on dups:
            - shrink window until dup removed

        a b c 
        s
              e
        """
        start = 0

        max_length = 0
        seen = set()
        for end in range(len(s)):
            if not s[end] in seen:
                seen.add(s[end])
            else:
                # seen a duplicate
                max_length = max(end - start, max_length)
                while s[start] != s[end]:
                    seen.remove(s[start])
                    start += 1
                start += 1
        
        # case when end goes out of bounds 
        max_length = max(max_length, len(s) - start)
        return max_length