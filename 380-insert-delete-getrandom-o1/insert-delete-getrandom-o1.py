from typing import List, Dict

class RandomizedSet:
    def __init__(self):
        self.vals: List[int] = []
        self.map: Dict[int, int] = {} # val -> index in vals 

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.vals.append(val)
        self.map[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        popped_idx = self.map[val]
        # swap to end of array & pop
        self.vals[popped_idx], self.vals[-1] = self.vals[-1], self.vals[popped_idx]
        self.vals.pop()

        # update position of swapped elem
        del self.map[val]
        if popped_idx < len(self.vals):
            self.map[self.vals[popped_idx]] = popped_idx
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()