func numDistinct(s string, t string) int {
    
    memo := make([][]int, len(s) + 1)
    for i := range memo{
        memo[i] = make([]int, len(t) + 1)
        for j := range memo[i]{
            memo[i][j] = -1
        }
    }
    memo[len(s)][len(t)] = 1

    var solve func(i, j int) int 
    solve = func(i, j int) int {
        if memo[i][j] != -1{
            return memo[i][j]
        }

        // Base Cases:
        if j == len(t) {
            return 1
        }
        if i == len(s) {
            return 0
        }

        // Recurrence
        numWays := 0
        if s[i] == t[j] {
            numWays += solve(i + 1, j + 1)
        }
        numWays += solve(i + 1, j) 

        memo[i][j] = numWays
        return numWays
    }
    solve(0, 0)
    return solve(0, 0)

}