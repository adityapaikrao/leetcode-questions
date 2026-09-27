class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append((v, cost))
        
        dist = [float('inf')] * n
        q = deque([(0, 0, src)]) # dist, stops, node

        while q:
            curr_dist, curr_stops, curr_node = q.popleft()
            if curr_stops == k + 1: continue
            
            for nbr, wt in adj[curr_node]:
                new_dist = curr_dist + wt
                new_stops = curr_stops + 1
                if new_dist < dist[nbr]:
                    dist[nbr] = new_dist
                    q.append((new_dist, new_stops, nbr))

        return dist[dst] if dist[dst] != float('inf') else -1