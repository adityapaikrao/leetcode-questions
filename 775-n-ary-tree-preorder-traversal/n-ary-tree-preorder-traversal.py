"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []

        order = []
        stack = [root]

        while stack:
            curr = stack.pop()
            order.append(curr.val)
            temp = []
            for child in curr.children:
                temp.append(child)
            
            temp.reverse()
            stack.extend(temp)
        
        return order
