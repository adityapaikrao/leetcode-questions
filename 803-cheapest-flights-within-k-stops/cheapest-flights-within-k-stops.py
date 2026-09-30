class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # k stops == k + 1 edges
        dist = [[float('inf')] * n for _ in range(k + 2)]
        dist[0][src] = 0

        for l in range(1, k + 2):
            dist[l][:] = dist[l-1][:].copy()
            changed = False
            for u, v, w in flights:
                if dist[l][v] > dist[l-1][u] + w:
                    changed = True
                    dist[l][v] = dist[l-1][u] + w
            if not changed: return dist[l][dst] if dist[l][dst] != float('inf') else -1
        
        return dist[k + 1][dst] if dist[k + 1][dst] != float('inf') else -1
