/*
10 6 8 5 11 9
i
3  1 2 1  1  0
          
stack = [11, 8, 6]

- if last person on stack is taller:
    append to stack & set ans to 1
- until last person is smaller pop:
    count popped persons
    set ans to popped + (1 if stack else 0)
    append to stack

5 1 2 3 10
i
4  1 1 1  0
stack = [10, 5]

*/


func canSeePersonsCount(heights []int) []int {
    canSee := make([]int, len(heights))
    stack := []int{heights[len(heights) - 1]}

    for i := len(heights) - 2; i >= 0; i--{
        // fmt.Println(heights[i], stack)
        if len(stack) == 0 || stack[len(stack) - 1] > heights[i] {
            stack = append(stack, heights[i])
            canSee[i] = 1
            continue
        }

        numPersons := 0
        for len(stack) > 0 && stack[len(stack) - 1] < heights[i] {
            stack = stack[:len(stack) - 1]
            numPersons++
        }

        canSee[i] = numPersons
        if len(stack) > 0 {canSee[i]++}
        stack = append(stack, heights[i])

    }

    return canSee
}