class SnapshotArray:

    def __init__(self, length: int):
        self._size = length
        self._indexes = [[] for _ in range(length)]
        self._snap_id = 0

    def set(self, index: int, val: int) -> None:
        self._indexes[index].append((self._snap_id, val))
        return

    def snap(self) -> int:
        self._snap_id += 1
        return self._snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        val = 0
        l, r = 0, len(self._indexes[index]) - 1

        while l <= r:
            mid = (l + r) // 2
            if self._indexes[index][mid][0] > snap_id:
                r = mid - 1
            else:
                val = self._indexes[index][mid][1]
                l = mid + 1
        
        return val

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)