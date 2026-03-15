func numDistinct(s string, t string) int {
    if len(t) > len(s){
        return 0
    }

    dp := make([][]int, len(t) + 1)
    for i := range dp{
        dp[i] = make([]int, len(s) + 1)
    }

    for i := range dp{
        dp[i][len(s)] = 0
    }

    for j := range dp[0]{
        dp[len(t)][j] = 1
    }

    for i := len(t) - 1; i >= 0; i--{
        for j := len(s) - 1; j >= 0; j--{
            if t[i] == s[j]{
                dp[i][j] += dp[i + 1][j + 1]
            }
            dp[i][j] += dp[i][j + 1]
        }
    }

    return dp[0][0]

}