"""

9 4 3 2 1

5 5 
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        stack = []


        for pos, speed in cars:
            time = (target - pos) / speed

            if stack and time < stack[-1]:
                stack.append(time)
            else:
                while stack and stack[-1] <= time:
                    stack.pop()
                stack.append(time)
        
        return len(stack)
