class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        times = [[float('inf')] * m for _ in range(n)]
        # times[0][0] = 0

        heap = [(grid[0][0], 0, 0)] # time, row_idx, col_idx
        while heap:
            curr_time, curr_row, curr_col = heapq.heappop(heap)
            if times[curr_row][curr_col] <= curr_time: continue

            if curr_row == n - 1 and curr_col == m - 1: return curr_time
            
            times[curr_row][curr_col] = curr_time
            for row_offset, col_offset in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                new_row = curr_row + row_offset
                new_col = curr_col + col_offset
                if 0 <= new_row < n and 0 <= new_col < m:
                    new_time = max(grid[new_row][new_col], curr_time)
                    if new_time < times[new_row][new_col]:
                        heapq.heappush(heap, (new_time, new_row, new_col))
        
            