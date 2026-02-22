func setZeroes(matrix [][]int)  {
    n := len(matrix)
    m := len(matrix[0])
    rowZero := make([]bool, n)
    colZero := make([]bool, m)

    for i := range n{
        for j := range m{
            if matrix[i][j] == 0{
                rowZero[i] = true
                colZero[j] = true
            }
        }
    }

    for i := range n{
        for j:= range m{
            if rowZero[i] || colZero[j]{
                matrix[i][j] = 0
            }
        }
    }
}