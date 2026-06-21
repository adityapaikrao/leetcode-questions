class MyCircularQueue:

    def __init__(self, k: int):
        self._arr = [0] * k
        self._front = 0
        self._len = 0
        self._size = k


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self._arr[(self._front + self._len) % self._size] = value
        self._len += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._front = (self._front + 1) % self._size
        self._len -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self._arr[self._front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self._arr[(self._front + self._len - 1) % self._size]
    def isEmpty(self) -> bool:
        return self._len == 0

    def isFull(self) -> bool:
        return self._len == len(self._arr)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()