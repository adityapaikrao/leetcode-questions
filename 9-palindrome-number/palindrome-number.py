class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        rev = 0
        x_orig = x

        while x:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        return x_orig == rev