class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append((v, cost))
        
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0 
        # stops[src] = 0

        heap = [(0, 0, src)] # (dist, stops, node)

        while heap:
            curr_dist, curr_stops, curr_node = heapq.heappop(heap)
            if dist[curr_node][curr_stops] < curr_dist: continue
            elif curr_stops == k + 1: continue

            # print(curr_node, dist, stops)
            for nbr, wt in adj[curr_node]:
                new_stops = curr_stops + 1
                new_dist = curr_dist + wt

                if dist[nbr][new_stops] > new_dist:
                    dist[nbr][new_stops] = new_dist
                    heapq.heappush(heap,
                        (new_dist, new_stops, nbr)
                    )
        
        min_dist = min(dist[dst])
        return min_dist if min_dist != float('inf') else -1
