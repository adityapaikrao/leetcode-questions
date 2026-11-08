class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        """
        1 0
        1 1
        """
        n = len(grid)
        m = len(grid[0])

        row_counts = [0] * n
        col_counts = [0] * m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
        
        num_connected = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    num_connected += 1
        
        return num_connected