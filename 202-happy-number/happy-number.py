class Solution:
    def isHappy(self, num: int) -> bool:
        seen = set([num])
        while True:
            curr_sum = 0
            while num > 0:
                curr_sum += (num % 10) ** 2
                num = num // 10
            
            if curr_sum == 1:
                return True
            elif curr_sum in seen:
                return False
            
            seen.add(curr_sum)
            num = curr_sum
            