"""
73,74,75,71,69,72,76,73
             1   1   0  0
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = [n-1]

        for i in range(n - 2, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack: answer[i] = stack[-1] - i
            stack.append(i)
        
        return answer
