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

}