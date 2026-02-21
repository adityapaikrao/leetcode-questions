var directions = [4][2]int{{0, -1}, {0, 1}, {1, 0}, {-1, 0}}

func isInBounds(rowIdx, colIdx, numRows, numCols int) bool{
    return rowIdx >= 0 && rowIdx < numRows && colIdx >=0 && colIdx < numCols
}

func findWord(wordIndex int, board *[][]byte, word *string, boardRow, boardCol int) bool{
    if wordIndex == len(*word){
        return true
    }
    if (*word)[wordIndex] != (*board)[boardRow][boardCol]{
        return false
    }
    if wordIndex == len(*word) - 1{
        return true 
    }
    // mark current elem as visited
    currVal := (*board)[boardRow][boardCol]
    (*board)[boardRow][boardCol] = byte('x')

    for _, offset := range directions{
        newRow := boardRow + offset[0]
        newCol := boardCol + offset[1]
        if isInBounds(newRow, newCol, len(*board), len((*board)[0])) && findWord(wordIndex + 1, board, word, newRow, newCol){
            return true
        }
    }
    // backtrack to original value
    (*board)[boardRow][boardCol] = currVal
    return false

}

func exist(board [][]byte, word string) bool {
    for i := range board{
        for j := range board[0]{
            if findWord(0, &board, &word, i, j){
                return true
            }
        }
    }
    return false
}