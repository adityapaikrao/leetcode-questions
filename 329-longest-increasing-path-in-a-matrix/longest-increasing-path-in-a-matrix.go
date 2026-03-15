func inBounds(i, j, numRows, numCols int) bool {
    return i >= 0 && i < numRows && j >= 0 && j < numCols
}

func longestIncreasingPath(matrix [][]int) int {
    n, m := len(matrix), len(matrix[0])
    memo := make([][]int, n)
    for i := range memo{
        memo[i] = make([]int, m)
        for j := range memo[i]{
            memo[i][j] = -1
        }
    }

    var dfs func(i, j int) int
    dfs = func(i, j int) int {
        if memo[i][j] != -1 {
            return memo[i][j]
        }
        longestLen := 1

        for _, offset := range [][2]int{{0, -1}, {0, 1}, {-1, 0}, {1, 0}}{
            new_i := i + offset[0]
            new_j := j + offset[1]
            if inBounds(new_i, new_j, n, m) && matrix[new_i][new_j] > matrix[i][j] {
                longestLen = max(longestLen, dfs(new_i, new_j) + 1)
            }
        }
        memo[i][j] = longestLen
        return longestLen
    }

    maxLen := 1
    for i := range n {
        for j := range m {
            maxLen = max(maxLen, dfs(i, j))
        }
    }

    return maxLen
}