"""
[1, 2, 5, 4, 3]

[3]

map = {1: 0, 2: 1, 5:2, 4:3, 3:4}

- get lookup index in arr in the map
- insert add to elem update entry in map
- remove swap elem to the end; pop from array & del key in map

"""
import random

class RandomizedSet:

    def __init__(self):
        self.elems = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.elems.append(val)
        self.map[val] = len(self.elems) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val]
        # swap to end & pop & delete key in map O(1)
        self.elems[index], self.elems[-1] = self.elems[-1], self.elems[index]
        self.elems.pop()
        del self.map[val]

        # update index for the swapped elem O(1)
        if index < len(self.elems):
            swapped = self.elems[index]
            self.map[swapped] = index
        return True


    def getRandom(self) -> int:
        index = random.randint(0, len(self.elems) - 1)
        return self.elems[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()