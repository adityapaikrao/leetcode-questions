# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """
        2 4 3 

        5 6 8

        7 0 2 1
        """
        carry = 0
        dummy = ListNode()
        curr_node = dummy
        
        while l1 or l2 or carry:
            curr_sum = carry
            if l1: 
                curr_sum += l1.val
                l1 = l1.next
            if l2: 
                curr_sum += l2.val
                l2 = l2.next

            digit = curr_sum % 10
            carry = curr_sum // 10

            curr_node.next = ListNode(digit)
            curr_node = curr_node.next

            
        
        return dummy.next

            
