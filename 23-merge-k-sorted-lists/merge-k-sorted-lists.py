# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        idx1 0[1, 4, 5]
        idx2 1[1, 3, 4]
        idx3 2[2, 6]

        [1, 1, 2, 3, 4, 4, 5, 6]

        - min heap of linked list vals
        - pop at each stage & add the next elem in heap
        - add popped elem to sorted LL

        heap = 1 [(1, idx1, node1), (1, idx2, node2)]

        Aproach:
        - build heap with (node.val, idx, node) from heads of lists
        - dummy head of new linked list
        while heap:
            val, idx, node = heap.pop()
            add node to new linked list
            
            next_node = node.next 
            push next_node in heap

        """
        heap = [] # (node.val, idx, node)
        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, idx, head))
        
        dummy = ListNode()
        itr = dummy

        while heap:
            val, idx, node = heapq.heappop(heap)
            itr.next = node
            
            next_node = node.next
            if next_node:
                heapq.heappush(heap, (next_node.val, idx, next_node))
            
            itr = itr.next
        
        return dummy.next
