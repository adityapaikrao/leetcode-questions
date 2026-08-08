class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.nums = encoding
        self.i = 0

    def next(self, n: int) -> int:
        while n > 0 and self.i < len(self.nums):
            self.nums[self.i] -= n
            if self.nums[self.i] >= 0:
                return self.nums[self.i + 1]
            else:
                n = -1 * self.nums[self.i]
                self.i += 2
        return -1
        



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)