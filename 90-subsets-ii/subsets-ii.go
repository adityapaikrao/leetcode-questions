/*
[1, 2, 2]
            []
        [1].                 []
    [1,2]      [1]       [2].      []
[1,2,2] [1,2] [1,2] [1] [2,2] [2] [2] []

- can create duplicates on the dont choose path if choosing num already skipped
- either pick or skip & never pick 
*/

import (
    "sort"
)

func getSubset(index int, nums *[]int, currSubset *[]int, powerSet *[][]int){
    if index == len(*nums){
        currSubsetCopy := make([]int, len(*currSubset))
        copy(currSubsetCopy, *currSubset)
        *powerSet = append(*powerSet, currSubsetCopy)
        return
    }

    // choose
    *currSubset = append(*currSubset, (*nums)[index])
    getSubset(index + 1, nums, currSubset, powerSet)
    *currSubset = (*currSubset)[:len(*currSubset) - 1]

    // skip all instances of element
    i := index
    for i < len(*nums) && (*nums)[i] == (*nums)[index]{
        i++
    }
    getSubset(i, nums, currSubset, powerSet)
    return
}


func subsetsWithDup(nums []int) [][]int {
    currSubset := make([]int, 0, len(nums))
    powerSet := make([][]int, 0)
    sort.Ints(nums)

    getSubset(0, &nums, &currSubset, &powerSet)

    return powerSet
}