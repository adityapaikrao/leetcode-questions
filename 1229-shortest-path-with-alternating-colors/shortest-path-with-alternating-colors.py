class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        adj = [[[] for _ in range(2)]  for _ in range(n)] # adj[u][0] -> [] RedEdges
                                                          # adj[u][1] -> [] BlueEdges
        for u, v in redEdges:
            adj[u][0].append(v)
        for u, v in blueEdges:
            adj[u][1].append(v)
        
        dp = [[float('inf')] * 2 for _ in range(n)]
        dp[0][0], dp[0][1] = 0, 0
        # dp[u][0] -> length of shortest alternating path ending in red
        # dp[u][1] -> length of shortest alternating path ending in blue

        q = deque([(0, 0), (0, 1)]) # node, color
        while q:
            curr_node, curr_color = q.popleft()

            for nbr in adj[curr_node][1 - curr_color]:
                if dp[nbr][1 - curr_color] > dp[curr_node][curr_color]: 
                    dp[nbr][1 - curr_color] = dp[curr_node][curr_color] + 1
                    q.append((nbr, 1 - curr_color))
        min_len = []
        for node in range(n):
            min_node = min(dp[node])
            min_len.append((min_node if min_node != float('inf') else -1))
        
        return min_len
                
        
                                                        