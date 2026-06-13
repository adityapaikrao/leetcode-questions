class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        0 -> 1

        0 -> 1 -> 3
          -> 2 -> 

        topological ordering: Kahn's
        """
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
        
        q = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                in_degree[course] -= 1
                q.append(course)
        
        if not q: return []
        # print(q, in_degree)
        order = []
        while q:
            curr_course = q.popleft()
            order.append(curr_course)

            for next_course in adj[curr_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    in_degree[next_course] -= 1
                    q.append(next_course)
        
        return order if len(order) == numCourses else []
