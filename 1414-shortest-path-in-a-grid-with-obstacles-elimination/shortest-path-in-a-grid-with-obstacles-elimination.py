class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        elims = [[-float('inf')] * m for _ in range(n)]

        q = deque([(0, k, 0, 0)]) # steps, removals_remaining, row, col

        while q:
            curr_steps, removals, curr_row, curr_col = q.popleft()
            if curr_row == n - 1 and curr_col == m - 1: return curr_steps
            if elims[curr_row][curr_col] > removals: continue

            elims[curr_row][curr_col] = removals
            for row_offset, col_offset in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                new_row = curr_row + row_offset
                new_col = curr_col + col_offset

                if 0 <= new_row < n and 0 <= new_col < m:
                    new_steps = curr_steps + 1
                    new_removals = removals if grid[new_row][new_col] == 0 else removals - 1

                    if new_removals >= 0 and new_removals > elims[new_row][new_col]:
                        elims[new_row][new_col] = new_removals
                        q.append((new_steps, new_removals, new_row, new_col))
        print(elims)
        return -1
              
            


