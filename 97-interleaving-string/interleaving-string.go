func boolToInt(b bool) int {
    if b {
        return 1
    }
    return 0
}


func isInterleave(s1 string, s2 string, s3 string) bool {
    if len(s3) != len(s1)+len(s2) {
        return false
    }

    memo := make([][]int, len(s1)+1)
    for i := range len(s1) + 1 {
        memo[i] = make([]int, len(s2)+1)
        for j := range memo[i] {
            memo[i][j] = -1
        }
    }

    var solve func(i, j int) bool
    solve = func(i, j int) bool {
        if memo[i][j] != -1 {
            return memo[i][j] == 1
        }

        k := i + j
        if k >= len(s3) {
            return true
        }
        if i >= len(s1) {
            memo[i][j] = boolToInt(s2[j:] == s3[k:])
            return memo[i][j] == 1
        }
        if j >= len(s2) {
            memo[i][j] = boolToInt(s1[i:] == s3[k:])
            return memo[i][j] == 1
        }

        result := false
        if s1[i] == s3[k] && solve(i+1, j) {
            result = true
        } 
        if s2[j] == s3[k] && solve(i, j+1) {
            result = true
        }

        memo[i][j] = boolToInt(result)
        return result
    }

    return solve(0, 0)
}

