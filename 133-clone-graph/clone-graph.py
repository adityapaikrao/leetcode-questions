"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
hmap = {1:1n, 2:2n, 4:4n, 3:3n}
1n -> [2n, 4n]
2n -> [1n, 3n]
4n -> [1n]
3n -> [2n]

curr = 4

q = [3]
vis = [1, 2, 4, 3]
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        new_node = Node(val = node.val)
        hmap = {node:new_node} # old nodes -> new nodes

        # Do BFS traversal and create new nodes as we traverse
        q = deque([node])
        visited = set([node])

        while q:
            curr = q.popleft()
            
            for nbr in curr.neighbors:
                if nbr not in hmap:
                    hmap[nbr] = Node(val=nbr.val)
            
                hmap[curr].neighbors.append(hmap[nbr])
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        

        return new_node
                
