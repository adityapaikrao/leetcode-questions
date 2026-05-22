func uniquePathsIII(grid [][]int) int {
    numPaths := 0
    n := len(grid)
    m := len(grid[0])
    startX, startY := -1, -1
    numEmpty := 0

    for i := range n {
        for j := range m {
            if grid[i][j] == 1 {
                startX, startY = i, j
            }   
            if grid[i][j] == 0 {
                numEmpty++
            }
        }
    }
    
    var dfs func(rowIdx, colIdx int)
    dfs = func(rowIdx, colIdx int) {
        // fmt.Println(rowIdx, colIdx, grid[rowIdx][colIdx])
        if grid[rowIdx][colIdx] == 2 && numEmpty == 0 {
            numPaths++
            // fmt.Println("numpaths:", numPaths)
            return
        }

        // Recurse 
        temp := grid[rowIdx][colIdx]
        grid[rowIdx][colIdx] = -1 // mark as visited

        for _, offset := range [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}{
            newX := rowIdx + offset[0]
            newY := colIdx + offset[1]

            if newX >= 0 && newX < n && newY >= 0 && newY < m && grid[newX][newY] != -1 {
                if grid[newX][newY] == 0 {
                    numEmpty--
                }
                dfs(newX, newY)

                if grid[newX][newY] == 0 {
                    numEmpty++
                }
            }
        }

        grid[rowIdx][colIdx] = temp
        return
    }

    dfs(startX, startY)

    return numPaths
}