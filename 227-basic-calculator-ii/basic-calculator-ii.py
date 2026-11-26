class Solution:
    def calculate(self, s: str) -> int:
        """
        32 + 2 * 2 = 7
                   i

        prev = 4
        op = *
        curr_num = 0
        curr_sum = 7



        - read num
            - if op == * or /:
                - recover prev from curr_sum -= prev
                - add prev 'op' num to curr_sum
                - prev = prev 'op' num
            - else:
                - curr_sum += prev op num
                - prev = num
                - curr_num = 0
        - read op


        curr_sum = 5
        num = 0
        curr_op = *

        """
        curr_sum = 0
        num = 0
        prev = 0
        op = '+'

        for char in s:
            if char == " ": continue
            if char in ["+", "-", "*", "/"]:
                # print(prev, op, num, curr_sum)
                if op == "+":
                    curr_sum += num
                    prev = num
                elif op == "-":
                    curr_sum -= num
                    prev = -num
                elif op == "*":
                    curr_sum -= prev
                    curr_sum += prev * num
                    prev = prev * num
                else:
                    curr_sum -= prev
                    curr_sum += int(prev / num)
                    prev = int(prev / num)
                op = char
                num = 0
            else:
                num = num * 10 + int(char)
        
        if op == "+":
            curr_sum += num
            prev = num
        elif op == "-":
            curr_sum -= num
            prev = -num
        elif op == "*":
            curr_sum -= prev
            curr_sum += prev * num
            prev = prev * num
        else:
            curr_sum -= prev
            curr_sum += int(prev / num)
            prev = int(prev / num)
        
        return curr_sum

        