/*
-1 1 3 4
 m
i

*/
import (
    "slices"
)


func firstMissingPositive(nums []int) int {
    slices.Sort(nums)

    i := 0
    j := len(nums) - 1

    for i <= j{
        mid := i + (j - i) / 2
        if nums[mid] <= 0{
            i = mid + 1
        } else {
            j = mid - 1
        }
    }

    curr := 1
    for idx := i; idx < len(nums); idx++{
        if idx > 0 && nums[idx] == nums[idx - 1]{
            continue
        }
        if nums[idx] != curr{
            return curr
        }
        curr++
    }

    return curr

}