class SnapshotArray:

    def __init__(self, length: int):
        self.index = {}
        self.snap_id = 0
    def set(self, index: int, val: int) -> None:
        if index not in self.index:
            self.index[index] = {}
        self.index[index][self.snap_id] = val
        return

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.index:
            return 0
        return self._most_recent(index, sorted(list(self.index[index].keys())), snap_id)
    
    def _most_recent(self, index: int, snap_ids: List[int], snap_id: int) -> int:
        most_recent = 0
        l = 0
        r = len(snap_ids) - 1
        while l <= r:
            mid = (l + r) // 2
            if snap_ids[mid] <= snap_id:
                most_recent = self.index[index][snap_ids[mid]]
                l = mid + 1
            else:
                r = mid - 1
        return most_recent
            


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)