class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        """
        0: land 
        1: water
        intially all 0

        """
        
        def can_cross(mid: int) -> bool:
            grid = [[0] * col for _ in range(row)]
            for i in range(mid + 1):
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1
            
            q = deque() # store (i, j) for valid starts
            for j in range(col):
                if grid[0][j] == 0: 
                    q.append((0, j))
                    grid[0][j] = -1 # mark as visited
            
            if not q: 
                return False # no valid starting cell

            while q:
                curr_i, curr_j = q.popleft()
                if curr_i == row - 1: 
                    return True # reached bottom
                
                for offset in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    new_i = curr_i + offset[0]
                    new_j = curr_j + offset[1]
                    if 0 <= new_i < row and 0 <= new_j < col and grid[new_i][new_j] == 0:
                        q.append((new_i, new_j))
                        grid[new_i][new_j] = -1 # mark as visited

            return False

        low = 0
        high = len(cells) - 1
        max_day = 0

        while low <= high:
            mid = (low + high) // 2
            if can_cross(mid):
                # print(f"can reach for {mid}")
                low = mid + 1
                max_day = mid + 1
            else:
                # print(f"can NOT reach for {mid}")
                high = mid - 1
        
        return max_day
        