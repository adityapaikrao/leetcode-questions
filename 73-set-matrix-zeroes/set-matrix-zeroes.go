func setZeroes(matrix [][]int)  {
    n := len(matrix)
    m := len(matrix[0])
    firstColZero := false

    // first pass: get all zeroed rows & cols flags
    // if first el in row == 0 => entire row zero
    // if first el in col == 0 => entire col zero (except first col)
    // if firstColzero => first col zero
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

    // mark all non edge elements to avoid overwriting flags
    for i := 1; i < n; i++{
        for j:= 1; j < m; j++{
            if matrix[i][0] == 0 || matrix[0][j] == 0{
                matrix[i][j] = 0
            }
        }
    }

    // do first row first o.w firstcolzero can set first row element to zero
    if matrix[0][0] == 0{
        for j := range m{
            matrix[0][j] = 0
        }
    }

    // finally
    if firstColZero{
        for i := range n {
            matrix[i][0] = 0
        }
    }
}