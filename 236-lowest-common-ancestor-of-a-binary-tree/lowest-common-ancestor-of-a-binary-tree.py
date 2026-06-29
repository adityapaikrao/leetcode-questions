# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}

        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left:
                parents[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                parents[curr.right] = curr
                stack.append(curr.right)
        
        ancestors_p = set()
        node = p
        while node:            
            ancestors_p.add(node)
            node = parents[node]

        node = q
        while node:
            if node in ancestors_p:
                break
            node = parents[node]
        
        return node

