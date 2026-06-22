
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        original = x

        while x != 0:
            digit = -x % 10 if x < 0 else x % 10
            rev = rev * 10 + int(digit)

            x = int(x / 10)
        if rev > (1 << 31) - 1 or rev < -(1<<31):
            return 0
        return rev if original > 0 else -rev
    