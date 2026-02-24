from collections import defaultdict, Counter

class DetectSquares:

    def __init__(self):
        self.x_map = defaultdict(Counter)  # x -> Counter of y values
        self.y_map = defaultdict(Counter)  # y -> Counter of x values
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_map[x][y] += 1
        self.y_map[y][x] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        total = 0

        # Iterate over all points sharing the same y-coordinate
        for x2, cnt2 in self.y_map[py].items():
            if x2 == px:
                continue  # skip degenerate case (same point)
            
            side_len = abs(x2 - px)

            # Try square above and below
            for dy in [side_len, -side_len]:
                target_y = py + dy
                # Need points at (px, target_y) and (x2, target_y)
                c1 = self.x_map[px][target_y]
                c2 = self.x_map[x2][target_y]
                total += cnt2 * c1 * c2

        return total