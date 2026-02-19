# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = []
        def preorder(node):
            if not node:
                nodes.append("N")
                return
            
            nodes.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

            # print(node.val, nodes)
            return
        preorder(root)
        # print("S:", nodes)
        return ",".join(nodes)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == ",":
            return None
        # print("R:", data)
        data = data.split(",")
        index = 0
        def build_tree():
            nonlocal index
            if data[index] == "N":
                index += 1
                return None
            
            curr_node = TreeNode(data[index])
            index += 1

            curr_node.left = build_tree()
            curr_node.right = build_tree()
            
            return curr_node
        
        return build_tree()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))