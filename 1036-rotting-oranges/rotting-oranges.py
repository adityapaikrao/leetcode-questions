class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rotten = deque([])
        num_fresh = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    grid[i][j] = 0 # mark as empty
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    num_fresh += 1
        
        if num_fresh == 0: return 0
        if not rotten: -1

        time = 0
        while rotten and num_fresh > 0:
            for _ in range(len(rotten)):
                curr_i, curr_j = rotten.popleft()
                for offset_i, offset_j in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    new_i = curr_i + offset_i
                    new_j = curr_j + offset_j
                    if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 1:
                        num_fresh -= 1
                        grid[new_i][new_j] = 0 # mark as empty
                        rotten.append((new_i, new_j))
            
            time += 1 
        return -1 if num_fresh > 0 else time
