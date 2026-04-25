class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        """
        Approach:
        - maxdepth = 1, memo = {}: stores (i, j) -> max length
        - for each node:
            do DFS
        dfs(node):
          if in memo: return value in memo
          
          maxdepth = 0
          for nbr:
            maxdepth = max(maxdepth, dfs(nbr))
          return 1 + maxdepth
        """
        n, m = len(grid), len(grid[0])
        memo = {} # store (row, col) -> depth

        def dfs(row: int, col: int) -> None:
            if (row, col) in memo:
                return memo[(row, col)]
            
            max_depth = 0
            for offset in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                new_row = row + offset[0]
                new_col = col + offset[1]

                if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] > grid[row][col]:
                    max_depth = max(max_depth, dfs(new_row, new_col))
            memo[(row, col)] = 1 + max_depth
            return memo[(row, col)]
        
        longest_path = 1
        for i in range(n):
            for j in range(m):
                longest_path = max(longest_path, dfs(i, j))
        
        return longest_path