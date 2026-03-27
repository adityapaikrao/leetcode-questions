from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        k = 3 -> 2th permutation
        0: 123
        1: 132
        2: 213
        3: 231
        4: 312
        5: 321


        
        """
        digits = [i + 1 for i in range(n)]
        k -= 1
        num = []
        for _ in range(n):
            idx = k // factorial(n-1)
            k %= factorial(n-1)

            num.append(str(digits[idx]))

            digits.pop(idx)
            n -= 1
        
        return "".join(num)


