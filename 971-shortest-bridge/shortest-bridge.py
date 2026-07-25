class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        [1,1,1,1,1]
        [1,0,0,0,1]
        [1,0,1,0,1]
        [1,0,0,0,1]
        [1,1,1,1,1]

        1. First BFS start from 1 and mark all as 2
        2. Second BFS start from 1 until you reach a 1 
        """
        n = len(grid)
        marked = False
        for i in range(n):
            if marked:
                break
            for j in range(n):
                # print(i, j)
                if grid[i][j] == 1:
                    marked = True
                    # start first DFS
                    # print((i, j))
                    q = [(i, j)]
                    grid[i][j] = 2
                    
                    while q:
                        curr_i, curr_j = q.pop()

                        for i_off, j_off in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                            new_i = curr_i + i_off
                            new_j = curr_j + j_off
                            if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == 1:
                                q.append((new_i, new_j))
                                grid[new_i][new_j] = 2
                    break
        
        # print(grid)
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    # start 2nd BFS
                    q.append((i, j))
                    grid[i][j] = -1
        
        flips = 0
        while q:
            for _ in range(len(q)):
                curr_i, curr_j = q.popleft()
                for i_off, j_off in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    new_i = curr_i + i_off
                    new_j = curr_j + j_off
                
                    if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] != -1:
                        if grid[new_i][new_j] == 2:
                            return flips
                        q.append((new_i, new_j))
                        grid[new_i][new_j] = -1
            flips += 1 

