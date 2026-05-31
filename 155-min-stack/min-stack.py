"""
2 3 f 1
flag = new_min - prev_min (1 - 2 = -1)
min = 1

when popping elem, if elem is min :
    - min = popped - flag (1 - -1 = 2)

1 2 3 


min = 1

"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None:
            self.stack.append(val)
            self.min = val
        
        elif self.min > val:
            self.stack.append(2*val - self.min)
            self.min = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()

        if popped < self.min:
            self.min = 2 * self.min - popped
        elif not self.stack:
            self.min = None

    def top(self) -> int:
        if self.stack[-1] < self.min:
            return self.min
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()