class Solution:
    def reverse(self, x: int) -> int:
        """
        12 
        1 1 0 0 

        21
        1 0 1 0 1
        """
        sign = 1
        if x < 0:
            x *= -1
            sign = -1
        
        num = 0
        while x > 0:
            num = num * 10 + (x % 10)
            x = x // 10
            # print(num, x)
        
        if sign == -1:
            return 0 if num > (1 << 31) else num * sign
        else:
            return 0 if num > (1 << 31) - 1 else num
        