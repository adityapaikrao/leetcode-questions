/*
[0, 1, 2] -> ideally should be 1 2 3 -> 4 [1, n]
- mark presence of number using indices [0, n-1]
- if i is present mark it using index i - 1: set to 1?
        0, 1, 2 -> 1, 1, 2 : works
        3, 4, 2, 1 ->  1, 4, 1, 1 : doesnt work (2 instead of 5)
        - overwriting future values: set to -ve instead & check absolute value?
        3, 4, 2, 1 -> -3, -4, -2, -1: works!
        0, 1, 2 -> -0, 1, 2 : zeros will cause issues
            - in one pass check if 1 present & convert nums not in [1, n] to 1 

*/

func firstMissingPositive(nums []int) int {
    onePresent := false
    n := len(nums)

    for i := range nums {
        if nums[i] == 1{
            onePresent = true
        } else if nums[i] < 1 || nums[i] > n{
            nums[i] = 1
        }
    }

    if !onePresent{
        return 1
    }

    for i := range nums {
        absVal := max(nums[i], -nums[i])
        if nums[absVal - 1] > 0 {
            nums[absVal - 1] *= -1
        }
    }

    for i := range nums {
        if nums[i] > 0 {
            return i + 1
        }
    }

    return n + 1
}