class Allocator:

    def __init__(self, n: int):
        self.arr = [0] * n # zero -> no allocated
    
    def _find_start_block(self, size: int) -> int:
        curr_size = 0
        for i in range(len(self.arr)):
            if self.arr[i] == 0:
                curr_size += 1
                if curr_size == size:
                    return i - size + 1
            else:
                curr_size = 0
        return -1

    def allocate(self, size: int, mID: int) -> int:
        start_idx = self._find_start_block(size)
        if start_idx == -1:
            return start_idx
        for i in range(start_idx, start_idx + size):
            self.arr[i] = mID
        return start_idx

    def freeMemory(self, mID: int) -> int:
        count = 0
        for i in range(len(self.arr)):
            if self.arr[i] == mID:
                count += 1
                self.arr[i] = 0
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)