class Solution:
    """
     3 + 2 * 2
             i

    exp = 3 
    prev = 2
    op = *

    - skip spaces
    - read number 
    - check op:
        + => add to exp; set prev num to num
        - => subtract from exp; set prev num to -num
        / => exp - prev num; exp + prevum / num; prevnum = num
        * => exp - prev num; exp + prevnum * num; prevnum = num
    - skip spaces
    - read operation
    """
    def calculate(self, s: str) -> int:
        prev = 0
        op = "+"
        exp = 0
        i = 0

        while i < len(s):
            # skip spaces
            while i < len(s) and s[i] == " ":
                i += 1

            # read number
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

            # read next op    
            if i < len(s):
                op = s[i]
                i += 1
        
        return exp
        
            
            

