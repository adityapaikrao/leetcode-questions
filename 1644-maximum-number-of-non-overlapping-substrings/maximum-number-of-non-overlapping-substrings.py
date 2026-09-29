class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        """
        adefaddacc

        - good strategy always choose single occurence chars 
        - then choose ones which do not overlap with this choice
        - fiind span of each char: char -> (start, end)

        heap = [
            (1, 2, 2, e) # len, start, end, char
            (1, 3, 3, f)
            (8, 0, 7, a)
            (6, 1, 6, d)
            (2, 8, 9, c)
        ]

        - reject the ones which overlap with chosen ones

        alternative approach
        - fiind span of each char: char -> (start, end)
        - if char span contains another chars span, always better to choose the inner one
        x x y y x x
        sx
            sy
        ie choose one that starts later and see if the earlier one has overlap: ex > sy
        """
        starts, ends = [-1] * 26, [-1] * 26
        for i in range(len(s)):
            if starts[ord(s[i]) - ord('a')] == -1:
                starts[ord(s[i]) - ord('a')] = i
            ends[ord(s[i]) - ord('a')] = i
        
        valid = [False] * len(s)
        
        for char_idx in range(26):
            if starts[char_idx] == -1: continue
            invalid = False
            j = starts[char_idx]
            while j <= ends[char_idx]:
                if starts[ord(s[j]) - ord('a')] < starts[char_idx]:
                    invalid = True
                    break
                ends[char_idx] = max(ends[char_idx], ends[ord(s[j]) - ord('a')])
                j += 1
            valid[starts[char_idx]] = not invalid
        
        last_start = len(s)
        strings = [] 
        for k in range(len(s) -1, -1, -1):
            if not valid[k]: continue

            curr_start, curr_end = starts[ord(s[k]) - ord('a')], ends[ord(s[k]) - ord('a')]
            if last_start > curr_end:
                last_start = curr_start
                strings.append(s[curr_start: curr_end + 1])
        
        return strings


