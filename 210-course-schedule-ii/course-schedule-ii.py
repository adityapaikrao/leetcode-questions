class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        for curr, prev in prerequisites:
            adj[prev].append(curr)
            in_degree[curr] += 1
        
        q = deque([])
        for course in range(n):
            if in_degree[course] == 0: 
                q.append(course)
                in_degree[course] -= 1 
        
        if not q: 
            return []
        
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nbr in adj[node]:
                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    q.append(nbr)
                    in_degree[nbr] -= 1
        
        return order if len(order) == n else []
        