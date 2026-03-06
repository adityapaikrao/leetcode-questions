class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        do a BFS from initial point [(i,j), min_time] # coords, min_time to unlock
        """
        n, m = len(grid), len(grid[0])
        q = [(grid[0][0], (0, 0))]
        times = [[float('inf')] * m for _ in range(n)]
        times[0][0] = grid[0][0]

        while q:
            curr_time, curr_node = heapq.heappop(q)
            if grid[curr_node[0]][curr_node[1]] == -1: continue

            if curr_node[0] == n-1 and curr_node[1] == m-1:
                return curr_time

            grid[curr_node[0]][curr_node[1]] = -1 # mark as visited
            for x_offset, y_offset in [[-1,0], [1, 0], [0, -1], [0, 1]]:
                new_x = curr_node[0] + x_offset
                new_y = curr_node[1] + y_offset

                if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] != -1:
                    new_time = max(grid[new_x][new_y], curr_time)
                    if new_time < times[new_x][new_y]:
                        times[new_x][new_y] = new_time
                        heapq.heappush(q,(new_time, (new_x, new_y)))
        
        return 0
