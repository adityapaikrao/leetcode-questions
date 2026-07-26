class Block:
    def __init__(self, start: int = -1, size: int = -1):
        self.start = start
        self.size = size
        self.next = None

class Allocator:

    def __init__(self, n: int):
        self.head = Block()
        self.head.next = Block(0, n)
        self.allocated = defaultdict(list) # mID -> List[(start, size)]

    def allocate(self, size: int, mID: int) -> int:
        prev = self.head
        curr = prev.next

        while curr:
            if curr.size >= size:
                allocation_start = curr.start
                curr.start += size
                curr.size -= size
                if curr.size == 0:
                    # remove this block from list
                    prev.next = curr.next
                self.allocated[mID].append((allocation_start, size))
                return allocation_start
            prev = curr
            curr = curr.next
        return -1

    def freeMemory(self, mID: int) -> int:
        freed = 0
        while self.allocated[mID]:
            start, size = self.allocated[mID].pop()
            freed += size
            self._free_block(start, size)
        
        return freed
    
    def _free_block(self, start: int, size: int):
        """
        [4, 2]
        (0, 4) (4, 2) [6, 7] (7, 10)
                                c
          p
        """
        prev = self.head
        curr = prev.next
        while curr and curr.start < start:
            prev = curr
            curr = curr.next

        # insert free block        
        new_block = Block(start, size) 
        prev.next = new_block
        new_block.next = curr

        merged_block = new_block
        # merge if possible
        if prev.start + prev.size == new_block.start:
            prev.size += new_block.size
            prev.next = new_block.next
            merged_block = prev
        
        if curr and merged_block.start + merged_block.size == curr.start:
            merged_block.size += curr.size
            merged_block.next = curr.next


        




# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)