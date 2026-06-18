# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = defaultdict(list)
        q = deque([(root, 0)])

        while q:
            curr_order = defaultdict(list)
            for _ in range(len(q)):
                curr, col_index = q.popleft()
                curr_order[col_index].append(curr.val)

                if curr.left:
                    q.append((curr.left, col_index - 1))
                if curr.right:
                    q.append((curr.right, col_index + 1))
            
            for index, node_vals in curr_order.items():
                node_vals.sort()
                order[index].extend(node_vals)
        
        traversal = []
        for key in sorted(order.keys()):
            traversal.append(order[key])
        
        return traversal