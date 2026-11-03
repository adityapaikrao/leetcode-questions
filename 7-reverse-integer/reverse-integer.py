class Solution:
    """
    2 4 8 16 32

    """
    def reverse(self, x: int) -> int:
        MIN_INT = -(1 << 31)
        MAX_INT = (1 << 31) - 1

        if x == MIN_INT:
            return 0
        
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        
        rev = 0
        while x > 0:
            digit = x % 10
            if (rev > MAX_INT // 10) or (rev == MAX_INT // 10 and  digit > 7):
                return 0
            rev = rev * 10 + digit
            x = x // 10
        
        return rev * sign 
        