func splitArray(nums []int, k int) int {
    sum := 0
    maxVal := -1
    for _, num := range nums{
        sum += num
        if num > maxVal {
            maxVal = num
        }
    }

    
    if k == 1 {
        return sum
    }

    var canSplit func(nums []int, maxSplit int, maxSum int) bool 
    canSplit = func(nums []int, maxSplit int, maxSum int) bool {
        currSum := 0
        k := 1

        for _, num := range nums {
            currSum += num
            if currSum > maxSum{
                currSum = num
                k++
            }
        }

        return k <= maxSplit

    }

    low := maxVal
    high := sum
    minMaxSum := -1

    for low <= high {
        mid := low + (high - low) / 2
        if canSplit(nums, k, mid) {
            high = mid - 1
            minMaxSum = mid
        } else {
            low = mid + 1
        }
    }
    
    return minMaxSum

}