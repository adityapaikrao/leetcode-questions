class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        2 7 3 6
        i
        max_right = []
        at every elem swap with the max num on its right

        """
        digits = list(str(num))

        max_right = []
        curr_max = len(digits) - 1
        for i in range(len(digits) - 1, -1, -1):
            if int(digits[i]) > int(digits[curr_max]):
                max_right.append(i)
                curr_max = i
            else:
                max_right.append(curr_max)
        
        max_right.reverse()
        
        max_num = num
        for i in range(len(digits)):
            right = int(digits[max_right[i]])
            if right > int(digits[i]):
                digits[i], digits[max_right[i]] = digits[max_right[i]], digits[i]
                new_num = int("".join(digits))
                max_num = max(max_num, new_num)
                digits[i], digits[max_right[i]] = digits[max_right[i]], digits[i]
        
        return max_num

