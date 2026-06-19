class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for source, dest, cost in flights:
            adj[source].append((dest, cost))
        
        costs = [float('inf')] * n
        stops = [float('inf')] * n
        stops[src] = 0
        costs[src] = 0

        q = deque([(0, 0, src)]) # num_stops, curr_cost, node
        while q:
            curr_stops, curr_cost, curr_node = q.popleft()
            # if costs[curr_node] >= curr_cost and stops[curr_node] >= curr_stops: continue

            if curr_stops >= k + 1: break
            for nbr, cost in adj[curr_node]:
                new_cost = curr_cost + cost
                new_stops = curr_stops + 1
                if new_stops < stops[nbr] or new_cost < costs[nbr]:
                    if new_stops < stops[nbr]: stops[nbr] = new_stops
                    if new_cost < costs[nbr]: costs[nbr] = new_cost
                    
                    q.append((new_stops, new_cost, nbr))
        
        return costs[dst] if costs[dst] != float('inf') else -1
