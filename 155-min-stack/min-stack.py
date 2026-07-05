"""
[2, 4, 2, 1]

min = 1

when min elem is popped -- need to recover prev min
need some flag to tell when new_min popped

on new min push
    new_min < prev_min
    2*new_min < prev_min + new_min
    new_min > 2*new_min - prev_min

    flag = 2 * new_miin - prev_min

when flag popped ie. a value less than curr_min
    => new_min popped
    recover prev_min = 2 * new_min - flag

"""


class MinStack:

    def __init__(self):
        self.stack: List[int] = []
        self.min_val: int = None
        
    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            self.min_val = value
            return
        
        if value >= self.min_val:
            self.stack.append(value)
        else:
            flag = 2 * value - self.min_val
            self.stack.append(flag)
            self.min_val = value
        

    def pop(self) -> None:
        if not self.stack:
            return 
        
        popped = self.stack.pop()
        if popped < self.min_val:
            # min val popped, recover prev min
            self.min_val = 2 * self.min_val - popped
        return

    def top(self) -> int:
        return self.stack[-1] if self.stack[-1] > self.min_val else self.min_val

    def getMin(self) -> int:
        return self.min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()