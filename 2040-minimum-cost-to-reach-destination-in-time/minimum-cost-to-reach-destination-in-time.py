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
        
        times = [float("inf")] * n
        heap = [(passingFees[0], 0, 0)] # cost, time, node

        while heap:
            curr_cost, curr_time, curr_node = heapq.heappop(heap)
            if times[curr_node] <= curr_time: continue
            if curr_node == n - 1: return curr_cost

            times[curr_node] = curr_time
            for nbr, wt in adj[curr_node]:
                new_time = curr_time + wt
                new_cost = curr_cost + passingFees[nbr]
                if new_time <= maxTime and new_time < times[nbr]:
                    heapq.heappush(heap, (new_cost, new_time, nbr))

        return -1