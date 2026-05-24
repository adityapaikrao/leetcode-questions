func longestConsecutive(nums []int) int {
    set := make(map[int]bool, 0)
    for _, num := range nums {
        set[num] = true
    }
    maxLen := 0

    for num := range set {
        if !set[num - 1] && set[num]{
            currLen := 1 
            for set[num + 1] {
                currLen++
                num++
            }
            maxLen = max(maxLen, currLen)
        } 
    }

    return maxLen
}