class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))

        num1 = num1[::-1]
        num2 = num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                res[i1 + i2] += int(num1[i1]) * int(num2[i2])
                res[i1 + i2 + 1] += res[i1 + i2] // 10 # carry
                res[i1 + i2] %= 10

        res.reverse()
        begin = 0
        while begin < len(res) and res[begin] == 0:
            begin += 1
        print(res, begin)
        return "".join(str(ch) for ch in res[begin:]) 