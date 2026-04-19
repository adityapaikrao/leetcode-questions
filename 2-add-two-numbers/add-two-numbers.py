# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        itr = dummy

        while carry or list1 or list2:
            curr_num = carry 
            if list1:
                curr_num += list1.val
                list1 = list1.next

            if list2:
                curr_num += list2.val
                list2 = list2.next
            
            curr = ListNode(curr_num % 10)
            itr.next = curr
            itr = curr

            carry = curr_num // 10
        

        return dummy.next
            
