class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append((v, cost))
        
        dist = [float('inf')] * n
        heap = [(0, 0, src)] # stops, disr, node

        while heap:
            curr_stops, curr_dist, curr_node = heapq.heappop(heap)
            if curr_dist >= dist[curr_node]: continue
            dist[curr_node] = curr_dist
            if curr_stops == k + 1: continue
            
            for nbr, wt in adj[curr_node]:
                new_dist = curr_dist + wt
                if new_dist < dist[nbr]:
                    heapq.heappush(heap, (curr_stops + 1, curr_dist + wt, nbr))

        return dist[dst] if dist[dst] != float('inf') else -1
