func getPermutation(index int, nums *[]int, allPermutations *[][]int){
    if index == len(*nums){
        currPermutation := make([]int, len(*nums))
        copy(currPermutation, *nums)
        *allPermutations = append(*allPermutations, currPermutation)
        return
    }

    // choose what number to place at current index
    for i := index; i < len(*nums); i++{
        (*nums)[i], (*nums)[index] = (*nums)[index], (*nums)[i]
        getPermutation(index + 1, nums, allPermutations)
        // backtrack
        (*nums)[i], (*nums)[index] = (*nums)[index], (*nums)[i]
        
    }
    return
}


func permute(nums []int) [][]int {
    allPermutations := make([][]int, 0)
    getPermutation(0, &nums, &allPermutations)

    return allPermutations
}