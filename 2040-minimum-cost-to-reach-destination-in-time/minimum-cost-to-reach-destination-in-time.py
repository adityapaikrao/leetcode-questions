"""

0 -> 1 -> 2 -> 
                5
  -> 3 -> 4 ->

"""


class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        n = len(passingFees)
        adj = [[] for _ in range(len(passingFees))]
        for src, dst, time in edges:
            adj[src].append((dst, time))
            adj[dst].append((src, time))
        
        costs = [float('inf')] * n
        # costs[0] = passingFees[0]

        heap = [(0, passingFees[0], 0)] # time, fees, node
        while heap:
            curr_time, curr_cost, curr_node = heapq.heappop(heap)
            if curr_cost >= costs[curr_node]: continue

            costs[curr_node] = curr_cost
            for nbr, wt in adj[curr_node]:
                new_cost = curr_cost + passingFees[nbr]
                new_time = curr_time + wt
                if new_time <= maxTime and (new_cost < costs[nbr]):
                    heapq.heappush(heap, (new_time, new_cost, nbr))
        return costs[-1] if costs[-1] != float('inf') else -1
