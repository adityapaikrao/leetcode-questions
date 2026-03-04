from collections import Counter, defaultdict

class DetectSquares:

    def __init__(self):
        self.xmap = defaultdict(Counter) # y-coord - > count
        self.ymap = defaultdict(Counter) # x-coord - > count
        
    def add(self, point: List[int]) -> None:
        self.xmap[point[0]][point[1]] += 1
        self.ymap[point[1]][point[0]] += 1

    def count(self, point: List[int]) -> int:
        # choose point on same y-coord
        xcoord, ycoord = point
        num_squares = 0
        for pointx, count1 in self.ymap[ycoord].items():
            if pointx == xcoord:
                continue
            side_len = abs(xcoord - pointx)
            for target_y in [point[1] + side_len, point[1] - side_len]:
                cnt1 = self.xmap[pointx][target_y]
                cnt2 = self.xmap[xcoord][target_y]

                num_squares += cnt1 * cnt2 * count1
        
        return num_squares


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)