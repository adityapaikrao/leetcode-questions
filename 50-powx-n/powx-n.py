class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base Cases
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x
        
        if n < 0:
            x = 1 / x
            n  = -n
        exp = self.myPow(x, n // 2)
        if n % 2 == 1:
            return x * exp * exp
        else:
            return exp * exp
    

        
        