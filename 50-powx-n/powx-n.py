class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base Cases
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x
        
        isIntMin = False
        if n < 0:
            x = 1 / x
            if n == -(1 << 31):
                isIntMin = True
                n += 1
            n  = -n
        exp = self.myPow(x, n // 2)
        mult = 1 / x if isIntMin else 1
        if n % 2 == 1:
            return x * exp * exp * mult
        else:
            return exp * exp * mult
    

        
        