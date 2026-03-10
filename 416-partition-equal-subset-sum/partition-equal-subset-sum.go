func canPartition(nums []int) bool {
    target := 0
    for i := range nums{
        target += nums[i]
    }

    if target % 2 != 0 {
        return false
    }
    target /= 2

    dp := make([][]bool, target + 1)
    for i := range target + 1{
        dp[i] = make([]bool, len(nums) + 1)
    }
    
    // Base Case: when target is zero; always one empty subset
    for i := range len(nums) + 1{
        dp[0][i] = true
    }


    for i := 1; i <= target; i++ {
        for j := 1; j <= len(nums); j++{
            dp[i][j] = dp[i][j-1] // dont take this elem
            if nums[j-1] <= i{
                dp[i][j] = dp[i][j] || dp[i - nums[j-1]][j-1]
            }
        }
    }

    return dp[target][len(nums)]

}