import (
    "strings"
)

func isValid(placement [][]string, rowIdx, colIdx int) bool{
    // check row 
    for j := range colIdx{
        if placement[rowIdx][j] == "Q"{
            return false
        }
    }

    // check upper diag
    i, j := rowIdx - 1, colIdx - 1
    for i >= 0 && j >= 0{
        if placement[i][j] == "Q"{
            return false
        }
        i--
        j--
    }

    // check lower diag
    i, j = rowIdx + 1, colIdx - 1
    for i < len(placement) && j >= 0{
        if placement[i][j] == "Q"{
            return false
        }
        i++
        j--
    }

    return true
}

func placeQueens(colIdx int, placement [][]string, allPlacements *[][]string) {
    if colIdx == len(placement){
        // add current placement to allPlacements
        currPlacement := make([]string, 0, len(placement))
        for i := range len(placement){
            var builder strings.Builder 
            for j:= range len(placement){
                builder.WriteString(placement[i][j])    
            }
            currPlacement = append(currPlacement, builder.String())
        }
        *allPlacements = append(*allPlacements, currPlacement)
        return
    }

    // choose where to place the Queen
    for rowIdx := range len(placement){
        if isValid(placement, rowIdx, colIdx){
            placement[rowIdx][colIdx] = "Q"
            placeQueens(colIdx + 1, placement, allPlacements)
            placement[rowIdx][colIdx] = "."
        }
    }

}


func solveNQueens(n int) [][]string {
    allPlacements := make([][]string, 0)
    placement := make([][]string, n)
    for i := 0; i < n; i++ {
        placement[i] = make([]string, n)
        for j := 0; j < n; j++ {
            placement[i][j] = "."
        }
    }
    placeQueens(0, placement, &allPlacements)

    return allPlacements
}