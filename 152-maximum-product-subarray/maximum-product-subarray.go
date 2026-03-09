import (
    "math"
)

/*
-2 1 0 8 -1

prefix = -2 -2 0 8 -8
suffix =  -2 1 0 -8 -1


*/

func maxProduct(nums []int) int {
    maxProd := math.MinInt32
    prefixProd := make([]int, len(nums))
    suffixProd := make([]int, len(nums))
    prev := 1

    for i := range nums {
        prefixProd[i] = prev * nums[i]
        prev = prefixProd[i]
        if prefixProd[i] == 0{
            prev = 1
        }
        maxProd = max(maxProd, nums[i], prefixProd[i])
    }

    prev = 1
    for i := len(nums) - 1; i >= 0; i--{
        suffixProd[i] = prev * nums[i]
        prev = suffixProd[i]
        if suffixProd[i] == 0{
            prev = 1
        }
        maxProd = max(maxProd, nums[i], suffixProd[i])
    }

    return maxProd

}