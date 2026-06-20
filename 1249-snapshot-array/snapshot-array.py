class SnapshotArray:
    """
    index -> snap_id & val

    set:
    - arr[index] = val

    snap:
    - insert (snap_id, index[val]) into index_map

    0 -> [0, 3], [0, 5], [2, 6], [3, 7]
    get:
    - find the largest index where snap_id <= query_snap_id
    - return val

    """

    def __init__(self, length: int):
        self.snap_id = 0
        self.index_map = [[] for _ in range(length)] # stores (snap_id, values) for each index

    def set(self, index: int, val: int) -> None:
        if self.index_map[index] and self.index_map[index][-1][0] == self.snap_id:
            self.index_map[index][-1][1] = val
        else:
            self.index_map[index].append([self.snap_id, val]) 

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        index_list = self.index_map[index]
        l = 0
        r = len(index_list) - 1
        val = 0

        while l <= r:
            mid = (l + r) // 2
            if index_list[mid][0] <= snap_id:
                val = index_list[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return val


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)