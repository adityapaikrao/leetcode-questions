class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        2 7 3 6
        i
        max_right = []
        at every elem swap with the max num on its right

        """
        digits = list(str(num))
        max_num = num
        curr_max = len(digits) - 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > digits[curr_max]:
                curr_max = i
                continue
            
            digits[curr_max], digits[i] = digits[i], digits[curr_max]
            new_num = int("".join(digits))
            max_num = max(max_num, new_num)
            digits[curr_max], digits[i] = digits[i], digits[curr_max]
    
        return max_num

