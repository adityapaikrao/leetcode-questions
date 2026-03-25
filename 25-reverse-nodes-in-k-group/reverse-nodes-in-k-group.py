# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
            1 -> 2 -> 3 -> 4 -> 5
                 c
            cs
        pe

        count 2

        """
        def reverseLL(node: ListNode) -> None:
            prev = None
            curr = node

            while curr:
                tmp = curr.next
                
                curr.next = prev
                prev = curr
                curr = tmp

            return prev
        

        dummy = ListNode()
        prev_end = dummy

        curr = head

        while curr:
            count = 1
            curr_start = curr

            while curr.next and count != k:
                curr = curr.next
                count += 1
            
            if count < k:
                break
            
            # isolate curr group
            tmp = curr.next
            prev_end.next = None
            curr.next = None

            new_start = reverseLL(curr_start)

            # connect back in-list
            prev_end.next = new_start
            curr_start.next = tmp

            # update curr for next iteration
            curr = curr_start.next
            prev_end = curr_start
        
        return dummy.next






            

            