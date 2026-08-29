# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        
        def getLCA(p, q, node) -> 'TreeNode':
            # Base Cases
            if p.val < node.val and q.val > node.val:
                return node
            if node.val == p.val:
                return p 
            elif node.val == q.val:
                return q
            
            # Recursive cases
            if q.val < node.val:
                return getLCA(p, q, node.left)
            else:
                return getLCA(p, q, node.right)
        
        return getLCA(p, q, root)
        
