class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        a / b = 2
        b / c = 3
          3    2
        c -> b -> a
          <-   <-
          1/3  0.5

        a / c = ? a / b * b / c
        b / a = 0.5
        a / e = -1
        a / a = 1 
        x / x = -1 
        """
        adj = defaultdict(list) # varX -> varY
        for eq, val in zip(equations, values):
            adj[eq[1]].append((eq[0], val))
            adj[eq[0]].append((eq[1], 1 / val))
        

        def compute_exp(source: str, dest: str) -> int:
            frontier = [(1, source)]
            seen = set()
            while frontier:
                curr_val, curr_var = frontier.pop()
                if curr_var == dest:
                    return curr_val
                
                for next_var, next_mult in adj[curr_var]:
                    if next_var not in seen:
                        seen.add(next_var)
                        frontier.append((curr_val * next_mult, next_var))
            return -1
        
        evals = []
        for query in queries:
            dest, source = query
            if source not in adj or dest not in adj:
                evals.append(-1)
                continue
            evals.append(compute_exp(source, dest))
        
        return evals