# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Serialization -> can be any tree-traversal algorithm
                    - pre-order
                    - in-order
                    - post-order
                    - dfs
                    - bfs
                -> should be uniquely de-serializable
De-serialization -> build from serialized representation

pre [1, 2, 3, 4, 5] S L R
in  [2, 1, 4, 3, 5] L S R
post [2, 4, 5, 3, 1] L R S 

all of them are missing info about null childs -> serialise null nodes too

pre [1, 2, N, N, 3, 4, N, N, 5, N, N] -> can be uniquely de-serialized
                                i

root = 5
stack = []
    
if root not null:
    if !root.left:
        root.left = node
        stack.append(node)
        root = node
        i++
    else:
        root.right = node
        root = node
        i++

if root is null:
    stack.pop.right = node
    root = stack.pop
    i++

    1 
  2       3
N   N   4.  5
       N N

"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder = []
        stack = [root]

        def pre_order_traversal(node: Optional[TreeNode]):
            if not node:
                preorder.append("N")
                return 
            
            preorder.append(str(node.val))
            pre_order_traversal(node.left)
            pre_order_traversal(node.right)

            return
        
        pre_order_traversal(root)
        return "#".join(preorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None

        preorder = data.split("#")
        i = 0

        def build_tree():
            nonlocal i
            if i >= len(preorder):
                return None
            
            if preorder[i] == "N":
                i += 1
                return None
            
            root = TreeNode(int(preorder[i]))
            i += 1
            root.left = build_tree()
            root.right = build_tree()

            return root
        
        return build_tree()
            
            




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))