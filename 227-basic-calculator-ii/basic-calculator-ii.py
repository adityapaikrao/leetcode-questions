class Solution:
    def calculate(self, s: str) -> int:
        """
        exp = 0
        prev = 0
        op = +

        3 + 5 / 2
            i

        num = 3
        """
        i = 0 
        prev = 0
        op = "+"
        exp = 0

        while i < len(s):
            # skip spaces
            while i < len(s) and s[i] == " ":
                i += 1
            
            if i == len(s): break
            # read num
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            
            # do operation
            if op == "+":
                exp += num
                prev = num
            elif op == "-":
                exp -= num
                prev = -num
            elif op == "*":
                exp -= prev
                exp += prev * num
                prev = prev * num
            else:
                exp -= prev
                exp += int(prev / num)
                prev = int(prev / num)

            # skip spaces
            while i < len(s) and s[i] == " ":
                i += 1
            
            # read next operation
            op = s[i] if i < len(s) else ""
            i += 1
        
        return exp
            
