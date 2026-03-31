class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        num = 0
        res = 0
        stack = []

        for i in range(len(s)):
            if s[i] == " ": continue
            elif s[i] == "(":
                stack.extend([res, sign])
                sign = 1
                num = 0
                res = 0
            elif s[i] == ")":
                res += sign * num
                num = 0
                sign = 1

                sign = stack.pop()
                prev = stack.pop()
                # print(res, sign, prev)
                res = res * sign + prev
            elif s[i] == "+":
                res += sign * num
                sign = 1
                num = 0
            elif s[i] == "-":
                res += sign * num
                sign = -1
                num = 0
            else:
                num = num * 10 + int(s[i])
        
        return res + sign * num
