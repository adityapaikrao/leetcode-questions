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

    prev := make([]int, len(w2) + 1)
    for j := range prev{
        prev[j] = len(w2) - j
    }

    for i := len(w1) - 1; i >= 0; i--{
        curr := make([]int, len(w2) + 1)
        curr[len(w2)] = len(w1) - i
        for j := len(w2) - 1; j >= 0; j--{
            if w1[i] == w2[j] {
                curr[j] = prev[j + 1]
            } else{
                curr[j] = 1 + min(curr[j + 1], prev[j], prev[j + 1])
            }
        }
        copy(prev, curr)
    }

    return prev[0]
}