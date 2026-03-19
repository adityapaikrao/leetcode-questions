/*
aaab
a*b

s = aa  p = a*

(i, j, prev) -> can match s[i:] with p[j:] given p[j-1] = prev?
i: 0 to n
j: 0 to m
prev: enum char 26 + 2
    
aa a*
i. j

case p[j] = .
    next -> (i + 1, j + 1, .)
case p[j] = char 
    b  cd 
    s[i] != p[j] :if prev is char -> false
                 ->(i + 1, j + 1, char) // next char could be *
    s[i] == p[j] -> (i + 1, j + 1, char) // matches
case p[j] = *  ba a*ba
    if s[i-1] != p[j-1] -> (i, j + 1, p[j-2] or '')
    if s[i] == p[j] : (i + 1, j, prev) // continue run for *
                    : (i + 1, j + 1, prev) //end run for *
*/
// func intToBool(x int) bool{
//     if x == 1{
//         return true
//     } 
//     return false
// }

func canRemove(j int, p string) bool{
    i := len(p) - 1
    for i >= j{
        if p[i] != '*'{
            return false
        }
        i -= 2
    }
    return true
}

func isMatch(s string, p string) bool {
    // var matches func(i, j int) bool
    // memo := make([][]int, len(s) + 1)
    // for i := range memo{
    //     memo[i] = make([]int, len(p) + 1)
    //     for j := range memo[i]{
    //         memo[i][j] = -1
    //     }
    // }

    // matches = func(i, j int) bool {
    //     if memo[i][j] != -1{
    //         return intToBool(memo[i][j])
    //     }

    //     // Base Cases
    //     if i == len(s) && j == len(p){
    //         return true
    //     }
    //     if j == len(p){
    //         return false
    //     }
    //     if i == len(s){
    //         return canRemove(j, p)
    //     }

    //     // Recurrence
    //     nextChar := byte('#')
    //     if j + 1 < len(p){
    //         nextChar = p[j + 1]
    //     }
    //     matched := false

    //     if nextChar == '*'{
    //         // match 
    //         if i < len(s) && (s[i] == p[j] || p[j] == '.'){
    //             matched = matches(i + 1, j)
    //         }

    //         // skip using
    //         matched = matched || matches(i, j + 2) 
    //     } else {
    //         if i == len(s){
    //             memo[i][j] = 0
    //             return false
    //         }
    //         if p[j] == '.' {
    //             matched = matched || matches(i + 1, j + 1)
    //         } else {
    //             matched = matched || (s[i] == p[j] && matches(i + 1, j + 1))
    //         }
    //     }

    //     memo[i][j] = 0
    //     if matched {memo[i][j] = 1}
    //     return matched
    // }

    // return matches(0, 0)

    dp := make([][]bool, len(s) + 1)
    for i := range dp{
        dp[i] = make([]bool, len(p) + 1)
        for j := range dp[i]{
            if i == len(s) && j == len(p){
                dp[i][j] = true
            } else if i == len(s){
                dp[i][j] = canRemove(j, p)
            }
        }
    }

    for i := len(s) - 1; i >= 0; i--{
        for j := len(p) - 1; j >= 0; j--{
            nextChar := byte('#')
            if j + 1 < len(p){
                nextChar = p[j + 1]
            }

            if nextChar == '*'{
                if s[i] == p[j] || p[j] == '.'{
                    dp[i][j] = dp[i + 1][j]
                }
                dp[i][j] = dp[i][j] || dp[i][j + 2]
            } else {
                if p[j] == '.'{
                    dp[i][j] = dp[i + 1][j + 1]
                } else{
                    dp[i][j] = (s[i] == p[j]) && dp[i + 1][j + 1]
                }
            }
        }
    }

    return dp[0][0]
}