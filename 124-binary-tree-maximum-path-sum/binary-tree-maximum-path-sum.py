# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        At each node:
            - self value
            - self + left max
            - self + right max
            - self + left max + right max
        """
        max_sum = float('-inf')
        def solve(node: TreeNode) -> None:
            nonlocal max_sum
            # Base Case
            if not node:
                return 0
            
            left_sum, left_max = 0, solve(node.left)
            right_sum, right_max = 0, solve(node.right)

            if left_max > 0:
                left_sum = left_max
            if right_max > 0:
                right_sum = right_max

            max_sum = max(max_sum, node.val + left_sum + right_sum)

            return max(node.val + left_sum, node.val + right_sum)
        
        solve(root)

        return max_sum