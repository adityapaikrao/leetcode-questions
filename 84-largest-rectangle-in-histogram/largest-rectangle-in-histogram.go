func largestRectangleArea(heights []int) int {
    stack := make([][]int, 0) // start_idx, height
    maxArea := 0

    for i := range heights {
        // previous runs can extend
        leftIdx := i
        for len(stack) > 0 && stack[len(stack) - 1][1] > heights[i] {
            prev := stack[len(stack) - 1]
            stack = stack[:len(stack) - 1]
            leftIdx = prev[0]

            area := (i - prev[0]) * prev[1]
            if area > maxArea {
                maxArea = area
            }
        }
        stack = append(stack, []int{leftIdx, heights[i]})
    }
    

    for i := range stack {
        area := (len(heights) - stack[i][0]) * stack[i][1]
        if area > maxArea {
            maxArea = area
        }
    }

    return maxArea
}