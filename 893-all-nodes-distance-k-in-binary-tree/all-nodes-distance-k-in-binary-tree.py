# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        def dfs(node: TreeNode, parent: Optional[TreeNode] = None):
            parents[node] = parent
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
        dfs(root)

        q = deque([target])
        visited = set([target])
        for _ in range(k):
            for _ in range(len(q)): 
                node = q.popleft()
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                if parents[node] and parents[node] not in visited:
                    q.append(parents[node])
                    visited.add(parents[node])
        return [node.val for node in q]