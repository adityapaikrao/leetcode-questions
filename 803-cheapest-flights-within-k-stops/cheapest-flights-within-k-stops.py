class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # k stops == k + 1 edges
        dist = [[float('inf')] * n for _ in range(k + 2)]
        dist[0][src] = 0

        for l in range(1, k + 2):
            dist[l][:] = dist[l-1][:].copy()
            for u, v, w in flights:
                if dist[l][v] > dist[l-1][u] + w:
                    dist[l][v] = dist[l-1][u] + w
        
        return dist[k + 1][dst] if dist[k + 1][dst] != float('inf') else -1
