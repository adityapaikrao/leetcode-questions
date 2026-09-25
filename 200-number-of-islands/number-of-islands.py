class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        num_islands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1": # not yet visited
                    num_islands += 1

                    q = deque([(i, j)])
                    grid[i][j] = "0"
                    while q:
                        curr_i, curr_j = q.popleft()
                        for offset_i, offset_j in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                            new_i, new_j = offset_i + curr_i, offset_j + curr_j
                            if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == "1":
                                grid[new_i][new_j] = "0" # mark as visited
                                q.append((new_i, new_j))
            
        return num_islands
