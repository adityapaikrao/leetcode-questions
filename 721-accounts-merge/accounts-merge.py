class UnionFind:
    def __init__(self, n: int):
        self.size = [1] * n
        self.parents = [i for i in range(n)]
    
    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.size[root_x] >= self.size[root_y]:
                self.size[root_x] += self.size[root_y]
                self.parents[root_y] = root_x
            else:
                self.size[root_y] += self.size[root_x]
                self.parents[root_x] = root_y

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        """
                      0                       0 
        "John","johnsmith@mail.com","john_newyork@mail.com"
                     0                      0
        "John","johnsmith@mail.com","john00@mail.com"
        "Mary","mary@mail.com"
        "John","johnnybravo@mail.com"
        """
        n = len(accounts)
        idx_to_mails = {}
        for i in range(n):
            idx_to_mails[i] = set(accounts[i][1:])
        
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if len(idx_to_mails[i] & idx_to_mails[j]) > 0:
                    uf.union(i, j)
        
        merged = defaultdict(set) # idx -> accounts
        for i in range(n):
            root = uf.find(i)
            merged[root].update(idx_to_mails[i])
        
        return [[accounts[key][0]] + [mail for mail in sorted(val)] for key, val in merged.items()]



        