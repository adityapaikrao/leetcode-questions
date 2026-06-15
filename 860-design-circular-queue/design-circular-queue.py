class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.q = [-1] * k
        self.front = 0
        self.rear = k - 1
        self.len = 0

    def enQueue(self, value: int) -> bool:
        if self.len == self.size:
            return False
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        self.len += 1
        return True 

    def deQueue(self) -> bool:
        if self.len == 0:
            return False
        self.front = (self.front + 1) % self.size
        self.len -= 1
        return True

    def Front(self) -> int:
        if self.len == 0:
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.len == 0:
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()