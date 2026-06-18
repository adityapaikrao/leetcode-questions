# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
 ------
    -------
2   1   3-> 5-> 6-> 4-> 7
d1
    d2
                        o
                            e

2-> 3 -> 6 ->  7 
1-> 5 -> 4 -> N

o.next = e.next
o = e.next
e.next = o.next
e = e.next

----- end loop when e null & o.next = d2 ----

2   1   3-> 5-> 6-> 4
d1
    d2
                o
                    e

2-> 3 -> 6 
1-> 5 -> 4

if e.next:
    o.next = e.next
    o = e.next
    e.next = o.next
    e = e.next
else:
    -- its done! o.next = d2

"""
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If <= 2 nodes, already grouped
        if not head or not head.next or not head.next.next:
            return head
        
        d1 = head
        d2 = head.next

        o = head
        e = head.next

        while e and e.next:
            o.next = e.next
            o = e.next
            e.next = o.next
            e = e.next
        
        o.next = d2
        return d1

        
