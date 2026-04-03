class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        i, j = 0, len(self.intervals) - 1
        ans = -1
        while i <= j:
            mid = (i + j) // 2
            if self.intervals[mid][0] <= left:
                ans = mid
                i = mid + 1
            else:
                j = mid - 1

        # ans = last interval whose start <= left
        if ans >= 0 and self.intervals[ans][1] >= left:
            start = ans  # overlaps, extend it
        else:
            start = ans + 1  # no overlap, insert new
            self.intervals.insert(start, [left, right])

        self.intervals[start][0] = min(self.intervals[start][0], left)
        self.intervals[start][1] = max(self.intervals[start][1], right)

        # merge all following intervals that now overlap
        i = start + 1
        while i < len(self.intervals) and self.intervals[i][0] <= self.intervals[start][1]:
            self.intervals[start][1] = max(self.intervals[start][1], self.intervals[i][1])
            i += 1

        self.intervals[start + 1:i] = []

    def queryRange(self, left: int, right: int) -> bool:
        if not self.intervals:
            return False

        i, j = 0, len(self.intervals) - 1
        ans = -1
        while i <= j:
            mid = (i + j) // 2
            if self.intervals[mid][0] <= left:
                ans = mid
                i = mid + 1
            else:
                j = mid - 1

        # ans = last interval whose start <= left — must also cover right
        if ans == -1:
            return False
        return self.intervals[ans][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        if not self.intervals:
            return

        i, j = 0, len(self.intervals) - 1
        ans = -1
        while i <= j:
            mid = (i + j) // 2
            if self.intervals[mid][1] <= left:
                i = mid + 1
            else:
                ans = mid
                j = mid - 1

        if ans == -1:
            return  # all intervals end before left, nothing to remove

        i = ans
        new = self.intervals[:i]

        # save left piece of first affected interval
        if self.intervals[i][0] < left:
            new.append([self.intervals[i][0], left])

        # skip all intervals fully covered by [left, right)
        while i < len(self.intervals) and self.intervals[i][1] <= right:
            i += 1

        # save right piece of last affected interval
        if i < len(self.intervals) and self.intervals[i][0] < right:
            new.append([right, self.intervals[i][1]])
            i += 1

        new.extend(self.intervals[i:])
        self.intervals = new