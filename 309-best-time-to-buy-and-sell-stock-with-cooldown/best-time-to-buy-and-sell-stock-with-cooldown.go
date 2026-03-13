func maxProfit(prices []int) int {
    memo := make([][2]int, len(prices) + 2)
    for i := range len(prices) + 2{
        memo[i] = [2]int{-1, -1}
    }
    memo[len(prices) + 1] = [2]int{0, 0}
    memo[len(prices)] = [2]int{0, 0}

    var solve func(index int, canBuy int) int
    solve = func(index int, canBuy int) int {
        // Base Case: out of bounds
        if index >= len(prices) {
            return 0
        }

        if memo[index][canBuy] != -1{
            return memo[index][canBuy]
        }

        // if canBuy: either buy or skip
        maxProfit := 0
        if canBuy == 1{
            maxProfit = max(solve(index + 1, canBuy), solve(index + 1, canBuy ^ 1) - prices[index])
        } else {
            // sell or skip
            maxProfit = max(solve(index + 1, canBuy),solve(index + 2, canBuy ^ 1) + prices[index])
        }
        memo[index][canBuy] = maxProfit
        return maxProfit
    }   

    return solve(0, 1)
}