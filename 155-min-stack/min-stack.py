"""
2 3 1 pop min
min = 

[1, 2, 3]
[1, 1,]

"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.aux:
            self.aux.append(min(val, self.aux[-1]))
        else:
            self.aux.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.aux.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.aux[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()