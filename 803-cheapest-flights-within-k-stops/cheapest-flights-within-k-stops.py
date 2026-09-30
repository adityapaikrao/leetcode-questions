class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # k stops == k + 1 edges
        dist = [[float('inf')] * n for _ in range(2)]
        dist[0][src] = 0
        prev = 0

        for l in range(1, k + 2):
            curr = 1 - prev
            dist[curr][:] = dist[prev][:].copy()
            changed = False
            for u, v, w in flights:
                if dist[curr][v] > dist[prev][u] + w:
                    changed = True
                    dist[curr][v] = dist[prev][u] + w
            if not changed: return dist[curr][dst] if dist[curr][dst] != float('inf') else -1
            prev = curr
        
        return dist[prev][dst] if dist[prev][dst] != float('inf') else -1
