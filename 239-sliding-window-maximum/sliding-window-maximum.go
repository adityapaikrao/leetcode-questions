/*
5 3 6 0 0 0
            

q = [6, 0, 0, 0]
- remove out of window elems from queue front (need to store indices in the q)
- remove smaller elems from the queue back
- max is at q front

5 
max window: 
*/

func maxSlidingWindow(nums []int, k int) []int {
    q := make([]int, 0, k)
    maxWindow := make([]int, 0, len(nums) - k + 1)

    for i := range nums {
        // remove out of window elems
        for len(q) > 0 && q[0] <= i - k {
            q = q[1:]
        }
        // remove smaller elems from q back
        for len(q) > 0 && nums[q[len(q) - 1]] < nums[i] {
            q = q[:len(q) - 1]
        }

        q = append(q, i)

        if i >= k - 1{
            maxWindow = append(maxWindow, nums[q[0]])
        }
    }

    return maxWindow    
}