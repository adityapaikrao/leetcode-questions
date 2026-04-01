func maxSlidingWindow(nums []int, k int) []int {
    q := make([]int, 0, k)
    maxWindow := make([]int, 0, len(nums) - k + 1)

    for i := range nums {
        // remove out of window elems
        if len(q) > 0 && q[0] <= i - k {
            q = q[1:]
        }
        // remove smaller elems from q back
        for len(q) > 0 && nums[q[len(q) - 1]] <= nums[i] {
            q = q[:len(q) - 1]
        }

        q = append(q, i)

        if i >= k - 1{
            maxWindow = append(maxWindow, nums[q[0]])
        }
    }

    return maxWindow    
}