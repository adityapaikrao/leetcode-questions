func setZeroes(matrix [][]int)  {
    n := len(matrix)
    m := len(matrix[0])
    firstColZero := false

    for i := range n{
        for j:= range m{
            if matrix[i][j] == 0{
                matrix[i][0] = 0
                if j == 0{
                    firstColZero = true
                } else {
                    matrix[0][j] = 0
                }
            }
        }
    }

    for i := 1; i < n; i++{
        for j:= 1; j < m; j++{
            if matrix[i][0] == 0 || matrix[0][j] == 0{
                matrix[i][j] = 0
            }
        }
    }

    if matrix[0][0] == 0{
        for j := range m{
            matrix[0][j] = 0
        }
    }

    if firstColZero{
        for i := range n {
            matrix[i][0] = 0
        }
    }
}