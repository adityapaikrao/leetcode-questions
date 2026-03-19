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

    prev := make([]int, 2)

    for i := len(prices) - 1; i >= 0; i--{
        curr := make([]int, 2)
        for j:= 1; j >= 0; j--{
            if j == 1{
                curr[j] = max(prev[j], prev[0] - prices[i] - fee)
            } else{
                curr[j] = max(prev[j], prev[1] + prices[i])
            }
        }
        copy(prev, curr)
    }

    return prev[1]
}