class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(row: int, col: int) -> None:
            grid[row][col] = "0" # mark as visited
            
            for row_off, col_off in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                new_row = row + row_off
                new_col = col + col_off
                if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == "1":
                    grid[row][col] = "0" # mark as visited
                    dfs(new_row, new_col)
        
        num_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    grid[i][j] = "0" # mark as visited
                    dfs(i, j)
                    num_islands += 1
        return num_islands