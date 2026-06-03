# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        node balanced iff
            - left subtree balanced
            - right subtree balanced
            - abs(lh - rh) <= 1
        """

        def tree_balanced(node: Optional[TreeNode]) -> Tuple[int, bool]:
            if not node:
                return 0, True
            
            left_height, left_balanced = tree_balanced(node.left)
            right_height, right_balanced = tree_balanced(node.right)
            subtree_height = max(left_height, right_height) + 1

            if not (left_balanced and right_balanced):
                return subtree_height, False
            
            if abs(left_height - right_height) > 1:
                return subtree_height, False
            
            return subtree_height, True
        
        return tree_balanced(root)[1]