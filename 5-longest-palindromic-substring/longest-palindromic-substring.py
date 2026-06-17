from typing import Tuple

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longest_odd_palindrome(start_index: int) -> Tuple[int, int]:
            i, j = start_index - 1, start_index + 1
            if i < 0 or j > len(s):
                return start_index, start_index
            
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            
            return i + 1, j - 1
        
        def longest_even_palindrome(start_index: int) -> Tuple[int, int]:
            i, j = start_index - 1, start_index
            if i < 0:
                return -1, -1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            
            return i + 1, j - 1
        
        longest_start = 0
        longest_end = 0

        for i in range(len(s)):
            odd_start, odd_end = longest_odd_palindrome(i)
            if odd_end - odd_start > longest_end - longest_start:
                longest_start, longest_end = odd_start, odd_end
        
            even_start, even_end = longest_even_palindrome(i)
            if even_end - even_start > longest_end - longest_start:
                longest_start, longest_end = even_start, even_end
        
        return s[longest_start: longest_end + 1]