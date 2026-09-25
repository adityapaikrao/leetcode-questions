class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = {}

        for node in range(n):
            if node not in color:
                color[node] = 0 # mark it in one set
                q = deque([node])

                while q:
                    curr = q.popleft()

                    for nbr in graph[curr]:
                        if nbr in color and color[nbr] == color[curr]:
                            return False
                        if nbr not in color:
                            color[nbr] = 1 - color[curr]
                            q.append(nbr)
        
        return True
