func numDistinct(s string, t string) int {
    if len(t) > len(s){
        return 0
    }

    prev := make([]int, len(s) + 1)

    for j := range prev{
        prev[j] = 1
    }

    for i := len(t) - 1; i >= 0; i--{
        curr := make([]int, len(s) + 1)
        for j := len(s) - 1; j >= 0; j--{
            if t[i] == s[j]{
                curr[j] += prev[j + 1]
            }
            curr[j] += curr[j + 1]
        }

        copy(prev, curr)
    }

    return prev[0]

}