import (
    "math"
)

func coinChange(coins []int, amount int) int {
    dp := make([]int, amount + 1)
    for i := range dp{
        dp[i] = math.MaxInt
    }
    dp[0] = 0

    for i := 1; i <= amount; i++{
        for _, coin := range coins{
            if coin > i{
                continue
            }
            if dp[i - coin] != math.MaxInt {
                dp[i] = min(dp[i - coin] + 1, dp[i])
            }
        }
    }

    if dp[amount] == math.MaxInt{
        return -1
    }

    return dp[amount]
}