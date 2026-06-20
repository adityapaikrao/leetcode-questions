class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj = [[] for _ in range(n)]
        for curr, prev in prerequisites:
            adj[prev].append(curr)
        
        visited = [0] * n
        def dfs(node: int) -> None:
            visited[node] = 1
            for nbr in adj[node]:
                if visited[nbr] == 1: return False
                if visited[nbr] != 2: 
                    if not dfs(nbr): return False
            visited[node] = 2
            return True

        for course in range(n):
            if visited[course] == 0:
                if not dfs(course): return False
        return True
        