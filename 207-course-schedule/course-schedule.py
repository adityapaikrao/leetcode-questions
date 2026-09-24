class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visited = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        def dfs(node: int) -> bool:
            visited[node] = 1 # mark as currently visiting
            for nbr in adj[node]:
                if visited[nbr] == 1:
                    return False
                elif visited[nbr] == 2: continue
                if not dfs(nbr): return False
            visited[node] = 2
            return True
        
        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course): return False
            
        return True