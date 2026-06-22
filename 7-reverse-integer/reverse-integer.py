class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        max_int = (1 << 31) - 1

        while x:
            digit = x % 10
            if rev > max_int // 10 or (rev == max_int // 10 and digit > 7):
                return 0
            rev = rev * 10 + digit
            x //= 10

        rev *= sign
        return rev if -(1 << 31) <= rev <= max_int else 0