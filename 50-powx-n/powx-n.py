class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base Cases
        if n == 0:
            return 1
        if x == -1:
            return (-1) ** (n % 2)
        if n == 1 or x == 1:
            return x
        
        if n < 0:
            x = (1/x)
            n = -n
        
        if n % 2 == 0:
            return self.myPow(x, n // 2) ** 2
        else:
            return x * ((self.myPow(x, n // 2)) ** 2)
    