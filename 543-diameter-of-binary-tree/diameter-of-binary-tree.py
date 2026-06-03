# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        height of left subtree + height of right subtree + 1 = diameter
        max_diam = 1

        def compute_height(node) - > int:
            lh = compute_height(node.left)
            rh = compute_height(node.right)

            diam = lh + rh + 1
            update max diam

            return max(lh, rh) + 1
        """
        max_diam = 1

        def get_height(node: Optional[TreeNode]) -> int:
            nonlocal max_diam
            if not node:
                return 0
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)

            max_diam = max(max_diam, left_height + right_height + 1)

            return max(left_height, right_height) + 1
        
        get_height(root)
        return max_diam - 1