class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append((v, cost))
        
        stops = [float('inf')] * n
        heap = [(0, 0, src)] # dist, stops, node

        while heap:
            curr_dist, curr_stops, curr_node = heapq.heappop(heap)
            if curr_node == dst: return curr_dist
            if curr_stops >= stops[curr_node]: continue
            if curr_stops == k + 1: continue

            stops[curr_node] = curr_stops
            for nbr, wt in adj[curr_node]:
                new_stops = curr_stops + 1
                if new_stops < stops[nbr]:
                    heapq.heappush(heap, (curr_dist + wt, new_stops, nbr))

        return -1 
