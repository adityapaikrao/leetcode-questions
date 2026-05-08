/*
3 2 4 -3 5 3 6 7
          
window = [3, 4]

- remove out of bounds elem at each iteration from front
- pop all smaller elems than curr from back

- will need deque to handle push from back & pop from front
*/

func maxSlidingWindow(nums []int, k int) []int {
    maxWindow := make([]int, 0, len(nums) - k)
    q := make([]int, 0, k)

    for i := range len(nums) {
        // remove all out of bound elems from front
        for len(q) > 0 && q[0] <= i - k {
            q = q[1:] // pop from front
        }

        // pop all smaller elems from back 
        for len(q) > 0 && nums[q[len(q) - 1]] <= nums[i] {
            q = q[:len(q) - 1]
        }

        q = append(q, i) // add curr elem 

        if i >= k - 1{
            maxWindow = append(maxWindow, nums[q[0]])
        }

    }

    return maxWindow

}