class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
        q = deque()
        for course in range(numCourses):
            if in_degree[course] == 0: q.append(course)
        
        if not q: return False

        numNodes = 0
        while q:
           curr = q.popleft()
           numNodes += 1
           for nbr in adj[curr]:
                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    q.append(nbr)

        return numNodes == numCourses
        