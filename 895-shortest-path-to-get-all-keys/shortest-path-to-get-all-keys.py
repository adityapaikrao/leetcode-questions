class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        n, m = len(grid), len(grid[0])
        all_keys = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    start = (i, j)
                elif grid[i][j].islower():
                    all_keys |= (1 << ord(grid[i][j]) - ord('a'))
        
        seen = {(0, *start)} # keys, row, col
        q = deque([(0, 0, *start)])

        while q:
            curr_steps, curr_keys, curr_row, curr_col = q.popleft()
            if curr_keys == all_keys: return curr_steps

            for row_offset, col_offset in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                new_row, new_col = curr_row + row_offset, curr_col + col_offset
                new_steps = curr_steps + 1

                if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] != "#":
                    cell = grid[new_row][new_col]
                    if cell.isupper() and not (curr_keys >> (ord(grid[new_row][new_col]) - ord('A')) & 1):
                        continue
                    new_keys = curr_keys if not cell.islower() else curr_keys  | (1 << (ord(grid[new_row][new_col]) - ord('a')))
                    if (new_keys, new_row, new_col) not in seen:
                        seen.add((new_keys, new_row, new_col))
                        q.append((new_steps, new_keys, new_row, new_col))

        return -1 

