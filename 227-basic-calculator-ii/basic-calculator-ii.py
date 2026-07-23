class Solution:
    def calculate(self, s: str) -> int:
        """
        3 + 2 * 2 = 7
        
        result = 5
        op = +
        prev = 2

        if op == + or -:
            result += currnum or -currnum
        else:
            result -= prev # restore prev num
            result += prev * currnum
        """
        prev = 0
        op = "+"
        result = 0

        i = 0
        while i < len(s):
            # skip space
            while i < len(s) and s[i] == " ":
                i += 1
            if i == len(s): 
                break

            # read num
            curr_num = 0
            while i < len(s) and s[i].isnumeric():
                curr_num = curr_num * 10 + int(s[i])
                i += 1
            
            # perform op
            if op in ['+', '-']:
                result += curr_num if op == '+' else -curr_num
                prev = curr_num if op == '+' else -curr_num
            elif op == '/':
                result -= prev
                result += int(prev / curr_num)
                prev = int(prev / curr_num)
            else:
                result -= prev
                result += prev * curr_num
                prev = prev * curr_num
            
            # skip spaces
            while i < len(s) and s[i] == " ":
                i += 1  
            
            # read next op
            if i < len(s):
                op = s[i]
                i += 1
        
        return result