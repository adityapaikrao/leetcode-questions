"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        order = []

        def postorder_helper(node: Node) -> None:
            if not node:
                return 
            
            for child in node.children:
                if child: postorder_helper(child)
            
            order.append(node.val)

        postorder_helper(root)
        return order