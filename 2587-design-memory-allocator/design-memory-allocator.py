"""
[1,2,3,_,_,_,_,_,_,_]
     i

mID -> { id:  (start, end)}
(1, 1) -> {1: (i: i + 1) = (0, 1)}
(1, 2) -> {1: (0, 1) 2: (1, 2) , 3:(2, 3)}

"""

class Allocator:

    def __init__(self, n: int):
        self.map = defaultdict(list)
        self.mem = [0] * n
    
    def _find_index(self, size: int) -> int:
        """
        0 0 1 2 3 3 0 0 0 4 
                    i

        size = 3
        """
        i = 0
        curr_len = 0
        while i < len(self.mem):
            while i < len(self.mem) and self.mem[i] == 0:
                i += 1
                curr_len += 1
                if curr_len == size:
                    return i - size
            while i < len(self.mem) and self.mem[i] != 0:
                i += 1
            curr_len = 0
        return -1
            

    def allocate(self, size: int, mID: int) -> int:
        start = self._find_index(size)
        if start != -1:
            for i in range(start, start + size):
                self.mem[i] = mID
        return start
        
    def freeMemory(self, mID: int) -> int:
        counts = 0
        for i, val in enumerate(self.mem):
            if val == mID:
                self.mem[i] = 0
                counts += 1
        return counts


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)