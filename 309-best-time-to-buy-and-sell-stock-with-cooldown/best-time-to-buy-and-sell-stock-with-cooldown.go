func maxProfit(prices []int) int {
    dp := make([][2]int, len(prices) + 2)
    for i := range dp{
        dp[i] = [2]int{0, 0}
    }

    for i := len(prices) - 1; i >= 0; i--{
        for j := range 2{
            if j == 1{
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][0] - prices[i])
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i + 2][1] + prices[i])
            }
        }
    }

    return dp[0][1]
}