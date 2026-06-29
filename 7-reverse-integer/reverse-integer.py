class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 
        if x < 0:
            x = -x
            sign = -1

        rev = 0
        MAX_INT = (1 << 31) - 1

        while x:
            digit = int(x % 10)
            
            if rev > MAX_INT // 10 or (rev == MAX_INT // 10 and digit == 7):
                return 0
            
            rev = rev * 10 + digit
            x //= 10
        
        rev *= sign
        return rev if -(1 << 31) <= rev <= MAX_INT else 0
