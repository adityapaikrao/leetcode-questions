func maxProfit(prices []int, fee int) int {
    // var solve func(i int, canBuy bool) int
    // solve = func(i int, canBuy bool) int {
    //     // Base Case
    //     if i >= len(prices){
    //         return 0
    //     }

    //     // Recurrence
    //     if canBuy{
    //         return max(solve(i + 1, canBuy), solve(i + 1, !canBuy) - prices[i] - fee)
    //     } 
        
    //     return max(solve(i + 1, canBuy), solve(i + 1, !canBuy) + prices[i])
    // }

    // return solve(0, true)

    dp := make([][]int, len(prices) + 1)
    for i := range dp{
        dp[i] = make([]int, 2)
    }
    dp[len(prices)] = []int{0, 0}

    for i := len(prices) - 1; i >= 0; i--{
        for j:= 1; j >= 0; j--{
            if j == 1{
                dp[i][j] = max(dp[i + 1][j], dp[i+1][0] - prices[i] - fee)
            } else{
                dp[i][j] = max(dp[i+1][j], dp[i+1][1] + prices[i])
            }
        }
    }

    return dp[0][1]
}