"""
key -> List[(timestamps, val)]
key -> 1, 3, 4, 6, 
    query 8 -> val(6)
    11, 12 
    query 8 -> ""

maintain map of key -> [timestamp, value] pairs
on query: do BS on List


questions? 
- timestamps icraeasing order?
- input validation? timestamp > 0 
- duplicate timestamp? no
"""
from typing import Dict, List, Tuple
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map: Dict[int, List[Tuple[int, int]]] = defaultdict(list) # key - > List[(timestamp, val)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        key_list = self.map[key]
        if not key_list: 
            return ""

        l = 0
        r = len(key_list) - 1
        max_val = ""
        while l <= r:
            mid = (l + r) // 2
            if key_list[mid][0] <= timestamp:
                max_val = key_list[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return max_val


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)