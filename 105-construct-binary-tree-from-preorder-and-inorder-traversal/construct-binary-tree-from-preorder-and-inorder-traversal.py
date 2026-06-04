# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
          3
        9    20
    2.     15    7
    pre = [3, 9, 2, 15, 20, 15, 7]
    in = [2, 9, 15, 3, 15, 20, 7]

        """
        inorder_map = {num: index for index, num in enumerate(inorder)}
        
        def get_root(perorder, pre_start, pre_end, inorder, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            root = TreeNode(val=preorder[pre_start])
            i = inorder_map[root.val]
            
            root.left = get_root(
                preorder,
                pre_start + 1,
                pre_start + (i - in_start),
                inorder,
                in_start,
                i - 1
            )

            root.right = get_root(
                preorder,
                pre_start + (i - in_start) + 1,
                pre_end,
                inorder,
                i + 1,
                in_end
            )
            
            return root
        
        return get_root(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

            