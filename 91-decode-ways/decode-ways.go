var memo map[int]int

func getNumWays(s *string, index int) int {
    // memoize:
    if val, ok := memo[index]; ok{
        return val
    }

    // Base Cases: found a way
    if index == len(*s) {
        return 1
    }
    // leading char: 0 or >= 3
    firstChar:= (*s)[index] - '0'
    if firstChar == 0{
        return 0
    }

    numWays := 0
    // Choose only firstChar
    numWays += getNumWays(s, index + 1)
    // Choose both chars
    if index + 1 < len(*s){
        nextChar := (*s)[index + 1] - '0'
        if (*s)[index] == '1' || ((*s)[index] == '2' && nextChar <= 6) {
            numWays += getNumWays(s, index + 2)
        }
    }
    
    memo[index] = numWays
    return numWays

}


func numDecodings(s string) int {
    // leading zeros, cannot decode
    if len(s) == 0 || s[0] == '0'{
        return 0
    }
    memo = make(map[int]int, len(s) + 1)
    return getNumWays(&s, 0)

}