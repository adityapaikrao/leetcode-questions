# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 or l2 or carry != 0:
            curr_num = carry
            if l1: 
                curr_num += l1.val
                l1 = l1.next
            if l2: 
                curr_num += l2.val
                l2 = l2.next

            carry = curr_num // 10 
            digit = curr_num % 10

            curr.next = ListNode(digit)
            curr = curr.next

        
        return dummy.next