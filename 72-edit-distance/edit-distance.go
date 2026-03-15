/*
w1 = horse
w2 = ros

(i, j) - > num operations needed to convert w1[i:] into w2[j:]
if w1 empty -> length of w2 // insert all 
if w2 empty -> length of w1 // remove all

if equal -> (i + 1, j + 1)
else -> MIN OF (i, j + 1) & (i + 1, j) & (i + 1, j + 1)

*/

func minDistance(w1 string, w2 string) int {
    var solve func(i, j int) int
    memo := make([][]int, len(w1) + 1)
    for i := range memo {
        memo[i] = make([]int, len(w2) + 1)
        for j := range memo[i] {
            memo[i][j] = -1
        }
    } 

    solve = func(i, j int) int {
        if memo[i][j] != -1 {
            return memo[i][j]
        }

        // Base Cases
        if i == len(w1) {
            return len(w2[j:])
        }
        if j == len(w2) {
            return len(w1[i:])
        }

        // Recurrence
        if w1[i] == w2[j]{
            memo[i][j] = solve(i + 1, j + 1)
            return memo[i][j]
        }
        memo[i][j] = min(1 + solve(i + 1, j), 1 + solve(i, j + 1), 1 + solve(i + 1, j + 1))
        return memo[i][j]
    }

    return solve(0, 0)
}