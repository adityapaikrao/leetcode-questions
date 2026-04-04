from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        1 -> 2 -> 7
        3 -> 6 -> 7

        """
        if source == target:
            return 0
        
        adj = [set() for _ in range(len(routes))] # bus_index -> bus index
        visited = [False] * len(routes)
        routes = [set(route) for route in routes]
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if routes[i] & routes[j]:
                    adj[i].add(j)
                    adj[j].add(i)
        
        q = deque() # source buses
        for i, route in enumerate(routes):
            if source in route:
                if target in route:
                    return 1
                q.append(i)
        
        if not q:
            return -1

        # print(f"{adj} \n {q}")
        num_buses = 1

        while q: # run multi-source bfs
            for _ in range(len(q)):
                curr_bus = q.popleft()
                if visited[curr_bus]: continue

                visited[curr_bus] = True
                for next_bus in adj[curr_bus]:
                    if target in routes[next_bus]:
                        return num_buses + 1
                    if not visited[next_bus]:
                        q.append(next_bus)
                
            num_buses += 1
        
        return -1