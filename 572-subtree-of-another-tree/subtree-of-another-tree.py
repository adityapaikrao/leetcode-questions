# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(rootA: Optional[TreeNode], rootB: Optional[TreeNode]) -> bool:
            if (not rootA) and (not rootB):
                return True
            if not (rootA and rootB): return False
            
            if rootA.val != rootB.val: return False

            return isSameTree(rootA.left, rootB.left) and isSameTree(rootA.right, rootB.right)
        
        q = [root]

        while q:
            node = q.pop()
            if isSameTree(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False
            