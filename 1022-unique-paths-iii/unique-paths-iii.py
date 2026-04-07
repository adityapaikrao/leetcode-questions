class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        num_empty = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start_row, start_col = i, j
                elif grid[i][j] == 0:
                    num_empty += 1

        def count_paths(row: int, col: int) -> None:
            nonlocal num_empty, num_paths
            # Base Case: reached dest
            if grid[row][col] == 2:
                if num_empty == -1:
                    num_paths += 1
                return
            
            temp = grid[row][col]
            grid[row][col] = -1 # mark as visited

            for offset in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                new_row = row + offset[0]
                new_col = col + offset[1]
                if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] in [0,2]:
                    num_empty -= 1
                    count_paths(new_row, new_col)
                    num_empty += 1
            
            grid[row][col] = temp

            
        num_paths = 0
        count_paths(start_row,start_col)

        return num_paths
        
