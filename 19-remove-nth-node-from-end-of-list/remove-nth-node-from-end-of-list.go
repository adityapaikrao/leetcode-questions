/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    if head.Next == nil {
        return nil
    }

    dummy := &ListNode{Next: head}
    itr := dummy.Next

    for range n {
        itr = itr.Next
        if itr == nil {
            return head.Next
        }
    }   
    newItr := dummy.Next

    for itr.Next != nil {
        itr = itr.Next
        newItr = newItr.Next
    }

    newItr.Next = newItr.Next.Next
    return dummy.Next
}