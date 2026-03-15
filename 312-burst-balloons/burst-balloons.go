func maxCoins(nums []int) int {
    coins := []int{1}
    coins = append(coins, nums...)
    coins = append(coins, 1)

    memo := make([][]int, len(coins))
    for i := range memo{
        memo[i] = make([]int, len(coins))
        for j := range memo[i]{
            memo[i][j] = -1
        }
    }

    var solve func(i, j int) int
    solve = func(i, j int) int{
        if memo[i][j] != -1{
            return memo[i][j]
        }

        // Base Case:
        if i > j{
            return 0
        } 
        if i == j{
            return coins[i] * coins[i-1] * coins[i + 1]
        }

        // Recurrence
        maxCoins := 0
        for k := i; k <= j; k++{
            curr := coins[k] * coins[i-1] * coins[j + 1]
            maxCoins = max(maxCoins, curr + solve(i, k - 1) + solve(k + 1, j))
        }

        memo[i][j] = maxCoins
        return maxCoins

    }

    return solve(1, len(nums))

    dp := make([][]int, len(coins))
    for i := range dp{
        dp[i] = make([]int, len(coins))
        for j := range dp[i]{
            if i > j {
                dp[i][j] = 0
            } 
            if i >= 1 && i < len(coins) {
                dp[i][i] = coins[i] * coins[i-1] * coins[i + 1]
            }
        }
    }

    for l := 1; l <= len(nums); l++{
        for i := 1; i <= len(nums) - l + 1; i++{
            j := i + l - 1
            for k := i; k <= j; k++{
                curr := coins[i-1] * coins[k] * coins[j + 1]
                dp[i][j] = max(dp[i][j], curr + dp[i][k-1] + dp[k+1][j])
            }
        }
    }

    return dp[1][len(nums)]
}